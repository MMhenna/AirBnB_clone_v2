#!/usr/bin/python3
'''
    Package initializer
'''

from engine.file_storage import FileStorage
from base_model import BaseModel
from user import User
from place import Place
from state import State
from city import City
from amenity import Amenity
from review import Review
import os

classes = {"User": User, "BaseModel": BaseModel,
           "Place": Place, "State": State,
           "City": City, "Amenity": Amenity,
           "Review": Review}


if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    from engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()