def second_largest(nums):
    unique_nums = list(set(nums))   # Remove duplicates
    if len(unique_nums) < 2:
        return None  # Not enough elements
    unique_nums.sort()
    return unique_nums[-2]

# Example
numbers = [10, 20, 4, 45, 99, 99]
print("Second largest:", second_largest(numbers))