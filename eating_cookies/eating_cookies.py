'''
Input: an integer
Returns: an integer
'''
from functools import lru_cache





@lru_cache(maxsize=5000)

def eating_cookies(n):
    # Your code here
    cookiesAtOnce = [1, 2, 3]
    if n == 0:
        return 1
    if n < 0:
        return 0
    count = 0
    for i in range(len(cookiesAtOnce)):
        count += eating_cookies(n - cookiesAtOnce[i])
    return count

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
