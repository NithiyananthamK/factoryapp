import uuid
from datetime import datetime, time
from decimal import Decimal
from sqlalchemy import update
from app.common import db
from app.factoryapp.user_orders.model.user_order import User_Orders
from app.factoryapp.orders.model.order import Available_Orders


def save_userorder(data):
    try:
        avlble_order = Available_Orders.query.filter(Available_Orders.id == data['order_id'], Available_Orders.isActive == 1).first()
        if avlble_order:
            user_order = User_Orders.query.filter(User_Orders.id == data['id'], User_Orders.isActive == 1).first()
            if not user_order:
                remaining_qty = avlble_order.available_qty - int(data['order_qty'])
                total_amt_topay = avlble_order.single_qty_price * int(data['order_qty'])
                new_userorder = User_Orders(
                    order_id=data['order_id'],
                    amount_to_pay=total_amt_topay,
                    ordered_qty=data['order_qty'],
                    delivery_address=data['del_address'],
                    delivery_city=data['del_city'],
                    delivery_state=data['del_state'],
                    delivery_postalcode=data['del_zipcode'],
                    created_by=data['created_by'],
                    created_date=datetime.utcnow(),
                    isActive=1
                )
                resp = update_qty(remaining_qty, data['order_id'])

                save_changes(new_userorder)
                res = {
                    "Errorcode": 9999,
                    "status": "success",
                    "order_id": new_userorder.id,
                    "message": "Ordered successfully"
                }
            else:
                remaining_qty = (avlble_order.available_qty + user_order.ordered_qty) - int(data['order_qty'])
                total_amt_topay = avlble_order.single_qty_price * int(data['order_qty'])
                user_order.ordered_qty = data['order_qty']
                user_order.delivery_address = data['del_address']
                user_order.delivery_city =data['del_city']
                user_order.delivery_state = data['del_state']
                user_order.delivery_postalcode = data['del_zipcode']
                user_order.updated_by = data['created_by'],
                user_order.updated_date = datetime.utcnow()
                user_order.amount_to_pay = total_amt_topay,

                resp = update_qty(remaining_qty, data['order_id'])
                save_changes(user_order)
                res = {
                    "Errorcode": 9999,
                    "status": "success",
                    "order_id": user_order.id,
                    "message": "Ordered successfully"
                }

        return res
    except Exception as e:
        print(e)


def update_qty(update_qty, order_id):
    try:
        stmt = update(Available_Orders).where(Available_Orders.id == order_id).values(available_qty=update_qty, updated_date=datetime.utcnow())
        update_changes(stmt)

        response = {
            "Errorcode":9999
        }
        return response
    except Exception as e:
        print(e)
        print('Handling run-time error:')


def get_user_orders(page, row, created_by):
    try:
        orders_list = []
        # Get all orders
        Orderslist = User_Orders.query.join(Available_Orders, User_Orders.order_id == Available_Orders.id). \
            add_columns(User_Orders.id, User_Orders.order_id, Available_Orders.type, User_Orders.amount_to_pay,
                        User_Orders.ordered_qty, Available_Orders.item_name, User_Orders.delivery_address,
                        User_Orders.delivery_city, User_Orders.delivery_state, User_Orders.delivery_postalcode, Available_Orders.single_qty_price, Available_Orders.available_qty).\
        filter(User_Orders.isActive == 1, User_Orders.created_by == created_by). \
        filter(Available_Orders.isActive == 1).paginate(int(page), int(row), False).items

        # Get orders count
        Orderslist_count = User_Orders.query.filter(User_Orders.isActive == 1, User_Orders.created_by == created_by).count()

        if Orderslist:
            for order in Orderslist:
                item={}
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

                orders_list.append(item)
        res = {
            "data": orders_list,
            "total_count": Orderslist_count
        }
        return res

    except Exception as e:
        print(e)
        print('Handling run-time error:')


def get_orderderdata_byid(id):
    try:
        ordered_detail = User_Orders.query.join(Available_Orders, User_Orders.order_id == Available_Orders.id). \
            add_columns(User_Orders.id, User_Orders.order_id, Available_Orders.type, User_Orders.amount_to_pay,
                        User_Orders.ordered_qty, Available_Orders.item_name, User_Orders.delivery_address,
                        User_Orders.delivery_city, User_Orders.delivery_state, User_Orders.delivery_postalcode). \
        filter(User_Orders.isActive == 1, User_Orders.id == id,
               Available_Orders.isActive == 1).first()
        if ordered_detail:
            item = {}
            item['id'] = ordered_detail[1]
            item['order_id'] = ordered_detail[2]
            item['type'] = ordered_detail[3]
            item['amount_to_pay'] = str(ordered_detail[4])
            item['ordered_qty'] = ordered_detail[5]
            item['item_name'] = ordered_detail[6]
            item['delivery_address'] = ordered_detail[7]
            item['delivery_city'] = ordered_detail[8]
            item['delivery_state'] = ordered_detail[9]
            item['delivery_postalcode'] = ordered_detail[10]
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

def update_changes(stmt):
    try:
       db.session.execute(stmt)
       db.session.commit()
    except Exception as e:
       print(e)
       print('Handling run-time error:')