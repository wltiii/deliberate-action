from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/deliberate-action'
mongo = PyMongo(app)
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/templates')
def getTemplates():
    templates = mongo.db.templates.find({})
    resp = dumps(templates)
    return resp

@app.route('/template/<type>/<name>/<user>')
def getTemplate(type, name, user):
    print(f'getTemplate({type}, {name}, {user})')
    query = {
        "type": f'{type}',
        "name": f'{name}',
        "user": int(user)
    }
    print (f'query is {query}')
    default_template = mongo.db.templates.find(query)
    resp = dumps(default_template)
    return resp

@app.route('/sessions')
def getSessions():
    default_template = mongo.db.templates.find({
        "type": "session",
        "name": "default",
        "user": 0
    })
    resp = dumps(default_template)
    return resp

if __name__ == '__main__':
    app.run(debug=True)
