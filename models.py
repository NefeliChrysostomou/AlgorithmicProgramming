tier_order = ['bronze', 'silver', 'gold', 'platinum'] # add new items in ascending order

"""
This code uses a python "trick", classes in python are basically dictionaries 
"""

class Model:
    COMPARE_ATTRIBUTE = None # set this to the name of the attribute you want to compare

    # due to the way static members work, these methods have to be implemented in the subclasses
    # to bind the class variable correctly
    def set_compare_attribute(self, attr):
        raise NotImplementedError("Subclasses must implement set_compare_attribute.")

    def get_compare_attribute(self):
        raise NotImplementedError("Subclasses must implement get_compare_attribute.")

    def get_compare_value(self):
        if self.COMPARE_ATTRIBUTE is None:
            raise ValueError("No comparison attribute set.")
        if not hasattr(self, self.COMPARE_ATTRIBUTE):
            raise AttributeError(f"Attribute '{self.COMPARE_ATTRIBUTE}' not found in object.")
        return getattr(self, self.COMPARE_ATTRIBUTE)


    def compare(self, other, attr=None):
        """
        Compare two objects based on a specified attribute.
        If no attribute is specified, use the class's COMPARE_ATTRIBUTE.
        """
        attr = attr or self.COMPARE_ATTRIBUTE # default to class attribute

        extra = False

        if attr is None:
            raise ValueError("No attribute specified for comparison.")
        if not hasattr(self, attr):
            raise AttributeError(f"Attribute '{attr}' not found in both objects.")
        if not hasattr(other, attr):
            if not isinstance(other, Model):
                extra = True
            else:
                raise AttributeError(f"Attribute '{attr}' not found in other object.")
        
        if extra:
            other_value = other
        else:
            other_value = getattr(other, attr) if not extra else other

        if attr == 'ticket_tier': # special behaviur for their ascending order
            self_value = tier_order.index(getattr(self, "ticket_tier"))
            other_value = tier_order.index(other_value)
        else:
            self_value = getattr(self, attr)

        if self_value < other_value:
            return -1
        elif self_value > other_value:
            return 1
        else:
            return 0
        
    def __lt__(self, other):
        return self.compare(other) < 0
    
    def __gt__(self, other):
        return self.compare(other) > 0
    
    def __eq__(self, other):
        return self.compare(other) == 0
        
class Ride(Model):
    COMPARE_ATTRIBUTE = "ride_id"
    def __init__(self, ride_id, name, location, duration, ticket_tier):
        self.ride_id = ride_id
        self.name = name
        self.location = location
        self.duration = duration
        self.ticket_tier = ticket_tier

    def get_ride_id(self):
        return self.ride_id

    def set_ride_id(self, ride_id):
        self.ride_id = ride_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_duration(self):
        return self.duration

    def set_duration(self, duration):
        self.duration = duration

    def get_ticket_tier(self):
        return self.ticket_tier

    def set_ticket_tier(self, ticket_tier):
        self.ticket_tier = ticket_tier

    def set_compare_attribute(self, attr):
        if hasattr(self, attr):
            Ride.COMPARE_ATTRIBUTE = attr
        else:
            raise AttributeError(f"Attribute '{attr}' not found in Ride class.")
        
    def get_compare_attribute(self):
        return Ride.COMPARE_ATTRIBUTE
    
    def __str__(self):
        return f"Ride {self.ride_id}: {self.name}, {self.location}, Duration: {self.duration}, Tier: {self.ticket_tier}"


class Customer(Model):
    COMPARE_ATTRIBUTE = "customer_id"
    def __init__(self, customer_id, name, age, gender, ticket_tier):
        self.customer_id = customer_id
        self.name = name
        self.age = age
        self.gender = gender
        self.ticket_tier = ticket_tier  # bronze, silver, gold, platinum

    def get_customer_id(self):
        return self.customer_id

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender

    def get_ticket_tier(self):
        return self.ticket_tier

    def set_ticket_tier(self, ticket_tier):
        self.ticket_tier = ticket_tier

    def set_compare_attribute(self, attr):
        if hasattr(self, attr):
            Customer.COMPARE_ATTRIBUTE = attr
        else:
            raise AttributeError(f"Attribute '{attr}' not found in Customer class.")

    def get_compare_attribute(self):
        return Customer.COMPARE_ATTRIBUTE

    def __str__(self):
        return f"Customer {self.customer_id}: {self.name}, {self.age}, {self.gender}, Tier: {self.ticket_tier}"


class Restaurant(Model):
    COMPARE_ATTRIBUTE = "restaurant_id"

    def __init__(self, restaurant_id, name, location, type_):
        self.restaurant_id = restaurant_id
        self.name = name
        self.location = location
        self.type = type_

    def get_restaurant_id(self):
        return self.restaurant_id

    def set_restaurant_id(self, restaurant_id):
        self.restaurant_id = restaurant_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_type(self):
        return self.type

    def set_type(self, type_):
        self.type = type_

    def set_compare_attribute(self, attr):
        if hasattr(self, attr):
            Restaurant.COMPARE_ATTRIBUTE = attr
        else:
            raise AttributeError(f"Attribute '{attr}' not found in Restaurant class.")

    def get_compare_attribute(self):
        return Restaurant.COMPARE_ATTRIBUTE

    def __str__(self):
        return f"Restaurant {self.restaurant_id}: {self.name}, {self.location}, Type: {self.type}"
