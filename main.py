import pymongo
#CREATING DATABASE AND INSERTING DOCUMENTS INTO COLLECTION.

if __name__== "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client['dbmsl']
    collection = db['students']
    #INSERTING SINGLE DOCUMENT
    dictionary = {'name': 'Mousam', 'department': 'CS', 'roll_no': 23, 'sgpa': 9.6 }
    #INSERTING MULTIPLE DOCUMENTS
    collection.insert_one(dictionary)
    dictionaries = [
        {'name': 'Anuj', 'department': 'CS', 'roll_no': 24, 'sgpa': 5.6},
        {'name': 'Shrujan', 'department': 'CS', 'roll_no': 25, 'sgpa': 6.6},
        {'name': 'Sagar', 'department': 'IT', 'roll_no': 34, 'sgpa': 7.6},
        {'name': 'Harsh', 'department': 'ME', 'roll_no': 56, 'sgpa': 8.6}
    ]
    collection.insert_many(dictionaries)