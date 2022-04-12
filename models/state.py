#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="delete")

    @property
    def cities(self):
        """Returns a list of cities with cities.state_id = self.id"""
        cities_list = []
        for city in self.cities:
            if self.id = city.state_id:
                cities_list.push(city)
        return cities_list
