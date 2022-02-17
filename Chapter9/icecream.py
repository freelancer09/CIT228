from restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type,number_served, flavors):
        super().__init__(restaurant_name, cuisine_type,number_served)
        self.flavors = flavors
    def display_flavors(self):
        print(f"{self.restaurant_name} flavors available:")
        for flavor in self.flavors:
            print(flavor)