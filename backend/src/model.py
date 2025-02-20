from sqlalchemy import Column, Integer, String

from .database import Base

class Document(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
    class Config:
        orm_mode = True