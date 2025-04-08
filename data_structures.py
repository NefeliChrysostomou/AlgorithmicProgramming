class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def add(self, item):
        """Add an item to the end of the linked list"""
        new_node = Node(item)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.count += 1

    def get_by_attribute(self, attribute_name, value):
        """Get an item by a specific attribute value"""
        current = self.head
        while current:
            if hasattr(current.data, attribute_name) and getattr(current.data, attribute_name) == value:
                return current.data
            current = current.next
        return None

    def remove_by_attribute(self, attribute_name, value):
        """Remove an item by a specific attribute value"""
        if not self.head:
            return False

        # Check head node
        if hasattr(self.head.data, attribute_name) and getattr(self.head.data, attribute_name) == value:
            self.head = self.head.next
            self.count -= 1
            return True

        # Search for the item to delete
        current = self.head
        while current.next:
            if hasattr(current.next.data, attribute_name) and getattr(current.next.data, attribute_name) == value:
                current.next = current.next.next
                self.count -= 1
                return True
            current = current.next

        return False

    def get_all(self):
        """Return a list of all items"""
        items = []
        current = self.head
        while current:
            items.append(current.data)
            current = current.next
        return items

    def size(self):
        """Return the number of items in the list"""
        return self.count
    


# --- Customer Linked List ---
class CustomerLinkedList(LinkedList):
    def __init__(self):
        self.head = None
        self.count = 0
        
    def add_customer(self, customer):
        return self.add(customer)

    def get_customer(self, customer_id):
        return self.get_by_attribute("customer_id", customer_id)

    def remove_customer(self, customer_id):
        return self.remove_by_attribute("customer_id", customer_id)

    def get_all_customers(self):
        return self.get_all()
    
    def sort_by_name(self):
        """Sort all items in the linked list by name"""
        items = self.get_all()
        items.sort(key=lambda item: item.name.lower())
        self.head = None
        self.count = 0
        for item in items:
            self.add(item)
        return self.get_all()


# --- Restaurant Linked List ---
class RestaurantLinkedList(LinkedList):
    def __init__(self):
        self.head = None
        self.count = 0

    def add_restaurant(self, restaurant):
        return self.add(restaurant)

    def get_restaurant(self, restaurant_id):
        return self.get_by_attribute("restaurant_id", restaurant_id)

    def remove_restaurant(self, restaurant_id):
        return self.remove_by_attribute("restaurant_id", restaurant_id)

    def get_all_restaurants(self):
        return self.get_all()

    def sort_by_name(self):
        """Sort all items in the linked list by name"""
        items = self.get_all() 
        items.sort(key=lambda item: item.name.lower())
        self.head = None
        self.count = 0
        for item in items:
            self.add(item)
        return self.get_all()



# --- Customer Array ---
class CustomerArray:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def get_customer(self, index):
        if 0 <= index < len(self.customers):
            return self.customers[index]
        return None

    def remove_customer(self, customer_id):
        for i, customer in enumerate(self.customers):
            if customer.customer_id == customer_id:
                del self.customers[i]
                return True
        return False

    def size(self):
        return len(self.customers)

    def sort_by_ticket_tier(self):
        """Sort customers by ticket tier (since rides_taken no longer exists)"""
        self.customers.sort(key=lambda c: c.ticket_tier)
        return self.customers

    def sort_by_name(self):
        """Sort customers by name"""
        self.customers.sort(key=lambda c: c.name.lower())  
        return self.customers


# --- Restaurant Array ---
class RestaurantArray:
    def __init__(self, initial_capacity=10):
        self.restaurants = [None] * initial_capacity
        self.size = 0
        self.capacity = initial_capacity

    def add_restaurant(self, restaurant):
        if self.size >= self.capacity:
            self._resize(self.capacity * 2)

        self.restaurants[self.size] = restaurant
        self.size += 1

    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.restaurants[i]

        self.restaurants = new_array
        self.capacity = new_capacity

    def get_restaurant(self, index):
        if 0 <= index < self.size:
            return self.restaurants[index]
        return None

    def remove_restaurant(self, restaurant_id):
        for i in range(self.size):
            if self.restaurants[i] and self.restaurants[i].restaurant_id == restaurant_id:
                # Shift elements
                for j in range(i, self.size - 1):
                    self.restaurants[j] = self.restaurants[j + 1]

                self.restaurants[self.size - 1] = None
                self.size -= 1

                # Resize if too empty
                if self.size < self.capacity // 4 and self.capacity > 10:
                    self._resize(self.capacity // 2)

                return True
        return False

    def get_all_restaurants(self):
        return [self.restaurants[i] for i in range(self.size) if self.restaurants[i]]

    def get_size(self):
        return self.size
