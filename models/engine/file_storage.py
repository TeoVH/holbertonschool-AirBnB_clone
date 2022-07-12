#!/usr/bin/python3
""" Class FileStorage """

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import json

classtype = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review,
}


class FileStorage:
    """ Define the class FileStorage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key """
        n_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(n_name, obj.id)] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        dict = {}
        for key, value in self.__objects.items():
            dict.update({key: value.to_dict()})
        with open(FileStorage.__file_path, "w") as file:
            json.dump(dict, file)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            with open(FileStorage.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    search = classtype[value["__class__"]](**value)
                    dict = {key: search}
                    self.__objects.update(dict)
        except Exception:
            pass
