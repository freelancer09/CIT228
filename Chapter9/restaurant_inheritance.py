# Try It Yourself 9-6
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type,number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")
    def set_number_served(self,served):
        self.number_served = int(served)
    def increment_number_served(self,served):
        self.number_served += served

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type,number_served, flavors):
        super().__init__(restaurant_name, cuisine_type,number_served)
        self.flavors = flavors
    def display_flavors(self):
        print(f"{self.restaurant_name} flavors available:")
        for flavor in self.flavors:
            print(flavor)

print("---------- Exercise 9-6 ----------")
restaurant1 = IceCreamStand("Moomers","Ice Cream",0,["Vanilla", "Chocolate", "Strawberry"])
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant1.display_flavors()