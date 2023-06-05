import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User (Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    userName = Column(String(250), nullable=False)
    firstName = Column(String (250), nullable=False)
    lasttName = Column(String (250), nullable=False)
    email = Column(String (250))
   

class Follower (Base):
    __tablename__ = 'Follower'
    user_from_id=Column(Integer,primary_key=True,)
    user_to_id=Column(Integer,ForeignKey('user.id'))
    user=relationship (User)

    def to_dict(self):
        return {}

class Post (Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    user_id=Column(Integer)


class Publishing (Base):
    __tablename__ = 'Publishing'
    id = Column(Integer, primary_key=True)
    date=Column(Integer)
    user_publish=Column(String(20), ForeignKey('user.id'))
    user=relationship(User)

    def to_dict(self):
        return {}

class Adverstising (Base):
    __tablename__ = 'Advertising'
    id = Column(Integer, primary_key=True)
    ads_length= Column(Integer)
   

class Images (Base):
    __tablename__ = 'Images'
    id = Column(Integer, primary_key=True)
    quantity= Column(Integer)
    id_post = Column (Integer, ForeignKey('post.id'))
    post=relationship(Post)

    def to_dict(self):
        return {}


class Comment (Base):
    __tablename__ = 'Comment'
    id = Column(Integer, primary_key=True)
    comment_text=Column(String(250))
    author_id=Column(Integer,ForeignKey('user.id'))
    user=relationship(User)
    post_id=Column(Integer,ForeignKey('post.id'))
    post=relationship(Post)
    
    def to_dict(self):
        return {}


class Likes (Base):
   __tablename__ = 'Likes'
   id = Column(Integer, primary_key=True)
   amount= Column(Integer)
   id_comment = Column (Integer, ForeignKey('comment.id'))
   comment=relationship(Comment)

   def to_dict(self):
        return {}


class Media(Base):
    __tablename__ = 'Media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    type = Column(String(250))
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
