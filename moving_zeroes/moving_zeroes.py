'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    zeros = []
    idx = 0
    length = len(arr) - 1
    while idx < length:
        if arr[idx] == 0:
            zeros.append(arr[idx])
            arr.pop(idx)
            length -= 1
        else:
            idx += 1
    for i in zeros:
        arr.append(i)
    return arr
if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 0, 0, 0, 3, 2, 1]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
    print(len(arr))