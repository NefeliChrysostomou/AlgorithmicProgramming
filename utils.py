import csv
from models import Customer, Restaurant
from data_structures import CustomerLinkedList, RestaurantArray

def import_customers_from_csv(filename):
    customer_list = CustomerLinkedList()
    
    try:
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)  # Skip header row
            
            for row in csv_reader:
                customer_id, name, age, gender = row[0], row[1], int(row[2]), row[3]
                # Assume ride data is in subsequent columns
                rides_taken = row[4:] if len(row) > 4 else []
                
                customer = Customer(customer_id, name, age, gender, rides_taken)
                customer_list.add_customer(customer)
        
        return customer_list
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None


def import_restaurants_from_csv(filename):
    """Import restaurants from a CSV file into a RestaurantArray"""
    restaurant_array = RestaurantArray()
    
    try:
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)  # Skip header row
            
            for row in csv_reader:
                restaurant_id, name, location = row[0], row[1], row[2]
                
                # Parse menu items and prices (if present)
                menu_items = []
                prices = []
                
                if len(row) > 3 and len(row) % 2 == 1:  # Make sure we have pairs of items/prices
                    for i in range(3, len(row), 2):
                        if i+1 < len(row):  # Make sure we don't go out of bounds
                            menu_items.append(row[i])
                            prices.append(float(row[i+1]))
                
                restaurant = Restaurant(restaurant_id, name, location, menu_items, prices)
                restaurant_array.add_restaurant(restaurant)
        
        return restaurant_array
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None