from sqlalchemy import create_engine,MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import  declarative_base



engine=create_engine("postgresql://postgres:Sunrise.123@localhost:5432/metics)",
    echo=True
)

#SessionLocal= sessionmaker(autocommit=False,bind=engine)

meta= MetaData()
con=engine.connect()