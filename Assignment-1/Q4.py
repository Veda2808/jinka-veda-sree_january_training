# Q4.py
# This function removes all even numbers correctly

def remove_even(nums):
    """
    Returns a new list with only odd numbers
    """
    result = []
    for num in nums:
        if num % 2 != 0:
            result.append(num)
    return result


# Test input
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(remove_even(nums))
