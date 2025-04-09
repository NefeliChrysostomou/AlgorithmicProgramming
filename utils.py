import csv
from models import Customer, Restaurant, Ride
from data_structures import DynamicArray, SinglyLinkedList, DoublyLinkedList, BinaryTree, BST

tier_order = ['bronze', 'silver', 'gold', 'platinum']  # Adding new items in ascending order

def import_csv(filename):
    """Read the CSV file and return headers and data"""
    headers = []
    data = []

    try:
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)  # Read headers
            for row in csv_reader:
                data.append(row)  # Collect data rows

        return headers, data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None, None


def match_headers(headers):
    """Determine the model class based on CSV headers"""
    if 'customer_id' in headers and 'name' in headers and 'age' in headers and 'gender' in headers:
        return Customer
    elif 'restaurant_id' in headers and 'name' in headers and 'location' in headers:
        return Restaurant
    elif 'ride_id' in headers and 'name' in headers and 'location' in headers and 'duration' in headers and 'ticket_tier' in headers:
        return Ride
    else:
        print("Error: Unknown CSV format.")
        return None


def data_to_objects(data, headers):
    """Convert CSV data to objects based on the headers"""
    model_class = match_headers(headers)
    if not model_class:
        return []

    objects = []

    for row in data:
        # Map row data to the appropriate object attributes
        if model_class == Customer:
            customer_id, name, age, gender = row[0], row[1], int(row[2]), row[3]
            ticket_tier = row[4].lower() if len(row) > 4 else 'bronze'  # default to 'bronze' if not found
            if ticket_tier not in tier_order:
                ticket_tier = 'bronze'  # Ensure ticket_tier is valid
            customer = Customer(customer_id, name, age, gender, ticket_tier)
            objects.append(customer)

        elif model_class == Restaurant:
            restaurant_id, name, location = row[0], row[1], row[2]
            type_ = row[3:] if len(row) > 3 else []  # Default to empty if no type is provided
            restaurant = Restaurant(restaurant_id, name, location, type_)
            objects.append(restaurant)

        elif model_class == Ride:
            ride_id, name, location, duration, ticket_tier = row[0], row[1], row[2], row[3], row[4].lower()
            if ticket_tier not in tier_order:
                ticket_tier = 'bronze'  # Default to 'bronze' if not valid
            ride = Ride(ride_id, name, location, duration, ticket_tier)
            objects.append(ride)

    return objects


def print_data(filename):
    """Load CSV and print the corresponding objects"""
    headers, data = import_csv(filename)
    if headers is None or data is None:
        return

    # Convert the data to objects
    objects = data_to_objects(data, headers)

    # Print out the objects
    for obj in objects:
        print(obj)


# Example Usage:
if __name__ == "__main__":
    print("Loading and printing Customer data from 'customers.csv'")
    print_data('customers.csv')

    print("\nLoading and printing Restaurant data from 'restaurants.csv'")
    print_data('restaurants.csv')

    print("\nLoading and printing Ride data from 'rides.csv'")
    print_data('rides.csv')
