import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    favoritos = relationship("Favoritos",backref="owner",lazy=True)


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name= Column(String(250), nullable=False)
    height= Column(String(250), nullable=False)
    gender= Column(String(250), nullable=False)
    favoritos = relationship("Favoritos",backref="owner",lazy=True)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name= Column(String(250), nullable=False)
    climate= Column(String(10), nullable=False)
    terrain= Column(String(10), nullable=False)
    favoritos = relationship("Favoritos",backref="owner",lazy=True)


class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name= Column(String(250), nullable=False)
    model= Column(String(10), nullable=False)
    class_name=Column(String(10), nullable=False)
    favoritos = relationship("Favoritos",backref="owner",lazy=True)

class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)

    usuario_id = Column(Integer, ForeignKey('usuario.id'),nullable=False)
    character_id= Column(Integer, ForeignKey('character.id'),nullable=True)
    planet_id= Column(Integer, ForeignKey('planet.id'),nullable=True)
    vehicle_id= Column(Integer, ForeignKey('vehicle.id'),nullable=True)




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
