# Q2.py
# This program safely uses a mutable parameter

def add_order(order_id, orders=None):
    """
    Stores order IDs across function calls safely
    """
    if orders is None:
        orders = []  # new list created each time

    orders.append(order_id)
    return orders


# Sample calls
print(add_order(101))
print(add_order(102))
print(add_order(103))
