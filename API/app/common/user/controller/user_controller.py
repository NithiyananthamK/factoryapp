from flask import request
from flask_restplus import Resource
import logging
from ..util.dto import UserDto
from ..service.user_service import login_user, signup_user
from app.common.util.constants import constant

api = UserDto.api
user_auth = UserDto.user_auth
signup = UserDto.signup_user

@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """
    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        return login_user(data=post_data)


@api.route('/signup_user')
class UserLogin(Resource):
    """
       Sign up a user
    """
    @api.doc('signup user')
    @api.expect(signup, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        return signup_user(data=post_data)



