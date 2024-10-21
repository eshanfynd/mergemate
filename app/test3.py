from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def create_connection(db_url):
    engine = create_engine(db_url)
    Base.metadata.bind = engine
    session = sessionmaker(bind=engine)()
    return session