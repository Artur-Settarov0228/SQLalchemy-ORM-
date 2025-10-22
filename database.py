from sqlalchemy import (
    URL,
    create_engine,
    MetaData

)
from sqlalchemy.orm import sessionmaker

import config

DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    host=config.DB_HOST,
    port=config.DB_PORT,
    password=config.DB_PASSWORD,
    username=config.DB_USER,
    database=config.DB_NAME
)

engine = create_engine(DATABASE_URL)

Base = MetaData()

conn = engine.connect()

LocalSession = sessionmaker(engine)

