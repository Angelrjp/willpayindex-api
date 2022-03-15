from flask import Flask
from sqlalchemy import event
from sqlalchemy.engine import Engine
from src.routes import bp as users_bp
from flask_sqlalchemy import SQLAlchemy

from extensions import db


app = Flask(__name__)
app.config.from_object('config.Config') 

db.app = app
db.init_app(app)

app.register_blueprint(users_bp)

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


