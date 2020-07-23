'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers(arr):
    # Your code here
    prod_arr = [1] * len(arr)
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                prod_arr[i] *= arr[j]
    return prod_arr


"""
nested for loop would be easiest -> but it's n^2 (OKAY IN FIRST PASS)
NO DIVISION - cooler this way
first thought is list comprehension? but that might be n^2
second thought - initialize an array of ones and operate on them
    -> this would be a cool use of lambda functions, which i've never used
    -> same for map() function
    plan:
        initialize list of one elements based on len of given arr
    reality: complicated? can't exclude certain elements with map
    ----> FURTHER STUDY
        map can be enumerated so you send a tuple! let's try it
    issue: not comfortable with lambda functions ALSO only one line
        -> so defining a standard function instead
    issue: this is still n^2 not n right?
    and it doesn't work
third thought:
    just go back to list comprehension and at least get it working
"""

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
    #        9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
