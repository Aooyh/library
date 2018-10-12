from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
CSRFProtect(app)


class MyConfig(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:5998381@localhost:3306/library'
    SQLALCHEMY_TRACK_MODIFICATION = True

app.config.from_object(MyConfig)
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer,primary_key=True)

from library_case.models import *


from library_case.feature import features

app.register_blueprint(features)



if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    app.run(debug=True)
