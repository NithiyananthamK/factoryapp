from flask_restplus import Namespace, fields


class OrderDto:
    api = Namespace('Order', description='Order related operations')

    order_details = api.model('order save details', {
        'id': fields.Integer(required=True, description='Order id'),
        'item_type': fields.String(required=True, description='Item type'),
        'item_name': fields.String(required=True, description='Item name'),
        'item_desc': fields.String(required=True, description='Item description'),
        'item_price': fields.String(required=True, description='Item price'),
        'stock_qty': fields.String(required=True, description='Item qty'),
        'created_by': fields.Integer(required=True, description='Order created by'),
    })

    updatestatus = api.model('Update order status', {
        'id': fields.Integer(required=True, description='id'),
        'status': fields.String(required=True, description='Order status'),
    })