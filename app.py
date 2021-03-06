import os
from flask import Flask
from flask import Response
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request, json
import logging

logging.basicConfig(filename='app.log',level=logging.DEBUG, format='%(asctime)s %(message)s')

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/deliberate-action'
mongo = PyMongo(app)

@app.route('/')
def index():
    return 'Deliberate Practice, Deliberate Action .... Refine your mental models ....'

@app.route('/templates')
def templateList():
    logging.debug('templateList()')
    templates = mongo.db.templates.find({})
    resp = dumps(templates)
    return Response(resp, mimetype='application/json')

@app.route('/templates/<id>')
def templateById(id):
    logging.debug(f'templateById({id})')

    query = {
        "_id": ObjectId(id)
    }
    template = mongo.db.templates.find_one_or_404(query)
    resp = dumps(template)
    return Response(resp, mimetype='application/json')

# TODO make this a unique index
@app.route('/templates/<type>/<name>/<int:user>')
def templateByKey(type, name, user):
    logging.debug(f'templateByKey({type}, {name}, {user})')
    query = {
        "type": f'{type}',
        "name": f'{name}',
        "user": user
    }
    template = mongo.db.templates.find_one_or_404(query)
    resp = dumps(template)
    return Response(resp, mimetype='application/json')

@app.route('/templates/default')
def getDefaultTemplate():
    logging.debug('getDefaultTemplate()')

    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/templates", "session-template-default.json")
    resp = dumps(json.load(open(json_url)))
    return Response(resp, mimetype='application/json')

@app.route('/sessions')
def sessionList():
    logging.debug('sessionList()')

    domains = []
    for doc in mongo.db.sessions.find():
        domains.append(asDomainObj(doc))

    # logging.debug(f'domains are {domains}')
    dumpedDomains = dumps(domains)
    # logging.debug(f'dumpedDomains are {dumpedDomains}')

    # sessions = mongo.db.sessions.find()
    # resp = dumps(sessions)
    # logging.debug(f'resp are {resp}')
    # for session in resp:
    #     asDomainObj(session)

    return Response(dumpedDomains, mimetype='application/json')

@app.route('/sessions/<id>', methods=['GET'])
def getSession(id):
    logging.debug(f'getSession({id})')

    query = {"_id": ObjectId(id)}
    doc = mongo.db.sessions.find_one_or_404(query)

    return Response(dumps(asDomainObj(doc)), mimetype='application/json')

@app.route('/sessions', methods=['POST'])
def addSession():
    logging.debug('addSession()')
    _json = request.json
    _startDateTime = _json['startDateTime']
    _endDateTime = _json['endDateTime']
    _preResponses = _json['preResponses']
    _postResponses = _json['postResponses']
	# TODO validate the received values and save or error
    # NOTE: user and template_id are always defaulted for now
    id = mongo.db.sessions.insert({
        'user': 1,
        'template_id': "default",
        'startDateTime': _startDateTime,
        'endDateTime': _endDateTime,
        'preResponses': _preResponses,
        'postResponses': _postResponses,
        })
    logging.debug(f'id is {id}')
    resp = dumps({ "id": f'{id}' })
    return Response(resp, mimetype='application/json')

@app.route('/sessions/<id>', methods=['PUT'])
def updateSession(id):
    logging.debug('updateSession()')
    _json = request.json
    _startDateTime = _json['startDateTime']
    _endDateTime = _json['endDateTime']
    _preResponses = _json['preResponses']
    _postResponses = _json['postResponses']
	# TODO validate the received values and save or error
    # NOTE: user and template_id are always defaulted for now

    query = { "_id": ObjectId(id) }
    document = {
        'user': 1,
        'template_id': "default",
        'startDateTime': _startDateTime,
        'endDateTime': _endDateTime,
        'preResponses': _preResponses,
        'postResponses': _postResponses,
    }

    result = mongo.db.sessions.update_one(query, {"$set": document})

    resp = dumps({ "matched": f'{result.matched_count}', "modified": f'{result.modified_count}' })
    return Response(resp, mimetype='application/json')

@app.route('/sessions/<id>', methods=['DELETE'])
def deleteSession(id):
    logging.debug('deleteSession()')

    query = {"_id": ObjectId(id)}

    result = mongo.db.sessions.delete_one(query)

    resp = dumps({ "deleted": f'{result.deleted_count}' })
    return Response(resp, mimetype='application/json')

def asDomainObj(entity: dict):
    logging.debug(f'asDomainObj({entity})')
    # logging.debug(f'entity type is {type(entity)}')
    # dumped = dumps(entity)
    # logging.debug(f'dumped type is {type(dumped)}')
    # logging.debug(f'dumped is {dumped}')
    # logging.debug(f'entity id is {dumps(entity["_id"])}')
    # logging.debug(f'startDateTime is {dumps(entity["startDateTime"])}')
    # logging.debug(f'template_id is {entity["template_id"]}')
    id = entity["_id"]
    del(entity["_id"])
    # logging.debug(f'_id is {str(id)}')
    startDateTime = entity["startDateTime"].strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    # logging.debug(f'startDateTime type is {type(startDateTime)}')
    # logging.debug(f'startDateTime entity is {entity["startDateTime"]}')
    # logging.debug(f'startDateTime entity string is {str(entity["startDateTime"])}')
    # logging.debug(f'startDateTime string is {str(startDateTime)}')
    # logging.debug(f'startDateTime is {startDateTime}')
    endDateTime = entity["endDateTime"].strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    # logging.debug(f'endDateTime entity is {entity["endDateTime"]}')
    # logging.debug(f'endDateTime string is {str(endDateTime)}')
    # logging.debug(f'endDateTime is {endDateTime}')
    # formatted = endDateTime.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    # logging.debug(f'formatted is {formatted}')
     # logging.debug(f'entity after del of _id ({entity})')
    entity["id"] = str(id)
    entity["startDateTime"] = startDateTime
    entity["endDateTime"] = endDateTime
    # logging.debug(f'entity after add of id ({entity})')
    return entity

if __name__ == '__main__':
    app.run(debug=True)
