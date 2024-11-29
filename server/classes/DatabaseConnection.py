from pymongo import MongoClient, errors

class DatabaseConnection:
    def __init__(self, connection_string, db_name, collection_name):
        try:
            self.client = MongoClient(connection_string, maxPoolSize=50, serverSelectionTimeoutMS=5000, tls=True, tlsAllowInvalidCertificates=False)
            self.database = self.client[db_name]
            self.collection = self.database[collection_name]
        except errors.ConnectionFailure as e:
            raise Exception(f"Failed to connect to MongoDB: {e}")

    def insert_one(self, data):
        """Insert a single document into the collection."""
        try:
            result = self.collection.insert_one(data)
            return result.inserted_id
        except errors.PyMongoError as e:
            raise Exception(f"Failed to insert document: {e}")

    def get_all_documents(self, filter_query=None, projection=None, sort_field="index"):
        """
        Retrieve all documents from the collection.

        Args:
            filter_query (dict, optional): MongoDB filter query. Defaults to {} (all documents).
            projection (dict, optional): Fields to include/exclude in results. Defaults to None (all fields).
            sort_field (str, optional): Field to sort by. Defaults to "index".

        Returns:
            list: List of documents.
        """
        filter_query = filter_query or {}
        try:
            return list(self.collection.find(filter_query, projection).sort(sort_field, 1))
        except errors.PyMongoError as e:
            raise Exception(f"Failed to retrieve documents: {e}")

    def close(self):
        """Close the MongoDB connection."""
        self.client.close()
