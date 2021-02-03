from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric

# this is for multiple table and relationships
from sqlalchemy.orm import relationship

# this is the Base in database.py
from .database import Base


class Pop_Table(Base):
    __tablename__ = "pop_2010_2019"

    
    year = Column(Integer)
    city_state = Column(String) 
    population= Column(Integer)
    id = Column(Integer, primary_key=True, index=True)
