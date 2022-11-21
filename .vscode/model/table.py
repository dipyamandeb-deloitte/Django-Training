from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from database import meta

users = Table(
    'users', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('email', String(200), unique=True)

)

metrics = Table(
    'metrics', meta,
    Column('id', Integer, primary_key=True),
    Column('title', String(50)),
    Column('description',String(200))

)