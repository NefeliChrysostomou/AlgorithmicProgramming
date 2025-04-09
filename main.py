from models import Customer, Ride, Restaurant
from algorithms import quicksort, merge_sort, linear_search, binary_search_by_key
from data_structures import DynamicArray, SinglyLinkedList, DoublyLinkedList, BinaryTree, BST

# Sample data for testing.
customers = [
    Customer("C1", "Alice", 30, "Female", "gold"),
    Customer("C2", "Bob", 25, "Male", "silver"),
    Customer("C3", "Charlie", 35, "Male", "platinum"),
    Customer("C4", "Diana", 28, "Female", "bronze")
]

rides = [
    Ride("R1", "Roller Coaster", "Park", "5", "silver"),
    Ride("R2", "Ferris Wheel", "Park", "7", "gold"),
    Ride("R3", "Bumper Cars", "Carnival", "3", "bronze"),
    Ride("R4", "Haunted House", "Fun Land", "6", "platinum")
]

restaurants = [
    Restaurant("Res1", "Burger King", "Mall", ["Fast Food"]),
    Restaurant("Res2", "Sushi World", "Downtown", ["Japanese"]),
    Restaurant("Res3", "Pasta Palace", "Uptown", ["Italian"]),
    Restaurant("Res4", "Curry House", "City Center", ["Indian"])
]

all_data = {
    "Customer": customers,
    "Ride": rides,
    "Restaurant": restaurants
}

# Data structure classes to test.
data_structure_classes = [DynamicArray, SinglyLinkedList, DoublyLinkedList, BinaryTree, BST]

# Sorting algorithms to test.
sorting_algorithms = [quicksort, merge_sort]

# Search algorithms to test.
search_algorithms = [linear_search, binary_search_by_key]

# Helper: Insert a list of objects into a data structure instance.
def insert_into_structure(ds_class, objects):
    print(f"\nInserting {len(objects)} items into {ds_class.__name__} ...")
    ds_instance = ds_class()
    for obj in objects:
        try:
            # Try common methods: insert (for trees), then add, then append.
            if hasattr(ds_instance, "insert"):
                ds_instance.insert(obj)
            elif hasattr(ds_instance, "add"):
                ds_instance.add(obj)
            elif hasattr(ds_instance, "append"):
                ds_instance.append(obj)
            else:
                raise AttributeError("No supported insertion method!")
        except Exception as e:
            print(f"  ERROR inserting {obj}: {e}")
    return ds_instance

# Helper: Retrieve all objects from a data structure.
def retrieve_all(ds_instance):
    if hasattr(ds_instance, "get_all"):
        return ds_instance.get_all()
    elif hasattr(ds_instance, "inorder"):
        items = []
        def inorder(node):
            if node:
                inorder(node.left)
                items.append(node.data)
                inorder(node.right)
        inorder(ds_instance.root)
        return items
    else:
        try:
            return list(ds_instance)
        except Exception as e:
            print(f"  ERROR retrieving items: {e}")
            return []

# Key functions for sorting and searching.
def key_customer_age(cust):
    return cust.get_age()

def key_ride_duration(ride):
    return int(ride.get_duration())

def key_restaurant_name(rest):
    return rest.get_name()

def key_customer_name(cust):
    return cust.get_name()

def key_ride_name(ride):
    return ride.get_name()

def key_restaurant_name_search(rest):
    return rest.get_name()

def run_sorting_test(ds_instance, sort_algo, key_func):
    try:
        # Retrieve items from the structure.
        items = retrieve_all(ds_instance)
        sorted_items = sort_algo(items, key_func)
        return sorted_items
    except Exception as e:
        print(f"  ERROR running sort {sort_algo.__name__}: {e}")
        return None

def run_search_test(ds_instance, search_algo, target, key_func):
    try:
        # Retrieve items (or use get_all when available).
        items = retrieve_all(ds_instance)
        result = search_algo(items, target, key_func)
        return result
    except Exception as e:
        print(f"  ERROR running search {search_algo.__name__}: {e}")
        return None

if __name__ == "__main__":
    print("=== Testing Compatibility of Sorting and Searching with Data Structures ===\n")
    
    # Loop over each data structure and each model type.
    for ds_class in data_structure_classes:
        print(f"\n--- DATA STRUCTURE: {ds_class.__name__} ---")
        for model_name, objects in all_data.items():
            print(f"\nModel Type: {model_name}")
            # Insert sample objects into the data structure.
            ds_instance = insert_into_structure(ds_class, objects)
            retrieved_items = retrieve_all(ds_instance)
            print("Retrieved items:")
            for item in retrieved_items:
                print("  ", item)
            
            # Run each sorting algorithm on this ds.
            for sort_algo in sorting_algorithms:
                # Choose a key function based on the model.
                if model_name == "Customer":
                    key_func = key_customer_age
                elif model_name == "Ride":
                    key_func = key_ride_duration
                elif model_name == "Restaurant":
                    key_func = key_restaurant_name
                else:
                    key_func = lambda x: x
                
                print(f"\nSorting using {sort_algo.__name__} by appropriate key:")
                sorted_items = run_sorting_test(ds_instance, sort_algo, key_func)
                if sorted_items is not None:
                    if model_name == "Customer":
                        sorted_keys = [key_customer_age(x) for x in sorted_items]
                    elif model_name == "Ride":
                        sorted_keys = [key_ride_duration(x) for x in sorted_items]
                    elif model_name == "Restaurant":
                        sorted_keys = [key_restaurant_name(x) for x in sorted_items]
                    else:
                        sorted_keys = sorted_items
                    print("Sorted keys:", sorted_keys)
            
            # Run each search algorithm on this ds.
            # For search, we choose a target from the first object's key.
            if retrieved_items:
                if model_name == "Customer":
                    key_func = key_customer_name
                    target = key_customer_name(retrieved_items[0])
                elif model_name == "Ride":
                    key_func = key_ride_name
                    target = key_ride_name(retrieved_items[0])
                elif model_name == "Restaurant":
                    key_func = key_restaurant_name_search
                    target = key_restaurant_name_search(retrieved_items[0])
                else:
                    key_func = lambda x: x
                    target = retrieved_items[0]
                
                print(f"\nSearching for target '{target}' using different algorithms:")
                for search_algo in search_algorithms:
                    result = run_search_test(ds_instance, search_algo, target, key_func)
                    if search_algo == binary_search_by_key:
                        if result != -1:
                            found = retrieve_all(ds_instance)[result] if result < len(retrieve_all(ds_instance)) else None
                            print(f"  {search_algo.__name__}: Found at index {result}: {found}")
                        else:
                            print(f"  {search_algo.__name__}: Target not found.")
                    else:
                        print(f"  {search_algo.__name__}: Found items:")
                        if result:
                            for r in result:
                                print("   ", r)
                        else:
                            print("    No results found.")

    print("\n=== Compatibility Testing Complete ===")
