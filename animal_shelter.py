from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:54887/?authMechanism=DEFAULT&authSource=AAC' % (username, password))
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            result = self.database.animals.insert_one(data)  # data should be dictionary
            return result.acknowledged
        else:
            raise Exception("Nothing to save, because data parameter is empty.")
            return False

# Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            result = self.database.animals.find(data, {"_id": False})  # data should be dictionary
        if result.count() > 0:
            return result
        else:
            raise Exception("Nothing to search, because data parameter is empty.")
            return False
               
# Create method to implement U in CRUD.
    def update(self, data, updateData):
        result = self.database.animals.update_one(data, updateData)  # data should be dictionary
        if result.modified_count:
            return result.raw_result
        else:
            raise Exception("Nothing to update, because data parameter is empty.")
            return False

# Create method to implement D in CRUD.
    def delete(self, data):
        result = self.database.animals.delete_one(data)  # data should be dictionary
        if result.deleted_count:
            return result.raw_result
        else:
            raise Exception("Nothing to delete, because data parameter is empty.")
            return False