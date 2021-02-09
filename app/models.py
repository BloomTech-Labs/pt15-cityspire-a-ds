from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric
# this is for multiple table and relationships
from sqlalchemy.orm import relationship
# this is the Base in database.py
from .database import Base





class Pop_Table(Base):
    __tablename__ = "pop_2010_2019"
    id_num = Column(Integer, primary_key=True)
    year = Column(Integer)
    city_state = Column(String) 
    population= Column(Integer)

    def __repr__(self):
        return '{"id_num": %s, "population": %s, "city_state": "%s", "year": %s}' % (self.id_num, self.population, self.city_state, self.year)
    
