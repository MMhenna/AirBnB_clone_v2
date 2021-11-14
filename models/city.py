#!/usr/bin/python3
'''
    Define the class City.
'''
import os
from .base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    '''
        Define the class City that inherits from BaseModel.
    '''
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place",
                              backref="cities",
                              cascade="all, delete, delete-orphan")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
