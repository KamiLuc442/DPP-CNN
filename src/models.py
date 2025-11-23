from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movies'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genres = Column(String)
    
    links = relationship("Link", back_populates="movie")
    ratings = relationship("Rating", back_populates="movie")
    tags = relationship("Tag", back_populates="movie")


class Link(Base):
    __tablename__ = 'links'
    
    movieId = Column(Integer, ForeignKey('movies.id'), primary_key=True)
    imdbId = Column(String)
    tmdbId = Column(String)
    
    movie = relationship("Movie", back_populates="links")


class Rating(Base):
    __tablename__ = 'ratings'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, nullable=False)
    movieId = Column(Integer, ForeignKey('movies.id'))
    rating = Column(Float)
    timestamp = Column(String)
    
    movie = relationship("Movie", back_populates="ratings")


class Tag(Base):
    __tablename__ = 'tags'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, nullable=False)
    movieId = Column(Integer, ForeignKey('movies.id'))
    tag = Column(String)
    timestamp = Column(String)
    
    movie = relationship("Movie", back_populates="tags")
