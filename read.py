import pymongo
#READING THE DATA
client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client)
db = client['dbmsl']
collection = db['students']
#READING SINGLE DOCUMENT
findingOne = collection.find_one({'name': 'Mousam'})
print(findingOne)
#READING MULTIPLE DOCUMENTS
findingMultiple = collection.find({'department': 'CS'})
for everyitem in findingMultiple:
    print(everyitem)
