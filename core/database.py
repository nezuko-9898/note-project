from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

db_url = 'sqlite:///note.db'

engine = create_engine( db_url, echo=True)

sessionLocal = sessionmaker(bind= engine, autoflush=False,
    autocommit=False,)


BASE = declarative_base()
