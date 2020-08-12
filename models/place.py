#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import models
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, String, Float, Integer
from sqlalchemy import *
from sqlalchemy.orm import relationship
import os

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60), ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60), ForeignKey
                             ("amenities.id"), primary_key=True,
                             nullable=False))

storage_type = os.getenv('HBNB_TYPE_STORAGE')

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"))
    user_id = Column(String(60), ForeignKey("users.id"))
    name = Column(String(128))
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    if storage_type == "db":
        amenities = relationship("Amenity",
                                 secondary="place_amenity",
                                 viewonly=False)

    if storage_type != "db":
        @property
        def amenities(self):
            """ Return a list of amenity instances based on the attribute
amenity_ids that contains all Amenity.id linked to the Place"""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj):
            """handles append method for adding an Amenity.id to the attribute
amenity_ids."""
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
