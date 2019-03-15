# Remove this connection string
import pymongo
uri = "mongodb://ingress233:JjYA9g5njmSWgmvVaLvOTKXpoxs3yilbemxsk8RCmnPxSoSqyjlvUR7OMEzU00ldmDnUG0aVufi7AE3FAnIwyQ==@ingress233.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
client = pymongo.MongoClient(uri)

# PyMongo https://api.mongodb.com/python/current/