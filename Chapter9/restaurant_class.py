# Try It Yourself 9-1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

print("---------- Exercise 9-1 ----------")
restaurant = Restaurant("TGI Friday","American")
print(f"Restaurant= {restaurant.restaurant_name}")
print(f"Cuisine= {restaurant.cuisine_type}")
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Try It Yourself 9-2
print("---------- Exercise 9-2 ----------")
restaurant1 = Restaurant("Olive Garden","Italian")
restaurant2 = Restaurant("Hunan","Chinese")
restaurant3 = Restaurant("La Senorita","Mexican")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()