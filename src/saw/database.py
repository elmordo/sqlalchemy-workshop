from os.path import isfile, join, dirname

from saw.declarative import Base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.engine import Engine

DB_FILE = "db.sqlite"
FULL_PATH = join(dirname(__file__), DB_FILE)
FILE_EXISTS_ON_STARTUP = isfile(FULL_PATH)


def make_engine():
    engine = create_engine(f"sqlite:///{DB_FILE}")
    if Base.metadata is None:
        Base.metadata = MetaData()
    if Base.metadata.bind is None:
        Base.metadata.bind = engine
    return engine


def prepare_database(engine: Engine):
    if not FILE_EXISTS_ON_STARTUP or True:
        Base.metadata.create_all()
