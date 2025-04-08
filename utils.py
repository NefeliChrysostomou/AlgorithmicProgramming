import csv
from models import Customer, Restaurant
from data_structures import CustomerLinkedList, RestaurantArray, RestaurantLinkedList

def import_customers_from_csv(filename):
    """Import customers from a CSV file into a CustomerLinkedList"""
    customer_array = CustomerLinkedList()
    
    try:
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)  # Skip header row
            
            for row in csv_reader:
                customer_id, name, age, gender = row[0], row[1], int(row[2]), row[3]
                ticket_tier = row[4:] if len(row) > 4 else []
                
                customer = Customer(customer_id, name, age, gender, ticket_tier)
                customer_array.add_customer(customer)
        
        return customer_array
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None


def import_restaurants_from_csv(filename, use_linked_list=False):
    """
    Import restaurants from a CSV file
    By default uses RestaurantArray
    If use_linked_list=True, uses RestaurantLinkedList instead
    """
    if use_linked_list:
        restaurant_container = RestaurantLinkedList()
        add_method = restaurant_container.add_restaurant
    else:
        restaurant_container = RestaurantArray()
        add_method = restaurant_container.add_restaurant

    try:
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)  # Skip header row

            for row in csv_reader:
                restaurant_id, name, location = row[0], row[1], row[2]

                type = row[3:] if len(row) > 3 else []

                restaurant = Restaurant(restaurant_id, name, location, type)
                add_method(restaurant)

        return restaurant_container
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
