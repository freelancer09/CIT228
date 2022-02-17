# Try It Yourself 9-4
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

print("---------- Exercise 9-4 ----------")
restaurant = Restaurant("Outback Steakhouse","American",4)
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(f"The starting number of customers was: {restaurant.number_served}")
restaurant.number_served = 200
print(f"The number of customers served has been changed to {restaurant.number_served}")
restaurant.set_number_served(300)
print(f"The number of customers served has been changed to {restaurant.number_served}")
restaurant.increment_number_served(45)
print(f"The number of customers served has been changed to {restaurant.number_served}")