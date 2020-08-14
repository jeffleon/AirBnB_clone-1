#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()
time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initialize the class object"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """String representation of the baseModel"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at with the current
        datetime"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the
        instance"""
        instanceDict = self.__dict__.copy()
        instanceDict["__class__"] = str(self.__class__.__name__)
        instanceDict["created_at"] = self.created_at.isoformat()
        instanceDict["updated_at"] = self.updated_at.isoformat()
        if "_sa_instance_state" in instanceDict:
            del instanceDict["_sa_instance_state"]
        return instanceDict

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
