from flask import request
from flask_restplus import Resource
import logging
from ..util.dto import User_OrderDto
from ..service.user_order_service import save_userorder, get_user_orders, get_orderderdata_byid

api = User_OrderDto.api
user_orderdetails = User_OrderDto.userorderdetails

@api.route('/confirm_userorder')
class SaveOrder(Resource):
    """
        Save order
    """
    @api.doc('save orders')
    @api.expect(user_orderdetails, validate=True)
    def post(self):
        # get the post data
        try:
            data = request.json
            return save_userorder(data)
        except Exception as e:
            print(e)
            print('save_order controller error:' + str(e))


@api.route('/getuser_orders/<page>/<row>/<created_by>')
class GetUserOrders(Resource):
    """
        Get all available orders
    """
    @api.doc('get user orders')
    def get(self, page, row, created_by):
        # get the post data
        try:
            return get_user_orders(page, row, created_by)
        except Exception as e:
            print(e)
            print('get_user_orders controller error:' + str(e))



@api.route('/get_orderderdata_byid/<ordered_id>')
class GetUserOrders(Resource):
    """
        Get all available orders
    """
    @api.doc('get user order by id')
    def get(self, ordered_id):
        # get the post data
        try:
            return get_orderderdata_byid(ordered_id)
        except Exception as e:
            print(e)
            print('get_orderderdata_byid controller error:' + str(e))