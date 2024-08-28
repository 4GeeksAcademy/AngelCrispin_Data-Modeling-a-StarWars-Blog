import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean,DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    active = Column(Boolean, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(Boolean, onupdate=datetime.now)

class Character(Base):
    __tablename__ = 'Character'
    id = Column(Integer, primary_key=True)
    birth_year = Column(String(250))
    eye_color = Column(String(250))
    gender = Column(String(250))
    hair_color = Column(String(250))
    height = Column(String(250))
    homeworld = Column(String(250))
    mass = Column(String(250))
    name = Column(String(250))
    skin_color = Column(String(250))
    height = Column(String(250))
    species = Column(String(250))
    starships = Column(String(250))
    url = Column(String(250))
    vehicles = Column(String(250))
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(Boolean, onupdate=datetime.now)

class Starship(Base):
    __tablename__ = 'Starship'
    id = Column(Integer, primary_key=True)
    MGLT = Column(String(250))
    cargo_capacity = Column(String(250))
    consumables = Column(String(250))
    cost_in_credits = Column(String(250))
    crew = Column(String(250))
    hyperdrive_rating = Column(String(250))
    length = Column(String(250))
    manufacturer = Column(String(250))
    max_atmosphering_speed = Column(String(250))
    model = Column(String(250))
    name = Column(String(250))
    passengers = Column(String(250))
    films = Column(String(250))
    pilots = Column(String(250))
    starship_class = Column(String(250))
    url = Column(String(250))
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(Boolean, onupdate=datetime.now)

class Planet(Base):
    __tablename__ = 'Planet'
    id = Column(Integer, primary_key=True)
    diameter = Column(String(250))
    films = Column(String(250))
    gravity = Column(String(250))
    name = Column(String(250))
    orbital_period = Column(String(250))
    population = Column(String(250))
    residents = Column(String(250))
    rotation_period = Column(String(250))
    surface_water = Column(String(250))
    terrain = Column(String(250))
    url = Column(String(250))
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(Boolean, onupdate=datetime.now)

class FavoriteCharacter(Base):
    __tablename__ = 'FavoriteCharacter'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.id"), nullable=False)
    character_id = Column(Integer, ForeignKey("Character.id"), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)

class FavoriteStarship(Base):
    __tablename__ = 'FavoriteStarship'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.id"), nullable=False)
    starship_id = Column(Integer, ForeignKey("Starship.id"), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)

class FavoritePlanet(Base):
    __tablename__ = 'FavoritePlanet'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.id"), nullable=False)
    planet_id = Column(Integer, ForeignKey("Planet.id"), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
