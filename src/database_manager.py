from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

DB_NAME = 'fox.db'


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    login = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    # Связь с Progress
    progress = relationship("Progress", back_populates="user", cascade="all, delete-orphan")
    # Связь с Settings
    settings = relationship("Settings", back_populates="user", uselist=False, cascade="all, delete-orphan")


class Progress(Base):
    __tablename__ = 'progress'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    score = Column(Integer, nullable=False)
    completed = Column(Boolean, nullable=False)
    time_spent = Column(Integer, nullable=False)

    # Обратная связь с User
    user = relationship("User", back_populates="progress")


class Words(Base):
    __tablename__ = 'words'

    id = Column(Integer, primary_key=True)
    word = Column(String, nullable=False)


class Settings(Base):
    __tablename__ = 'settings'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    sound_volume = Column(Float, nullable=False, default=1.0)
    music_volume = Column(Float, nullable=False, default=1.0)
    language = Column(String, nullable=False, default="en")

    # Связь с User
    user = relationship("User", back_populates="settings")
