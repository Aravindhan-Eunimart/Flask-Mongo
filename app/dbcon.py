from pymongo import MongoClient


client = MongoClient("mongodb+srv://todo:todo@cluster0.kt1j0.mongodb.net/?retryWrites=true&w=majority")
db = client.FlaskMongo
student_collection = db.student_collection
