from pymongo import MongoClient
import gridfs

client = MongoClient("localhost", 27017)
db = client["rescue_app"]
users_collection = db["users"]
reports_collection = db["reports"]
fs = gridfs.GridFS(db)
