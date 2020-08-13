#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns the dictionary __objects"""
        if not cls:
            return self.__objects
        if cls:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls.__name__ in key:
                    new_dict[key] = value
        return new_dict

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        for key, value in self.__objects.items():
            if not isinstance(value, dict):
                self.__objects[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                file_object = json.load(f)
            for key, value in file_object:
                self.__objects[key] = classes[file_object[key]["__class__"]]\
                                      (**file_object[key])
        except:
            pass
    def delete(self, obj=None):
        """Delete  obj from __objects if it’s inside  __"""
        if obj is None:
            return
        if obj:
            pattern = "{}.{}".format(obj.__class__.__name__, obj.id)
            if pattern in self.__objects.keys():
                del self.__objects[key]
                self.save()
