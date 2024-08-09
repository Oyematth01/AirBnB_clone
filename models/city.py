#!/usr/bin/python3
""" This is city module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class has state ID and name for managing the city objects """
    state_id = ""
    name = ""
