#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

classes = {
    "BaseModel": BaseModel,
    "State": State,
    "City": City,
    "User": User,
    "Place": Place,
    "Amenity": Amenity,
    "Review": Review,
}

if os.getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage

    storage = DBStorage()
    storage.reload()
else:

    from models.engine.file_storage import FileStorage

    storage = FileStorage()
    storage.reload()