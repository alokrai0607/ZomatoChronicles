from menu_management import Dish, Menu

class Order:
    order_id_counter = 1

    def __init__(self, customer_name, dishes):
        self.order_id = Order.order_id_counter
        Order.order_id_counter += 1
        self.customer_name = customer_name
        self.dishes = dishes
        self.status = 'received'

class OrderManagement:
    def __init__(self, menu):
        self.menu = menu
        self.orders = []

  # Inside the OrderManagement class

    def take_order(self, customer_name, dish_ids):
        dishes = [self.menu.get_dish_by_id(dish_id) for dish_id in dish_ids]
        if None in dishes:
            return None

        if all(dish.available for dish in dishes):
            order = Order(customer_name, dishes)
            self.orders.append(order)
            return order
        return None

    def update_order_status(self, order_id, new_status):
        if new_status in ['preparing', 'ready for pickup', 'delivered']:
            for order in self.orders:
                if order.order_id == order_id:
                    order.status = new_status
                    return True
        return False



# Initialize order management system
order_management = OrderManagement(Order)

