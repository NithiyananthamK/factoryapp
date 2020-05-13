import uuid
from datetime import datetime
from app.cura import db
from sqlalchemy import and_, or_
from app.factoryapp.orders.model.order import Available_Orders


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


def save_changes(data):
    try:
        db.session.add(data)
        db.session.commit()
    except Exception as e:
        print(e)
        print('Handling run-time error:')