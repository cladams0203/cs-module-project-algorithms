'''
Input: a List of integers
Returns: a List of integers
'''
'''
First Day code 47 operations on python tutor
'''
# def moving_zeroes(arr):
#     # Your code here
#     zeros = []
#     idx = 0
#     length = len(arr) - 1
#     while idx < length:
#         if arr[idx] == 0:
#             zeros.append(arr[idx])
#             arr.pop(idx)
#             length -= 1
#         else:
#             idx += 1
#     for i in zeros:
#         arr.append(i)
#     return arr
'''
Second day code 39 operations on python tutor
'''
def moving_zeroes(arr):
    left = 0
    right = len(arr) - 1
    while right > left:
        if arr[left] == 0 and arr[right] != 0:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            left += 1
            right -= 1
        if arr[left] != 0:
            left += 1
        if arr[right] == 0:
            right -= 1
    return arr
if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 0, 0, 0, 3, 2, 1]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
    print(len(arr))