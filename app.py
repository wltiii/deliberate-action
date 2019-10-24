from flask import Flask
from flask import Response
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request
import logging
logging.basicConfig(filename='app.log',level=logging.DEBUG, format='%(asctime)s %(message)s')

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/deliberate-action'
mongo = PyMongo(app)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/templates')
def getTemplates():
    logging.debug('getTemplates()')
    templates = mongo.db.templates.find({})
    resp = dumps(templates)
    return resp

@app.route('/templates/<id>')
def findById(id):
    logging.debug(f'findById({id})')
    query = {
        "_id": ObjectId(id)
    }
    template = mongo.db.templates.find_one_or_404(query)
    resp = dumps(template)
    return Response(resp, mimetype='application/json')

@app.route('/templates/<type>/<name>/<user>')
def findByKey(type, name, user):
    logging.debug(f'findByKey({type}, {name}, {user})')
    query = {
        "type": f'{type}',
        "name": f'{name}',
        "user": int(user)
    }
    template = mongo.db.templates.find_one_or_404(query)
    resp = dumps(template)
    return Response(resp, mimetype='application/json')

@app.route('/templates/default')
def getDefaultTemplate():
    logging.debug('getDefaultTemplate()')
    return findByKey('session', 'default', 0)

@app.route('/sessions')
def getSessions():
    logging.debug('getSessions()')
    sessions = mongo.db.sessions.find()
    resp = dumps(sessions)
    return resp

@app.route('/sessions', methods=['POST'])
def addSession():
    logging.debug('addSession()')
    sessions = mongo.db.sessions.find()
    resp = dumps(sessions)
    return resp

@app.route('/sessions/<id>', methods=['PUT'])
def updateSession(id):
    logging.debug('updateSession()')
    sessions = mongo.db.sessions.find()
    resp = dumps(sessions)
    return resp

@app.route('/sessions/<id>', methods=['DELETE'])
def deleteSession(id):
    logging.debug('deleteSession()')
    sessions = mongo.db.sessions.find()
    resp = dumps(sessions)
    return resp

if __name__ == '__main__':
    app.run(debug=True)
