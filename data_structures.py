class CustomerNode:
    def __init__(self, customer):
        self.customer = customer
        self.next = None

class CustomerLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def add_customer(self, customer):
        """Add a customer to the end of the linked list"""
        new_node = CustomerNode(customer)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def get_customer(self, customer_id):
        """Get a customer by ID"""
        current = self.head
        while current:
            if current.customer.customer_id == customer_id:
                return current.customer
            current = current.next
        return None
    
    def remove_customer(self, customer_id):
        """Remove a customer by ID"""
        if not self.head:
            return False
        
        # If head node has the customer we want to be deleted
        if self.head.customer.customer_id == customer_id:
            self.head = self.head.next
            self.size -= 1
            return True
        
        # Search for the customer we want to be deleted
        current = self.head
        while current.next and current.next.customer.customer_id != customer_id:
            current = current.next
        
        # If the customer was found
        if current.next:
            current.next = current.next.next
            self.size -= 1
            return True
        
        return False
    
    def get_all_customers(self):
        """Return a list of all customers"""
        customers = []
        current = self.head
        while current:
            customers.append(current.customer)
            current = current.next
        return customers
    
    def size(self):
        """Return the number of customers in the list"""
        return self.size
    
class CustomerArray:
    def __init__(self):
        self.customers = []
    
    def add_customer(self, customer):
        """Add a customer to the array"""
        self.customers.append(customer)
    
    def get_customer(self, index):
        """Get a customer by index"""
        if 0 <= index < len(self.customers):
            return self.customers[index]
        return None
    
    def remove_customer(self, customer_id):
        """Remove a customer by ID"""
        for i, customer in enumerate(self.customers):
            if customer.customer_id == customer_id:
                del self.customers[i]
                return True
        return False
    
    def size(self):
        """Return the number of customers"""
        return len(self.customers)
    
    def sort_by_rides(self):
        """Sort customers by ride count for binary search"""
        self.customers.sort(key=lambda x: x.get_ride_count())
        return self.customers



class RestaurantArray:
    def __init__(self, initial_capacity=10):
        self.restaurants = [None] * initial_capacity
        self.size = 0
        self.capacity = initial_capacity
    
    def add_restaurant(self, restaurant):
        """Add a restaurant to the dynamic array"""
        if self.size >= self.capacity:
            self._resize(self.capacity * 2)
        
        self.restaurants[self.size] = restaurant
        self.size += 1
    
    def _resize(self, new_capacity):
        """Resize the internal array to a new capacity"""
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.restaurants[i]
        
        self.restaurants = new_array
        self.capacity = new_capacity
    
    def get_restaurant(self, index):
        """Get a restaurant by index"""
        if 0 <= index < self.size:
            return self.restaurants[index]
        return None
    
    def remove_restaurant(self, restaurant_id):
        """Remove a restaurant by ID"""
        for i in range(self.size):
            if self.restaurants[i] and self.restaurants[i].restaurant_id == restaurant_id:
                # Shift elements to fill the gap
                for j in range(i, self.size - 1):
                    self.restaurants[j] = self.restaurants[j + 1]
                
                self.restaurants[self.size - 1] = None
                self.size -= 1
                
                # Resize if array is too empty
                if self.size < self.capacity // 4 and self.capacity > 10:
                    self._resize(self.capacity // 2)
                
                return True
        return False
    
    def get_all_restaurants(self):
        """Return a list of all restaurants (no None values)"""
        return [self.restaurants[i] for i in range(self.size) if self.restaurants[i]]
    
    def get_size(self):
        """Return the number of restaurants"""
        return self.size