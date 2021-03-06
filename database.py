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

connect_str = 'postgresql+psycopg2://user:user@localhost:5432/test'
engine = create_engine(connect_str)
DBSession = sessionmaker(bind = engine)
#create table
#Base.metadata.create_all(engine)
Base.metadata.bind = engine

def add(item : Items):
    session = DBSession()
    session.add(item)
    session.commit()
    session.close()

def get_all():
    session = DBSession()
    result = session.query(Items).all()
    session.close()
    return result

def get(id):
    session = DBSession()
    result = session.query(Items).filter(Items.id == id).first()
    session.close()
    return result

def delete(id):
    session = DBSession()
    session.query(Items).filter(Items.id == id).delete()
    #session.delete(get(id))
    session.commit()
    session.close()

def update(id, name, quantity):
    session = DBSession()
    items = session.query(Items).filter(Items.id == id)
    if name != None:
        items.update({'name':name})
    if quantity != None:
        items.update({'quantity':quantity})
    session.commit()
    session.close()
