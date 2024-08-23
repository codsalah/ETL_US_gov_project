import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, Float

db_folder = 'final_data_in_sqlite'
db_file = 'database.db'
db_path = os.path.join(db_folder, db_file)
os.makedirs(db_folder, exist_ok=True)

db_url = f"sqlite:///{db_path}"

engine = create_engine(db_url)

Base = declarative_base()

class UsaGov(Base):
    __tablename__ = 'usa_gov_data'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    web_browser = Column(String)
    operating_sys = Column(String)
    from_url = Column(String) 
    to_url = Column(String)               
    city = Column(String)                 
    latitude = Column(Float)              
    longitude = Column(Float)            
    time_zone = Column(String)            
    time_in = Column(String)              
    time_out = Column(String)             

     
Base.metadata.create_all(engine)





