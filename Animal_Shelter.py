from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, userName, password, HOST, PORT, databaseName, collectionName):
        # Initializing the MongoClient. This takes in
        # a username, password, host, port, to
        # access MongoDB databases and collections.
        #
        #
        # database/collection being accessed
        DB = databaseName
        COL = collectionName
        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (userName,password, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
# Create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            try:
                success = self.database.animals.insert_one(data)  # data should be dictionary
                # returns true if successful
                return success.acknowledged
            except:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, lookupData):
        if lookupData is not None:
            # LookupData should be key/value pair
            # LookupData {} sends back full list of documents
            data = self.database.animals.find(lookupData)
        else:
            raise Exception("Bad read on collection")
        return data
            
        
# Create method to implement the U in CRUD.
    def update(self, lookupData, updateData):
        #lookupData/updateData should each be a key/value pair in a dictionary
        if not lookupData:
            raise Exception("lookupData parameter is empty")
        else:
            try:
                if "_id" in lookupData:
                    lookupData["_id"] = ObjectId(lookupData["_id"])
                result = self.database.animals.update_many(lookupData, {"$set":updateData})
            except:
                return "Error updating document"
        
        return result.modified_count
    
# Create method to implement the D in CRUD.
    def delete(self, deleteData):
        #deleteData should be a key/value pair in a dictionary
        if not deleteData:
            raise Exception("deleteData parameter is empty")   
        else:
            try:
                if "_id" in deleteData:
                    deleteData["_id"] = ObjectId(deleteData["_id"])
                result = self.database.animals.delete_many(deleteData)
            except:
                return "Error Deleting Document"
            
        return result.deleted_count
    
    
    
    
    
    
    