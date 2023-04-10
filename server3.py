from flask import Flask, request, jsonify
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from bson.objectid import ObjectId
from flask_cors import CORS
import yaml

# Initialize Flask app and MongoDB connection
app = Flask(__name__)
config = yaml.safe_load(open('db.yaml'))
client = MongoClient(config['uri'])
db = client['biomez']
CORS(app)

# Error handling for 404 error
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

# Error handling for 400 error
@app.errorhandler(DuplicateKeyError)
def resource_not_found(e):
    return jsonify(error=f"Duplicate key error."), 400

# Default route
@app.route('/', methods=['GET'])
def home():
    msg = "Biome-z Database"
    return(msg)

# Route for searching MongoDB using the search term received from the front-end.
# This function accepts json in the following format: 
# { "q": <search term string> }
@app.route('/post-json', methods=['POST','GET'])
def postJsonHandler():
    query = request.json['q']
    records = db.records

    result = records.find(
        { "$text": {
            "$search": query
        }
        }
    )
    data = []
    for doc in result:
        doc['_id'] = str(doc['_id']) 
        data.append(doc)
    print(data)
    return jsonify(data)

# Route for processing POST and GET requests respectively.
# POST implementation inserts a record into the database 
# GET implementation returns all records within the database
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
    
    # GET records from db
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

# Route for processing GET, DELETE, and PUT reuests for a single record using its object _id
# Example: http://127.0.0.1:5000/records/63ff6e901e2e79534ebcddf5
# GET implementation returns a single record if _id is found
# DELETE implementation removes a single record if _id is found
# PUT implementation updates a single record if _id is found 
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
