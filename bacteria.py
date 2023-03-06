import pymongo
from bson import ObjectId

class Bacteria:
    def __init__(self, uri, database):
        self.client = pymongo.MongoClient(uri)
        self.database = database
        self.collection = "bacteria"
        self.db_collection = self.client[database][self.collection]
