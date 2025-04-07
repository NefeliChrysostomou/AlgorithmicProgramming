def binary_search_most_rides(sorted_customers):
    """
    Since customers are sorted by ride count, the one with most rides
    will be at the end of the array
    """
    if not sorted_customers:
        return None
    return sorted_customers[-1]

def binary_search_by_ride_count(sorted_customers, target_rides):
    """Binary search to find customers with an exact ride count"""
    left = 0
    right = len(sorted_customers) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if sorted_customers[mid].get_ride_count() == target_rides:
            return mid
        elif sorted_customers[mid].get_ride_count() < target_rides:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  

def quicksort_by_demographics(customers, demographic_key):
    """Sort customers by the specified demographic attribute using quicksort"""
    if len(customers) <= 1:
        return customers
    
    pivot = customers[len(customers) // 2]
    
    def get_value(customer):
        if demographic_key == 'age':
            return customer.get_age()
        elif demographic_key == 'gender':
            return customer.get_gender()
        elif demographic_key == 'name':
            return customer.get_name()
        elif demographic_key == 'rides':
            return customer.get_ride_count()
        # Default to customer ID
        return customer.get_customer_id()
    
    pivot_value = get_value(pivot)
    
    left = [x for x in customers if get_value(x) < pivot_value]
    middle = [x for x in customers if get_value(x) == pivot_value]
    right = [x for x in customers if get_value(x) > pivot_value]
    
    return quicksort_by_demographics(left, demographic_key) + middle + quicksort_by_demographics(right, demographic_key)



def linear_search_by_location(restaurant_array, target_location):
    """
    Linear search to find restaurants in a specific location
    Returns a list of restaurants that match the location
    """
    matching_restaurants = []
    
    for i in range(restaurant_array.get_size()):
        restaurant = restaurant_array.get_restaurant(i)
        if restaurant and restaurant.get_location().lower() == target_location.lower():
            matching_restaurants.append(restaurant)
    
    return matching_restaurants

def merge_sort_by_price(restaurants):
    """Sort restaurants by average meal price using merge sort"""
    if len(restaurants) <= 1:
        return restaurants
    
    mid = len(restaurants) // 2
    left = restaurants[:mid]
    right = restaurants[mid:]
    
    left = merge_sort_by_price(left)
    right = merge_sort_by_price(right)
    
    return merge(left, right)

def merge(left, right):
    """Helper function for merge sort"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i].get_average_price() <= right[j].get_average_price():
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result