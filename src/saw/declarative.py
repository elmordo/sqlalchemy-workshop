from sqlalchemy.orm import declarative_base

RawBase = declarative_base()


class Base(RawBase):
    __abstract__ = True
