'''from sqlalchemy import create_engine, MetaData, Table

engine = create_engine('postgresql+psycopg2://user:user@localhost:5432/test')
meta = MetaData(bind=engine)
items = Table('items', meta, autoload = True, autoload_with = engine)'''

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Items(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key = True)
    name = Column(String(30), nullable = False)
    quantity = Column(Integer, nullable = False)

engine = create_engine('postgresql+psycopg2://user:user@localhost:5432/test')

#create table
#Base.metadata.create_all(engine)
Base.metadata.bind = engine

def add(item : Items):
    DBSession = sessionmaker(bind = engine)
    session = DBSession()
    session.add(item)
    session.commit()
