'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


# def single_number(arr):
#     # Your code here
#     single = None
#     arr.sort() # O(n)
#     for i in range(0, len(arr), 2): # O(n)
#         if i == len(arr) - 1 or arr[i] != arr[i + 1]:
#             return arr[i]


def single_number(arr):
    set_arr = set()  # initialize empty set O(1)
    for i in arr:  # iterate over array O(n)
        if i in set_arr:
            set_arr.remove(i)  # O(1)
        else:
            set_arr.add(i)  # O(1)
    return list(set_arr)[0]  # O(1)


"""
first-pass thoughts:
    array should only be iterated over once, so shouldn't use "in"
    O(1) space complexity means I don't create a new array right?
    Solutions:
        1. sort the array, then loop over and check pairs? <- probably efficient? needs a sort
            -> default array sort would be a decent enough first implementation
            ISSUES:
                shouldn't be memory efficient, but still runs fast?
            PROS:
                cuts off early if found, doesn't need to ALWAYS hit every element
                simple, terse
DICTIONARIES are good at checking for dupes
also SETS
"""

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
