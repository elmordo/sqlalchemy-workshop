from typing import Callable

from flask import Flask
from sqlalchemy.orm import Session


class Application(Flask):

    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)
        self.session_maker: Callable[[], Session] = None
