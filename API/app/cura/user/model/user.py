from app.cura import db, flask_bcrypt
import datetime
import logging
#
class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "tbluser"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(255), nullable=False)
    password=db.Column(db.String(200))
    role = db.Column(db.String(200), nullable=True)
    created_by = db.Column(db.Integer, nullable=True)
    updated_by = db.Column(db.Integer, nullable=True)
    created_date = db.Column(db.DateTime, nullable=True, default=datetime.datetime.utcnow())
    updated_date = db.Column(db.DateTime, nullable=True, default=datetime.datetime.utcnow())
    isActive = db.Column(db.Integer, nullable=True)

