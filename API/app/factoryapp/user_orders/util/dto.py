from flask_restplus import Namespace, fields


class User_OrderDto:
    api = Namespace('User order', description='user order related operations')

    userorderdetails = api.model('user order details', {
        "id":fields.Integer(required=True, description='id'),
        'order_id': fields.Integer(required=True, description='Order id'),
        'order_qty': fields.String(required=True, description='Item type'),
        'item_price': fields.Float(required=True, description='Item price'),
        'del_address': fields.String(required=True, description='Delivery address'),
        'del_city': fields.String(required=True, description='Delivery city'),
        'del_state': fields.String(required=True, description='Delivery state'),
        'del_zipcode': fields.String(required=True, description='Delivery zipcode'),
    })

