from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from flask_track_usage import TrackUsage
from flask_track_usage.storage.sql import SQLStorage

app = Flask(__name__)


# PostgreSQL настройка
# Пример: dialect+driver://username:password@host:port/database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345678@localhost:5432/database_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
sql_db = SQLAlchemy(app)


with app.app_context():
    # TrackUsage
    pstore = SQLStorage(db=sql_db)
    t = TrackUsage(app, pstore)


@app.route('/')
def index():
    # если хочешь отправить что-то еще
    g.track_var["optional"] = "something"
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)