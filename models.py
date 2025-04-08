class Customer:
    def __init__(self, customer_id, name, age, gender, ticket_tier):
        self.customer_id = customer_id
        self.name = name
        self.age = age
        self.gender = gender
        self.ticket_tier = ticket_tier  # bronze, silver, gold, platinum

    def get_customer_id(self):
        return self.customer_id

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_ticket_tier(self):
        return self.ticket_tier

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_gender(self, gender):
        self.gender = gender

    def set_ticket_tier(self, ticket_tier):
        self.ticket_tier = ticket_tier

    def __lt__(self, other):
        """Comparison based on ticket tier hierarchy"""
        tiers = {'bronze': 1, 'silver': 2, 'gold': 3, 'platinum': 4}
        return tiers.get(self.ticket_tier.lower(), 0) < tiers.get(other.ticket_tier.lower(), 0)

    def __eq__(self, other):
        if isinstance(other, Customer):
            return self.customer_id == other.customer_id
        return False

    def __str__(self):
        return f"Customer {self.customer_id}: {self.name}, {self.age}, {self.gender}, Tier: {self.ticket_tier}"


class Restaurant:
    def __init__(self, restaurant_id, name, location, type_):
        self.restaurant_id = restaurant_id
        self.name = name
        self.location = location
        self.type = type_

    def get_restaurant_id(self):
        return self.restaurant_id

    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    def get_type(self):
        return self.type

    def set_name(self, name):
        self.name = name

    def set_location(self, location):
        self.location = location

    def set_type(self, type_):
        self.type = type_

    def __lt__(self, other):
        """Comparison based on name (alphabetical)"""
        return self.name.lower() < other.name.lower()

    def __eq__(self, other):
        if isinstance(other, Restaurant):
            return self.restaurant_id == other.restaurant_id
        return False

    def __str__(self):
        return f"Restaurant {self.restaurant_id}: {self.name}, {self.location}, Type: {self.type}"
