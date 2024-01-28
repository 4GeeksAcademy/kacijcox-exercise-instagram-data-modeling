import enum
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy import Enum

Base = declarative_base()

class Follower (Base):
    __tablename__ = 'follower'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, nullable=False)
    user_to_id = Column(Integer, nullable=False)
   
class User (Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250))
    firstname = Column(String(250))
    lastname = Column(String(250), nullable=False)
    email = Column(String(250))
    follower = relationship("Follower")
    follower = Column(Integer, ForeignKey('follower.id'))

   
class Media (Base):
    __tablename__ = 'media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    type = Column(Enum, primary_key=True)
    url = Column(String(250))
    post_id = Column(String(250))

class Comment (Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    make = Column(String(250))
    model = Column(String(250))

class Post (Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(String(250))
    follower = relationship("Follower")
    user = relationship("User")
    media = relationship("Media")
    post = relationship("Post")
    comment = relationship("Comment")
    follower = Column(Integer, ForeignKey('follower.id'))
    user = Column(Integer, ForeignKey('user.id'))
    media = Column(Integer, ForeignKey('media.id'))
    comment = Column(Integer, ForeignKey('comment.id'))
    post = Column(Integer, ForeignKey('post.id'))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')


