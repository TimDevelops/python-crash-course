#  🍕 Pizza Builder — Challenge Steps
#
# 1. Define a Pizza class that stores:
#    - size, crust type, and a list of toppings
# 2. Add a method to add a new topping
# 3. Add a method to remove a topping if it exists
# 4. Add a method to print pizza details:
#    - size, crust, and all toppings (or “No toppings yet!”)
# 5. Create a pizza object, customize it, and print the summary

class Pizza:
    def __init__(self,size, crust_type):
        self.size = size
        self.crust_type = crust_type
        self.toppings = []

    def new_topping(self, topping):
        self.toppings.append(topping)

    def remove_topping(self,topping):
        if topping in self.toppings:
            self.toppings.remove(topping)
        else:
            print(f"{topping.title()}'s are not on the pizza!")

    def pizza_details(self):
        if len(self.toppings) == 0:
            print(f"Size: {self.size}\nCrust: {self.crust_type}\nToppings: No toppings yet!")
        else:
            print(f"Size: {self.size}\nCrust: {self.crust_type}\nToppings: {', '.join(self.toppings)}")

pizza1 = Pizza('med','stuffed')
pizza1.new_topping('pepperoni')
pizza1.new_topping('onions')
print(f"Pizza1's order")
pizza1.pizza_details()