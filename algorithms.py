def binary_search_most(items, key_func):
    """Return the item with the highest value based on the key function"""
    if not items:
        return None
    return max(items, key=key_func)


def binary_search_by_key(sorted_items, target_value, key_func):
    """Generic binary search to find an item by the target value using key_func"""
    left, right = 0, len(sorted_items) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_value = key_func(sorted_items[mid])
        if mid_value == target_value:
            return mid
        elif mid_value < target_value:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def quicksort(items, key_func):
    """Generic quicksort using key function"""
    if len(items) <= 1:
        return items
    
    pivot = items[len(items) // 2]
    pivot_value = key_func(pivot)
    
    left = [x for x in items if key_func(x) < pivot_value]
    middle = [x for x in items if key_func(x) == pivot_value]
    right = [x for x in items if key_func(x) > pivot_value]
    
    return quicksort(left, key_func) + middle + quicksort(right, key_func)



def linear_search(items, target_value, key_func):
    """Generic linear search to find items by attribute using key_func"""
    results = []
    
    # If collection has a 'get_all' method, use it
    if hasattr(items, 'get_all'):
        items = items.get_all()
    elif hasattr(items, 'get_all_restaurants'):
        items = items.get_all_restaurants()
    
    for item in items:
        if item and key_func(item).lower() == target_value.lower():
            results.append(item)
    
    return results


def merge_sort(items, key_func):
    """Generic merge sort using key function"""
    if hasattr(items, 'get_all_restaurants'):
        items = items.get_all_restaurants()
    elif hasattr(items, 'get_all'):
        items = items.get_all()
    
    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = merge_sort(items[:mid], key_func)
    right = merge_sort(items[mid:], key_func)
    
    return merge(left, right, key_func)

def merge(left, right, key_func):
    """Helper merge function"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if key_func(left[i]) <= key_func(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result
