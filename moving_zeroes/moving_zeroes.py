'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here
    zero_count = curIndex = 0
    while curIndex < len(arr):
        if arr[curIndex] == 0:
            # don't increment index!!!!!
            arr.pop(curIndex)
            zero_count += 1
        else:
            # do increment index!
            curIndex += 1
    # reappend those zeroes!
    arr.extend([0] * zero_count)
    return arr


"""
first pass:
    i'm thinking of a bubble sort? bubble up the zeroes?
    counting sort wouldn't actually be terrible here?
        -> except it's asking for a single pass through arr
    so maybe use a loop?
        -> for loop testing showed issues with sequential zeroes and
           further research showed that using pop in a for loop is 
           generally considered bad practice
        -> while loop implementation works GREAT
        ISSUE:
            have to append a bunch of zeroes at the end, which potentially 
            reallocates a lot of memory
            solution -> i can use extend~! (one potential reallocation)
"""

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
