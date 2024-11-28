from pymongo import MongoClient

class DatabaseConnection:
    def __init__(self, connection_string, db_name, collection_name):
        self.client = MongoClient(connection_string)
        self.database = self.client[db_name]
        self.collection = self.database[collection_name]

    def insert_one(self, data):
        return self.collection.insert_one(data)

    def find_all(self):
        return self.collection.find().sort("index", 1)
