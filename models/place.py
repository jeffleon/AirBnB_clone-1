#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import models
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, String, Float, Integer
from sqlalchemy import *
from sqlalchemy.orm import relationship, backref
import os

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60), ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60), ForeignKey
                             ("amenities.id"), primary_key=True,
                             nullable=False))

storage_type = os.getenv("HBNB_TYPE_STORAGE")


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    if storage_type == "db":
        amenities = relationship("Amenity",
                                 secondary="place_amenity",
                                 viewonly=False)
        '''
        reviews = relationship("Review",
                               cascade="all,delete",
                               backref=backref("place", cascade="all,delete"))
        '''
    if storage_type != "db":
        '''
        @property
        def reviews(self):
            """Return list of review"""
            from models import storage
            reviews = list()
            for key, value in storage.all().items():
                if value.place_id == self.id:
                    reviews.append(value)
            return reviews
        '''
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
