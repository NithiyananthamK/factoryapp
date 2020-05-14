from app.common import db, flask_bcrypt
import datetime
import logging
from sqlalchemy.dialects.postgresql import JSONB
#
class User_Orders(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "tbl_userorders"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, nullable=True)
    amount_to_pay = db.Column(db.DECIMAL(10, 1), nullable=True)
    ordered_qty = db.Column(db.Integer, nullable=True)
    delivery_address= db.Column(db.String(50))
    delivery_city = db.Column(db.String(50))
    delivery_state = db.Column(db.String(50))
    delivery_postalcode = db.Column(db.String(50))
    created_by = db.Column(db.Integer, nullable=True)
    updated_by = db.Column(db.Integer, nullable=True)
    created_date = db.Column(db.DateTime, nullable=True, default=datetime.datetime.utcnow())
    updated_date = db.Column(db.DateTime, nullable=True, default=datetime.datetime.utcnow())
    isActive = db.Column(db.Integer, nullable=True)
    order_status = db.Column(db.Integer, nullable=True)

