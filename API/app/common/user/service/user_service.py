import uuid
from datetime import datetime
from app.common import db
from app.common.user.model.user import User
import logging

def login_user(data):
    try:
        user = User.query.filter(User.email == data["email"], User.password == data["password"],
                    User.isActive == 1).first()
        if user:
            res = {
                "Errorcode":9999,
                "status":"success",
                "user_id": user.id,
                "user_role": user.role
            }
        else:
            res = {
                "Errorcode": 9998,
                "status": "failure",
                "user_id": 0
            }
        return res
    except Exception as e:
        print(e)

def signup_user(data):
    try:
        user = User.query.filter(User.email == data["email"], User.isActive == 1).first()
        if user:
            res = {
                "Errorcode":9998,
                "status":"failure",
                "user_id": user.id,
                "message":"User already exists"
            }
        else:
            new_user = User(
                name = data['name'],
                email=data['email'],
                password=data['password'],
                role=data['role'],
                created_by=1,
                created_date=datetime.utcnow(),
                isActive=1
            )
            save_changes(new_user)
            res = {
                "Errorcode":9999,
                "status": "success",
                "user_id": new_user.id,
                "message": "User successfully added"
            }
        return res
    except Exception as e:
        print(e)



def save_changes(data):
    try:
        db.session.add(data)
        db.session.commit()
    except Exception as e:
        print(e)
        print('Handling run-time error:')