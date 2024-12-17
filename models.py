from sqlalchemy import Column, Integer, Text, String
from .database import Base

class Post(Base):
    _tablename_ = "posts"

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String(255), nullable = False, index = True)
    content = Column(Text, nullable = False, index = True)