from saw.application import Application
import saw.model
from saw.database import make_engine, prepare_database
from saw.resources import bp
from sqlalchemy.orm import sessionmaker


def main():
    engine = make_engine()
    prepare_database(engine)
    app = Application(__name__)
    app.register_blueprint(bp)
    app.session_maker = sessionmaker(bind=engine)
    app.run("127.0.0.1", 5000, debug=True)


if __name__ == "__main__":
    main()
