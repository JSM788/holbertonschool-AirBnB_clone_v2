#!/usr/bin/python3
""" State Module for HBNB project """
<<<<<<< HEAD
from models.base_model import BaseModel
from sqlalchemy import Column, String
=======
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
import models
from models.city import City
from os import getenv
>>>>>>> 0d16544016d37875bd2abdc66c4ef3cc152ddbd2

"""
class State(BaseModel):
    
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
"""

class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        cities = relationship("City", backref="state", cascade="all,delete")

    else:
        @property
        def cities(self):
            """ Creation of getter cities"""
            newList = []
            allClass = models.storage.all(City)
            for city in allClass.values():
                if city.state_id == self.id:
                    newList.append(city)
            return newList
