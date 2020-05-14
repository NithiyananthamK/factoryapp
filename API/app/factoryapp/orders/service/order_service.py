import uuid
from datetime import datetime
from app.common import db
from sqlalchemy import and_, or_
from app.factoryapp.orders.model.order import Available_Orders
from app.factoryapp.user_orders.model.user_order import User_Orders
from app.common.user.model.user import User

def get_all_available_orders(page, row):
    try:
        orders_list = []
        # Get all Available orders
        avlbe_orders = Available_Orders.query.filter(Available_Orders.isActive == 1).paginate(int(page), int(row), False).items

        # Get Available orders count
        avlbe_orders_count = Available_Orders.query.filter(Available_Orders.isActive == 1).count()

        if avlbe_orders:
            for avl_order in avlbe_orders:
                item={}
                item['order_id'] = avl_order.id
                item['type'] = avl_order.type
                item['available_qty'] = avl_order.available_qty
                item['single_qty_price'] = str(avl_order.single_qty_price)
                item['item_name'] = avl_order.item_name
                item['item_description'] = avl_order.item_description
                orders_list.append(item)
        res = {
            "data": orders_list,
            "total_count": avlbe_orders_count
        }
        return res

    except Exception as e:
        print(e)
        print('Handling run-time error:')


def save_order(data):
    try:
        if data['id'] == 0:
            avlble_order = Available_Orders.query.filter(Available_Orders.item_name == data['item_name'], Available_Orders.isActive == 1).first()
            if avlble_order:
                res = {
                    "Errorcode":9998,
                    "status":"failure",
                    "user_id": avlble_order.id,
                    "message":"Order already exists please use different name"
                }
            else:
                new_order = Available_Orders(
                    type=data['item_type'],
                    item_name=data['item_name'],
                    item_description=data['item_desc'],
                    available_qty=data['stock_qty'],
                    single_qty_price=data['item_price'],
                    created_date=datetime.utcnow(),
                    created_by = data['created_by'],
                    isActive=1
                )
                save_changes(new_order)
                res = {
                    "Errorcode":9999,
                    "status": "success",
                    "user_id": new_order.id,
                    "message": "Order successfully added"
                }
        else:
            avlble_order = Available_Orders.query.filter(Available_Orders.id == data['id'], Available_Orders.isActive == 1).first()
            if avlble_order:
                avlble_order.available_qty = data['stock_qty']
                avlble_order.single_qty_price = data['item_price']
                avlble_order.item_description = data['item_desc']
                avlble_order.updated_by = data['created_by']
                avlble_order.updated_date = datetime.utcnow()
                save_changes(avlble_order)
                res = {
                    "Errorcode": 9999,
                    "status": "success",
                    "user_id": avlble_order.id,
                    "message": "Order successfully updated"
                }
        return res
    except Exception as e:
        print(e)


def delete_order(order_id):
    try:
        avl_order = Available_Orders.query.filter(Available_Orders.id == order_id).first()
        if avl_order:
            avl_order.isActive = 0
            save_changes(avl_order)
            response_object = {
                "Errorcode": 9999,
                "status": "Success",
                "message": "Order deleted successfully"
            }
        else:
            response_object = {
                "Errorcode": 9998,
                "status": "Invalid order id",
                "message": "Order id does not exists"
            }
        return response_object
    except Exception as e:
        print(e)
        print('Order delete function error :'+str(e))


def get_order_byid(order_id):
    try:
        avl_order = Available_Orders.query.filter(Available_Orders.id == order_id, Available_Orders.isActive == 1).first()
        if avl_order:
            item = {}
            item['order_id'] = avl_order.id
            item['type'] = avl_order.type
            item['available_qty'] = avl_order.available_qty
            item['single_qty_price'] = str(avl_order.single_qty_price)
            item['item_name'] = avl_order.item_name
            item['item_description'] = avl_order.item_description
            return item
        else:
            res = {
                "Errorcode": 9998,
                "message": "Order id not exists"
            }
            return res
    except Exception as e:
        print(e)
        print('get_order_byid function error :'+str(e))


def get_alluser_orders(page, row):
    try:
        orders_list = []
        # Get all orders
        Orderslist = User_Orders.query.join(Available_Orders, User_Orders.order_id == Available_Orders.id). \
            join(User, User_Orders.created_by == User.id).add_columns(User_Orders.id, User_Orders.order_id, Available_Orders.type, User_Orders.amount_to_pay,
                        User_Orders.ordered_qty, Available_Orders.item_name, User_Orders.delivery_address,
                        User_Orders.delivery_city, User_Orders.delivery_state, User_Orders.delivery_postalcode,
                        Available_Orders.single_qty_price, Available_Orders.available_qty, User.name, User_Orders.order_status). \
            filter(User_Orders.isActive == 1). \
            filter(Available_Orders.isActive == 1).paginate(int(page), int(row), False).items

        # Get orders count
        Orderslist_count = User_Orders.query.filter(User_Orders.isActive == 1).count()

        if Orderslist:
            for order in Orderslist:
                item = {}
                item['id'] = order[1]
                item['order_id'] = order[2]
                item['type'] = order[3]
                item['amount_to_pay'] = str(order[4])
                item['ordered_qty'] = order[5]
                item['item_name'] = order[6]
                item['delivery_address'] = order[7]
                item['delivery_city'] = order[8]
                item['delivery_state'] = order[9]
                item['delivery_postalcode'] = order[10]
                item['item_price'] = str(order[11])
                item['available_qty'] = order[12]
                item['ordered_user_name'] = order[13]
                item['order_status'] = order[14]

                orders_list.append(item)
        res = {
            "data": orders_list,
            "total_count": Orderslist_count
        }
        return res

    except Exception as e:
        print(e)
        print('Handling run-time error:')


def update_order_status(data):
    try:
        exists_order = User_Orders.query.filter(User_Orders.id == data['id'], User_Orders.isActive == 1).first()
        if exists_order:
            exists_order.order_status = int(data['status'])
            save_changes(exists_order)
            res = {
                "Errorcode":9999,
                "message": "Order status updated successfully"
            }
            return  res
    except Exception as e:
        print(e)
        print('Handling run-time error:')
        res = {
            "Errorcode": 9997,
            "message": "Order status update failed"
        }
        return res


def save_changes(data):
    try:
        db.session.add(data)
        db.session.commit()
    except Exception as e:
        print(e)
        print('Handling run-time error:')