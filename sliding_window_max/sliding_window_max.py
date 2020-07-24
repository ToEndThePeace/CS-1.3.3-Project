'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

def sliding_window_max(nums, k):
    # Your code here
    max_arr = [None] * (len(nums) - k + 1)
    for i in range(len(max_arr)):
        max_arr[i] = max(nums[i:i + k])
    return max_arr


"""
first step is initialize array with fixed length of len(nums) - k + 1
use modified range along with slicing to accomplish the task
    -> first thought is this one seems the easiest out of all of them
    -> range needs to be len of max_arr instead of nums
    -> this is a good first pass, but it takes a while to run on large inputs
I CAN DO THIS IWTH RECURSIONnnnnnnnn--->
    check that len(nums) >= k - 1?
        -> if it isn't just return []?
    recurse?
        -> return [max] + recursion()
"""


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
