#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place",
                          backref=backref("user",
                                          cascade="all, delete, delete-orphan"))
    reviews = relationship("Review",
                           backref=backref("user",
                                           cascade="all, delete, delete-orphan"))
