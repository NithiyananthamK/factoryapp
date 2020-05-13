from flask_restplus import Api
from flask import Blueprint

from .cura.user.controller.user_controller import api as user_ns
from .factoryapp.orders.controller.order_controller import api as orders_ns
from .factoryapp.user_orders.controller.userorder_controller import api as userorders_ns


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='CURA API WITH JWT',
          version='1.0',
          description='A CURA rest web service'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(orders_ns, path='/orders')
api.add_namespace(userorders_ns, path='/user_orders')











