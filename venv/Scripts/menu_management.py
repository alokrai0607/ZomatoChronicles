class Dish:
    def __init__(self, dish_id, name, price, available):
        self.dish_id = dish_id
        self.name = name
        self.price = price
        self.available = available

class Menu:
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

        # Inside the Menu class

    def get_dish_by_id(self, dish_id):
        for dish in self.dishes:
            if dish.dish_id == dish_id:
                return dish
        return None


    def remove_dish(self, dish_id):
        self.dishes = [dish for dish in self.dishes if dish.dish_id != dish_id]

    def update_availability(self, dish_id, available):
        for dish in self.dishes:
            if dish.dish_id == dish_id:
                dish.available = available

# Initialize the menu
menu = Menu()
