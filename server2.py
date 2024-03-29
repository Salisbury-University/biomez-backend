from flask import Flask, request, jsonify
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from bson.objectid import ObjectId
from flask_cors import CORS
import yaml

app = Flask(__name__)
config = yaml.safe_load(open('db.yaml'))
client = MongoClient(config['uri'])
db = client['biomez']
CORS(app)

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@app.errorhandler(DuplicateKeyError)
def resource_not_found(e):
    return jsonify(error=f"Duplicate key error."), 400

@app.route('/records', methods=['POST', 'GET'])
def data():
    
    # POST record to db
    if request.method == 'POST':
        body = request.json
        articleName = body['articleName']
        authorName = body['authorName']
        doi = body['doi']
        db['records'].insert_one({
            "articleName": articleName,
            "authorName": authorName,
            "doi": doi 
        })
        return jsonify({
            'status': 'Record added successfully',
            'articleName': articleName,
            'authorName': authorName,
            'doi': doi
        })
    
    # GET record from db
    if request.method == 'GET':
        allData = db['records'].find()
        dataJson = []
        for data in allData:
            id = data['_id']
            articleName = data['articleName']
            authorName = data['authorName']
            doi = data['doi']
            dataDict = {
                '_id': str(ObjectId(id)),
                'articleName': articleName,
                'authorName': authorName,
                'doi': doi
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
        doi = data['doi']
        dataDict = {
            '_id': str(ObjectId(id)),
            'articleName': articleName,
            'authorName': authorName,
            'doi': doi
        }
        print(dataDict)
        return jsonify(dataDict)
        
    # DELETE record
    if request.method == 'DELETE':
        db['records'].delete_one({'_id': ObjectId(id)})
        print('\n # Deletion successful # \n')
        return jsonify({'status': 'Record (id: ' + id + ') is deleted!'})

    # UPDATE record by id
    if request.method == 'PUT':
        body = request.json
        articleName = body['articleName']
        authorName = body['authorName']
        doi = body['doi']
        db['records'].update_one(
            {'_id': ObjectId(id)},
            {
                "$set": {
                    "articleName": articleName,
                    "authorName": authorName,
                    "doi": doi
                }
            }
        )
        return jsonify({'status': 'Record updated successfully'})

if __name__ == '__main__':
    app.debug = True
    app.run()