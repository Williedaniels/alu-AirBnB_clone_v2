#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from dotenv import load_dotenv


load_dotenv()

storage_type = getenv("HBNB_TYPE_STORAGE")
print(f"HBNB_TYPE_STORAGE: {storage_type}")

if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()

classes = {
    "BaseModel": BaseModel,
    "State": State,
    "City": City,
    "User": User,
    "Place": Place,
    "Amenity": Amenity,
    "Review": Review,
}