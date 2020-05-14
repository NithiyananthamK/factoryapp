from flask import request
from flask_restplus import Resource
import logging
from ..util.dto import OrderDto
from ..service.order_service import get_all_available_orders, save_order, delete_order, get_order_byid, get_alluser_orders

api = OrderDto.api
orderdetails = OrderDto.order_details

@api.route('/getall_orders/<page>/<row>')
class GetAvailableOrders(Resource):
    """
        Get all available orders
    """
    @api.doc('get all orders')
    def get(self, page, row):
        # get the post data
        try:
            return get_all_available_orders(page, row)
        except Exception as e:
            print(e)
            print('get_all_available_orders controller error:' + str(e))


@api.route('/save_order')
class SaveOrder(Resource):
    """
        Save order
    """
    @api.doc('save orders')
    @api.expect(orderdetails, validate=True)
    def post(self):
        # get the post data
        try:
            data = request.json
            return save_order(data)
        except Exception as e:
            print(e)
            print('save_order controller error:' + str(e))


@api.route('/delete_order/<order_id>')
class DeleteOrder(Resource):
    @api.doc('Delete order from list')
    def get(self, order_id):
        try:
            """Delete order from list"""
            return delete_order(order_id)
        except Exception as e:
            print("delete order controller error: "+str(e))
            return ""

@api.route('/get_order_byid/<order_id>')
class AvailableOrders(Resource):
    """
        Get order by id
    """
    @api.doc('get order by id')
    def get(self, order_id):
        # get the post data
        try:
            return get_order_byid(order_id)
        except Exception as e:
            print(e)
            print('get_order_byid controller error:' + str(e))


@api.route('/get_alluser_orders/<page>/<row>')
class GetAlluserOrders(Resource):
    """
        Get all available orders
    """
    @api.doc('get all users orders')
    def get(self, page, row):
        # get the post data
        try:
            return get_alluser_orders(page, row)
        except Exception as e:
            print(e)
            print('get_alluser_orders controller error:' + str(e))