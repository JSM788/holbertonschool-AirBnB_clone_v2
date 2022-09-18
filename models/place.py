#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship
import models
import os

tables = Table("place_amenity", Base.metadata,
               Column("place_id", String(60),
                      ForeignKey("places.id"),
                      primary_key=True, nullable=False),
               Column("amenity_id", String(60),
                      ForeignKey("amenities.id"),
                      primary_key=True, nullable=False))


class Place(BaseModel, Base):

    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)
    amenity_ids = []

    if os.getenv("HBNB_TYPE_STORAGE") != "db":

        @property
        def reviews(self):
            """ Creation of getter of reviews """
            newList = []
            allClass = models.storage.all(Review)
            for key, value in allClass.items():
                if value.place_id == self.id:
                    newList.append(value)
            return newList

        @property
        def amenities(self):
            """That returns of list amenity instances"""
            newList = []
            allClass = models.storage.all(Amenity)
            for key, value in allClass.items():
                if value.id == self.amenity_ids:
                    newList.append(value)
            return newList

        @amenities.setter
        def amenities(self, value):
            """Setter attribute amenities that handles append method for add"""
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
