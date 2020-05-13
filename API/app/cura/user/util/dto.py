from flask_restplus import Namespace, fields

address = {
        "address1": "string",
        "address2": "string",
        "city": "string",
        "state": "string",
        "zip": "string",
        "country": "string",
        "phonenumber": "string"
    }
contacts = {
        "Phonenumber": "string",
       }

rolepermission = {

    "menuid":"string"
}

class UserDto:
    api = Namespace('user', description='user related operations')

    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })

    signup_user = api.model('auth_details', {
        'name': fields.String(required=True, description='user name'),
        'email': fields.String(required=True, description='user email'),
        'password': fields.String(required=True, description='user password'),
        'role': fields.String(required=True, description='User role'),
    })
