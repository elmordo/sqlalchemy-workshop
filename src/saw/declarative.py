from typing import Any, Dict

from sqlalchemy.orm import declarative_base

RawBase = declarative_base()


class Base(RawBase):
    __abstract__ = True
    __fillable__ = []

    def fill_data(self, data: Dict[str, Any]):
        for k, v in data.items():
            if k in self.__fillable__:
                setattr(self, k, v)
