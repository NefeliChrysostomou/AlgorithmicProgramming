class Customer:
    def __init__(self, customer_id, name, age, gender, rides_taken=None):
        self.customer_id = customer_id
        self.name = name
        self.age = age
        self.gender = gender
        self.rides_taken = rides_taken if rides_taken else []
    
    def get_customer_id(self):
        return self.customer_id
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_gender(self):
        return self.gender
    
    def get_rides_taken(self):
        return self.rides_taken
    
    def set_name(self, name):
        self.name = name
    
    def set_age(self, age):
        self.age = age
    
    def set_gender(self, gender):
        self.gender = gender
        
        
    def add_ride(self, ride_id):
        self.rides_taken.append(ride_id)
    
    def get_ride_count(self):
        return len(self.rides_taken)
    
    
    def __lt__(self, other):
        """Less than comparison based on ride count"""
        return self.get_ride_count() < other.get_ride_count()
    
    def __eq__(self, other):
        """Equal comparison based on customer_id"""
        if isinstance(other, Customer):
            return self.customer_id == other.customer_id
        return False
    
    def __str__(self):
        return f"Customer {self.customer_id}: {self.name}, {self.age}, {self.gender}, Rides: {len(self.rides_taken)}"
    

class Restaurant:
    def __init__(self, restaurant_id, name, location, menu_items=None, prices=None):
        self.restaurant_id = restaurant_id
        self.name = name
        self.location = location  # ex. "North Wing"
        self.menu_items = menu_items if menu_items else []
        self.prices = prices if prices else []
    
    def get_restaurant_id(self):
        return self.restaurant_id
    
    def get_name(self):
        return self.name
    
    def get_location(self):
        return self.location
    
    def get_menu_items(self):
        return self.menu_items
    
    def get_prices(self):
        return self.prices
    
    def set_name(self, name):
        self.name = name
    
    def set_location(self, location):
        self.location = location
    

    def add_menu_item(self, item, price):
        self.menu_items.append(item)
        self.prices.append(price)
    
    def get_average_price(self):
        if not self.prices:
            return 0
        return sum(self.prices) / len(self.prices)
    

    def __lt__(self, other):
        """Less than comparison based on average price"""
        return self.get_average_price() < other.get_average_price()
    
    def __eq__(self, other):
        """Equal comparison based on restaurant_id"""
        if isinstance(other, Restaurant):
            return self.restaurant_id == other.restaurant_id
        return False
    
    def __str__(self):
        return f"Restaurant {self.restaurant_id}: {self.name}, {self.location}, Avg Price: ${self.get_average_price():.2f}"