from flask import Flask, request, jsonify
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from bson.objectid import ObjectId
from bson.json_util import dumps
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

@app.route('/post-json', methods=['POST'])
def postJsonHandler():
    query = request.json['q']
    records = db.records

    result = records.find(
        { "$text": {
            "$search": query
        }
        }
    )
    return dumps(result)

@app.route('/records', methods=['POST', 'GET'])
def data():
    
    # POST record to db
    if request.method == 'POST':
        body = request.json
        itemType = body['Item Type']
        pubYear = body['Publication Year']
        author = body['Author']
        title = body['Title']
        pubTitle = body['Publication Title']
        issn = body['ISSN']
        doi = body['DOI']
        url = body['Url']
        abstract = body['Abstract Note']
        date = body['Date']
        issue = body['Issue']
        volume = body['Volume']
        libCatalog = body['Library Catalog']
        manualTags = body['Manual Tags']
        autoTags = body['Automatic Tags']
        db['records'].insert_one({
            'Item Type': itemType,
            'Publication Year': pubYear,
            'Author': author,
            'Title': title,
            'Publication Title': pubTitle,
            'ISSN': issn,
            'DOI': doi,
            'Url': url,
            'Abstract Note': abstract,
            'Date': date,
            'Issue': issue,
            'Volume': volume,
            'Library Catalog': libCatalog,
            'Manual Tags': manualTags,
            'Automatic Tags': autoTags
       })
        return jsonify({
            'status': 'Record added successfully',
            'Item Type': itemType,
            'Publication Year': pubYear,
            'Author': author,
            'Title': title,
            'Publication Title': pubTitle,
            'ISSN': issn,
            'DOI': doi,
            'Url': url,
            'Abstract Note': abstract,
            'Date': date,
            'Issue': issue,
            'Volume': volume,
            'Library Catalog': libCatalog,
            'Manual Tags': manualTags,
            'Automatic Tags': autoTags
        })
    
    # GET record from db
    if request.method == 'GET':
        allData = db['records'].find()
        dataJson = []
        for data in allData:
            id = data['_id']
            itemType = data['Item Type']
            pubYear = data['Publication Year']
            author = data['Author']
            title = data['Title']
            pubTitle = data['Publication Title']
            issn = data['ISSN']
            doi = data['DOI']
            url = data['Url']
            abstract = data['Abstract Note']
            date = data['Date']
            issue = data['Issue']
            volume = data['Volume']
            libCatalog = data['Library Catalog']
            manualTags = data['Manual Tags']
            autoTags = data['Automatic Tags']
            dataDict = {
                '_id': str(ObjectId(id)),
                'Item Type': itemType,
                'Publication Year': pubYear,
                'Author': author,
                'Title': title,
                'Publication Title': pubTitle,
                'ISSN': issn,
                'DOI': doi,
                'Url': url,
                'Abstract Note': abstract,
                'Date': date,
                'Issue': issue,
                'Volume': volume,
                'Library Catalog': libCatalog,
                'Manual Tags': manualTags,
                'Automatic Tags': autoTags
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
        itemType = data['Item Type']
        pubYear = data['Publication Year']
        author = data['Author']
        title = data['Title']
        pubTitle = data['Publication Title']
        issn = data['ISSN']
        doi = data['DOI']
        url = data['Url']
        abstract = data['Abstract Note']
        date = data['Date']
        issue = data['Issue']
        volume = data['Volume']
        libCatalog = data['Library Catalog']
        manualTags = data['Manual Tags']
        autoTags = data['Automatic Tags']
        dataDict = {
            '_id': str(ObjectId(id)),
            'Item Type': itemType,
            'Publication Year': pubYear,
            'Author': author,
            'Title': title,
            'Publication Title': pubTitle,
            'ISSN': issn,
            'DOI': doi,
            'Url': url,
            'Abstract Note': abstract,
            'Date': date,
            'Issue': issue,
            'Volume': volume,
            'Library Catalog': libCatalog,
            'Manual Tags': manualTags,
            'Automatic Tags': autoTags
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
        itemType = body['Item Type']
        pubYear = body['Publication Year']
        author = body['Author']
        title = body['Title']
        pubTitle = body['Publication Title']
        issn = body['ISSN']
        doi = body['DOI']
        url = body['Url']
        abstract = body['Abstract Note']
        date = body['Date']
        issue = body['Issue']
        volume = body['Volume']
        libCatalog = body['Library Catalog']
        manualTags = body['Manual Tags']
        autoTags = body['Automatic Tags']
        db['records'].update_one(
            {'_id': ObjectId(id)},
            {
                "$set": {
                    'Item Type': itemType,
                    'Publication Year': pubYear,
                    'Author': author,
                    'Title': title,
                    'Publication Title': pubTitle,
                    'ISSN': issn,
                    'DOI': doi,
                    'Url': url,
                    'Abstract Note': abstract,
                    'Date': date,
                    'Issue': issue,
                    'Volume': volume,
                    'Library Catalog': libCatalog,
                    'Manual Tags': manualTags,
                    'Automatic Tags': autoTags
                }
            }
        )
        return jsonify({'status': 'Record updated successfully'})

if __name__ == '__main__':
    app.debug = True
    app.run()