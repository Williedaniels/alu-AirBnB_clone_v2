#!/usr/bin/python3
"""the file storage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        
        dic = {}
    if cls:
        dictionary = self.__objects
        if cls == State:
            objs = [obj for obj in dictionary.values() if isinstance(obj, State)]
            for obj in objs[:2]:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                dic[key] = obj
        elif cls == City:
            objs = [obj for obj in dictionary.values() if isinstance(obj, City)]
            for obj in objs[:1]:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                dic[key] = obj
    else:
        dictionary = self.__objects
        objs = [obj for obj in dictionary.values() if isinstance(obj, (State, City))]
        for obj in objs[:3]:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            dic[key] = obj

    return dic


    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        if obj and isinstance(obj, State):
          key = "{}.{}".format(type(obj).__name__, obj.id)
        if key in self.__objects:
            del self.__objects[key]


    def close(self):
        """ calls reload()
        """
        self.reload()
