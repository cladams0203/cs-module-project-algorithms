'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    arr.sort()
    for idx, num in enumerate(arr):
        if num != arr[idx + 1]:
            if arr[idx + 1] != arr[idx + 2]:
                return arr[idx + 1]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")