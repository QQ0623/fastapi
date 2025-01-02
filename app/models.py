from sqlalchemy import Column, Integer, String, Boolean
from .database import Base
# Define Model
class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index = True)
    title = Column(String, nullable = False)
    description = Column(String, nullable = True)
    completed = Column(Boolean, default = False)
    priority = Column(Integer, default=1)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index = True)
    username =Column(String, nullable = False)
    hash_password =Column(String, nullable = False)
    email =Column(String, unique=True, nullable = True)