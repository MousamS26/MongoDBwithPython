import pymongo
#DELETING DATA
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['dbmsl']
collection = db['students']
#DELETING SINGLE DOCUMENT
DocToBeDeleted = {'name': 'Harsh'}
collection.delete_one(DocToBeDeleted)
abc = collection.find_one({'name': 'Harsh'})
print(abc)
#DELETING MULTIPLE DOCUMENTS
DocsToBeDeleted = {'department': 'IN'}
collection.delete_many(DocsToBeDeleted)
abcd = collection.find_one({'department': 'IN'})
print(abcd)