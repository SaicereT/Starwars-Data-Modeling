import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

    

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    height = Column(Integer, nullable=True)
    mass = Column(Integer, nullable=True)
    hair_color = Column(Integer, nullable=True)
    skin_color = Column(Integer, nullable=True)
    eye_color = Column(Integer, nullable=True)
    birth_year = Column(String(250), nullable=True)
    gender = Column(String(250), nullable=True)
    name = Column(String(250), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    diameter = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    gravity = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)
    climate = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    surface_water = Column(Integer, nullable=False)
    name = Column(Integer, nullable=False)

class Fave_planets(Base):
    __tablename__ = "fave_planets"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship (User, backref= 'user', lazy=True)
    planet_id = Column (Integer, ForeignKey('planets.id'))
    planet = relationship (Planets, backref= 'planets', lazy=True)

class Fave_characters(Base):
    __tablename__ = "fave_characters"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship (User, backref= 'user', lazy=True)
    character_id = Column(Integer, ForeignKey('characters.id'))
    character = relationship (Characters, backref= 'characters', lazy=True)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
