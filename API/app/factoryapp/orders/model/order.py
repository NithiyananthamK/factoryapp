from app.common import db, flask_bcrypt
import datetime
import logging
from sqlalchemy.dialects.postgresql import JSONB
#
class Available_Orders(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "tbl_availableorders"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(50))
    item_name = db.Column(db.String(255), nullable=True)
    item_description = db.Column(db.String(255), nullable=True)
    single_qty_price = db.Column(db.DECIMAL(10, 1), nullable=True)
    available_qty = db.Column(db.Integer, nullable=True)
    created_by = db.Column(db.Integer, nullable=True)
    updated_by = db.Column(db.Integer, nullable=True)
    created_date = db.Column(db.DateTime, nullable=True, default=datetime.datetime.utcnow())
    updated_date = db.Column(db.DateTime, nullable=True, default=datetime.datetime.utcnow())
    isActive = db.Column(db.Integer, nullable=True)

