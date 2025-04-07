from models import Customer, Restaurant
from data_structures import CustomerLinkedList, CustomerArray, RestaurantArray
from algorithms import binary_search_most_rides, quicksort_by_demographics, linear_search_by_location, merge_sort_by_price
from utils import import_customers_from_csv, import_restaurants_from_csv

def main():
    print("===== CUSTOMER SECTION =====")
    customer_list = CustomerLinkedList()
    
    # Try to import customers from CSV
    try:
        imported_customers = import_customers_from_csv('customers.csv')
        if imported_customers:
            customer_list = imported_customers
            print("Successfully imported customers from CSV.")
        else:
            raise FileNotFoundError("No customers imported from CSV")
    except Exception as e:
        print(f"Using sample data instead. Error: {e}")
        # Create sample data
        sample_customers = [
            Customer("1", "John Doe", 25, "Male", ["ride1", "ride2"]),
            Customer("2", "Jane Smith", 30, "Female", ["ride1", "ride2", "ride3", "ride4"]),
            Customer("3", "Bob Johnson", 45, "Male", ["ride1"]),
            Customer("4", "Alice Brown", 22, "Female", ["ride2", "ride3"])
        ]
        
        for customer in sample_customers:
            customer_list.add_customer(customer)
    
    customers = customer_list.get_all_customers()
    
    customer_array = CustomerArray()
    for customer in customers:
        customer_array.add_customer(customer)
    
    # Sort by ride count for binary search
    sorted_customers = customer_array.sort_by_rides()
    
    # Find customer with most rides using binary search on sorted array
    most_rides_customer = binary_search_most_rides(sorted_customers)
    print(f"\nCustomer with most rides: {most_rides_customer}")
    
    # Sort customers by different demographics using quicksort
    print("\nCustomers sorted by age:")
    age_sorted = quicksort_by_demographics(customers, 'age')
    for customer in age_sorted:
        print(customer)
    
    print("\nCustomers sorted by gender:")
    gender_sorted = quicksort_by_demographics(customers, 'gender')
    for customer in gender_sorted:
        print(customer)
    
    print("\nCustomers sorted by name:")
    name_sorted = quicksort_by_demographics(customers, 'name')
    for customer in name_sorted:
        print(customer)



    print("\n===== RESTAURANT SECTION =====")
    
    # Try to import restaurants from CSV
    try:
        imported_restaurants = import_restaurants_from_csv('restaurants.csv')
        if imported_restaurants:
            restaurant_array = imported_restaurants
            print("Successfully imported restaurants from CSV.")
        else:
            raise FileNotFoundError("No restaurants imported from CSV")
    except Exception as e:
        print(f"Using sample restaurant data instead. Error: {e}")
        # Create sample restaurant data
        restaurant_array = RestaurantArray()
        
        r1 = Restaurant("R1", "Burger Palace", "North Wing", 
                      ["Cheeseburger", "Fries", "Soda"], 
                      [8.99, 3.99, 2.49])
        r2 = Restaurant("R2", "Pizza Place", "North Wing", 
                      ["Pepperoni Pizza", "Cheese Pizza", "Garlic Bread"], 
                      [12.99, 10.99, 4.99])
        r3 = Restaurant("R3", "Ice Cream Shop", "South Wing", 
                      ["Vanilla Cone", "Chocolate Sundae", "Banana Split"], 
                      [3.49, 5.99, 7.99])
        r4 = Restaurant("R4", "Taco Stand", "East Wing", 
                      ["Beef Taco", "Chicken Burrito", "Nachos"], 
                      [4.99, 9.99, 7.49])
        r5 = Restaurant("R5", "Noodle House", "South Wing", 
                      ["Ramen", "Pad Thai", "Fried Rice"], 
                      [11.99, 13.49, 10.99])
        
        for restaurant in [r1, r2, r3, r4, r5]:
            restaurant_array.add_restaurant(restaurant)
    
    # Display all restaurants
    restaurants = restaurant_array.get_all_restaurants()
    print("\nAll restaurants in the food court:")
    for restaurant in restaurants:
        print(restaurant)
    
    # Linear search: find restaurants by location
    location_to_search = "North Wing"
    matching_restaurants = linear_search_by_location(restaurant_array, location_to_search)
    print(f"\nRestaurants in {location_to_search}:")
    if matching_restaurants:
        for restaurant in matching_restaurants:
            print(restaurant)
    else:
        print(f"No restaurants found in {location_to_search}")
    
    # Merge sort: sort restaurants by average meal price
    sorted_restaurants = merge_sort_by_price(restaurants)
    print("\nRestaurants sorted by average meal price:")
    for restaurant in sorted_restaurants:
        print(restaurant)

if __name__ == "__main__":
    main()