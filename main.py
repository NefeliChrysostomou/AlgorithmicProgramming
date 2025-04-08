from models import Customer, Restaurant
from data_structures import CustomerLinkedList, RestaurantLinkedList
from algorithms import quicksort, linear_search, binary_search_by_key, merge_sort, binary_search_most
from utils import import_customers_from_csv, import_restaurants_from_csv

def main():
    print("===== CUSTOMER SECTION =====")
    
    # Initialize customer list
    customer_list = CustomerLinkedList()

    # Try to import customers from CSV
    try:
        imported_customer_list = import_customers_from_csv('customers.csv')
        if imported_customer_list:
            print("Successfully imported customers from CSV.")
            customer_list = imported_customer_list
        else:
            raise FileNotFoundError("No customers imported from CSV")
    except Exception as e:
        print(f"Using sample customer data instead. Error: {e}")
        # Fallback sample data
        sample_customers = [
            Customer("1", "John Doe", 25, "Male"),
            Customer("2", "Jane Smith", 30, "Female"),
            Customer("3", "Bob Johnson", 45, "Male"),
            Customer("4", "Alice Brown", 22, "Female"),
        ]
        for customer in sample_customers:
            customer_list.add_customer(customer)

    customers = customer_list.get_all_customers()


    # Quicksort by demographics
    if customers:
        print("\nCustomers sorted by age:")
        for customer in quicksort(customers, key_func=lambda c: c.age):
            print(customer)

        print("\nCustomers sorted by gender:")
        for customer in quicksort(customers, key_func=lambda c: c.gender):
            print(customer)

        print("\nCustomers sorted by name:")
        for customer in quicksort(customers, key_func=lambda c: c.name):
            print(customer)

        
        # Merge Sort by ticket tier 
        ticket_tier_order = {
            'Bronze': 1,
            'Silver': 2,
            'Gold': 3,
            'Platinum': 4
        }

        if customers:
            print("\nCustomers sorted by ticket tier:")
            sorted_by_ticket_tier = merge_sort(customers, key_func=lambda c: ticket_tier_order.get(c.ticket_tier[0], 0))
            for customer in sorted_by_ticket_tier:
                print(customer)


        # Binary Search by name
        if customers:
            sorted_customers = customer_list.sort_by_name()

        target_name = "John Doe"
        index = binary_search_by_key(sorted_customers, target_value=target_name, key_func=lambda c: c.name)
        if index != -1:
            print(f"\nCustomer found by binary search: {sorted_customers[index]}")
        else:
            print(f"\nCustomer with name '{target_name}' not found.")


        # Binary Search Most by ticket tier (using numerical comparison for ticket tiers)
        if customers:
            most_ticket_tier_customer = binary_search_most(customers, key_func=lambda c: ticket_tier_order.get(c.ticket_tier[0], 0))
            print(f"\nCustomer with highest ticket tier: {most_ticket_tier_customer}")



    print("\n===== RESTAURANT SECTION =====")

    # Initialize restaurant data structures
    restaurant_linked_list = RestaurantLinkedList()

    # Try to import restaurants from CSV
    try:
        imported_restaurant_array = import_restaurants_from_csv('restaurants.csv', use_linked_list=False)
        imported_restaurant_linked_list = import_restaurants_from_csv('restaurants.csv', use_linked_list=True)

        if imported_restaurant_array:
            restaurant_array = imported_restaurant_array
            restaurant_linked_list = imported_restaurant_linked_list
            print("Successfully imported restaurants from CSV.")
        else:
            raise FileNotFoundError("No restaurants imported from CSV")
    except Exception as e:
        print(f"Using sample restaurant data instead. Error: {e}")
        sample_restaurants = [
            Restaurant("R1", "Burger Palace", "North Wing", "American"),
            Restaurant("R2", "Pizza Place", "North Wing", "Pizzeria"),
            Restaurant("R3", "Ice Cream Shop", "South Wing", "Dessert"),
            Restaurant("R4", "Taco Stand", "East Wing", "Mexican"),
            Restaurant("R5", "Noodle House", "South Wing", "Asian"),
        ]
        for restaurant in sample_restaurants:
            restaurant_array.add_restaurant(restaurant)
            restaurant_linked_list.add_restaurant(restaurant)


    # Display all restaurants from linked list
    restaurants_linked_list = restaurant_linked_list.get_all_restaurants()
    print("\nAll restaurants in the food court:")
    for restaurant in restaurants_linked_list:
        print(restaurant)


    # Linear search for restaurants by location
    # Define target location
    location_to_search = "South Wing"

    matching_restaurants = linear_search(
        restaurant_linked_list,
        target_value=location_to_search,
        key_func=lambda r: r.location
    )
    print(f"\nRestaurants in {location_to_search}:")
    if matching_restaurants:
        for restaurant in matching_restaurants:
            print(restaurant)
    else:
        print(f"No restaurants found in {location_to_search}")

    # Merge Sort for restaurants by name
    print("\nRestaurants sorted by name:")
    sorted_restaurants_by_name = merge_sort(restaurant_linked_list, key_func=lambda r: r.name)
    for restaurant in sorted_restaurants_by_name:
        print(restaurant)

if __name__ == "__main__":
    main()
