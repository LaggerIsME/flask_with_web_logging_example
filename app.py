from flask import Flask, g
#from flask_sqlalchemy import SQLAlchemy
from flask_mongoengine import MongoEngine
from flask_track_usage import TrackUsage
#from flask_track_usage.storage.sql import SQLStorage
from flask_track_usage.storage.mongo import MongoEngineStorage

app = Flask(__name__)


# PostgreSQL настройка
# Пример: dialect+driver://username:password@host:port/database

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345678@localhost:5432/database_name'
#sql_db = SQLAlchemy(app)

# MongoDB настройка
app.config['MONGODB_SETTINGS'] = {
    'db': 'example_website',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


with app.app_context():
    # TrackUsage
    #pstore = SQLStorage(db=sql_db)
    mstore = MongoEngineStorage()
    t = TrackUsage(app, mstore)


@app.route('/')
def index():
    # если хочешь отправить что-то еще
    g.track_var["optional"] = "something"
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)