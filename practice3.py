def return_only_integer(lst):
    result = []
    
    for item in lst:
        if item.isdigit():
            result.append(item)
    
    return result


# Example
print(return_only_integer([9, 2, "bvrn", "gcet", "adit", 16]))