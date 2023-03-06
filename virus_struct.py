import pymongo
from bson import ObjectId

class ViruStruct:
    def __init__(self, uri, database):
        self.client = pymongo.MongoClient(uri)
        self.database = database
        self.collection = "virus_struct"
        self.db_collection = self.client[database][self.collection]


    def update_key_collection(self, object_id, key, new_key):
        object_id = ObjectId(object_id)
        if key == new_key:
            print("The key value and the new key value are equal")
            return

        self.db_collection.update_one(
            {"_id": object_id},
            {"$rename": {key: new_key}}
        )
        print("Now " + key + " is "+ new_key)   

    
    def insert_key_collection(self, object_id, key, key_value=None):
        object_id = ObjectId(object_id)
        self.db_collection.insert_one({key: key_value})