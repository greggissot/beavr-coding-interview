from sqlalchemy import Column, Integer, String

from .database import Base

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    summary = Column(String)
    key_elements = Column(String)
    
    class Config:
        orm_mode = True