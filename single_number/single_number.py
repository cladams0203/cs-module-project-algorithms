'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
'''
First day code 33 operations on python tutor
'''
# def single_number(arr):
#     # Your code here
#     arr.sort()
#     for idx, num in enumerate(arr):
#         if num != arr[idx + 1]:
#             if arr[idx + 1] != arr[idx + 2]:
#                 return arr[idx + 1]

'''
Second day code 44 operations on python tutor
'''
def single_number(arr):
    # keep track of number of times an item occurs in input
    counts = {}

    # loop through input list O(n)
    for num in arr:
        # if item in counts
        if num in counts:
            # remove item
            del counts[num]
        # otherwise
        else:
            counts[num] = 1
            # add item​
    for k, v in counts.items():  # O(1)
        if v == 1:
            return k

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")