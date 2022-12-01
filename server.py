from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_cors import CORS
import yaml

app = Flask(__name__)
config = yaml.safe_load(open('db.yaml'))
client = MongoClient(config['uri'])
db = client['biomez']
CORS(app)

@app.route('/')
def index():
    return '<h1>Home Page</h1>'

@app.route('/records', methods=['POST', 'GET'])
def data():
    
    # POST record to db
    if request.method == 'POST':
        body = request.json
        articleName = body['articleName']
        authorName = body['authorName'] 
        db['records'].insert_one({
            "articleName": articleName,
            "authorName": authorName
        })
        return jsonify({
            'status': 'Record added successfully',
            'articleName': articleName,
            'authorName': authorName,
        })
    
    # GET record from db
    if request.method == 'GET':
        allData = db['records'].find()
        dataJson = []
        for data in allData:
            id = data['_id']
            articleName = data['articleName']
            authorName = data['authorName']
            dataDict = {
                '_id': str(ObjectId(id)),
                'articleName': articleName,
                'authorName': authorName,
            }
            dataJson.append(dataDict)
        print(dataJson)
        return jsonify(dataJson)

@app.route('/records/<id>', methods=['GET', 'DELETE', 'PUT'])
def onedata(id):

    # GET record by id
    if request.method == 'GET':
        data = db['records'].find_one({'_id': ObjectId(id)})
        id = data['_id']
        articleName = data['articleName']
        authorName = data['authorName']
        dataDict = {
            '_id': str(ObjectId(id)),
            'articleName': articleName,
            'authorName': authorName,
        }
        print(dataDict)
        return jsonify(dataDict)
        
    # DELETE record
    if request.method == 'DELETE':
        db['records'].delete_one({'_id': ObjectId(id)})
        print('\n # Deletion successful # \n')
        return jsonify({'status': 'Data id: ' + id + ' is deleted!'})

    # UPDATE record by id
    if request.method == 'PUT':
        body = request.json
        articleName = body['articleName']
        authorName = body['authorName']

        db['records'].update_one(
            {'_id': ObjectId(id)},
            {
                "$set": {
                    "articleName": articleName,
                    "authorName": authorName,
                }
            }
        )
        return jsonify({'status': 'Record updated successfully'})

if __name__ == '__main__':
    app.debug = True
    app.run()