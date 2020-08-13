#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
import models
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship


class User(BaseModel):
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
    places = relationship("Place", backref="user",
                          cascade="all, delete")
