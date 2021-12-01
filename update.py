import pymongo
#UPDATING THE DATA
client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client)
db = client['dbmsl']
collection = db['students']
docToBeChanged = {'name': 'Mousam'}
changesToBeMade = {"$set": {'sgpa': 9.9}}
#UPDATING SINGLE DOCUMENTS
collection.update_one(docToBeChanged, changesToBeMade)
abc = collection.find_one({'name': 'Mousam'})
print(abc)
#UPDATING MULTIPLE DOCUMENTS
docToBeChangedAgain = {'department': 'CS'}
changesToBeMadeAgain = {"$set": {'department': 'IN'} }
collection.update_many(docToBeChangedAgain, changesToBeMadeAgain)
findingMultiple = collection.find({'department': 'IN'})
for everyitem in findingMultiple:
    print(everyitem)