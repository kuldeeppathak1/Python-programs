def second_largest(nums):
    unique_nums = list(set(nums))   # Remove duplicates
    if len(unique_nums) < 2:
        return None  # Not enough elements
    unique_nums.sort()
    return unique_nums[-2]

# Example
numbers = [10, 20, 4, 45, 99, 99]
print("Second largest:", second_largest(numbers))

############################
def second_largest1(arr):
    if len(arr) < 2:
        return None
    
    first = second = float('-inf')
    
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    
    return second if second != float('-inf') else None
    
    
numbers = [10, 20, 4, 45, 99, 99]
print(second_largest1(numbers))