import time

"""
You are given all numbers between 1, 2, ..., n except one. Your task is to find the missing number.
"""
def solve(n: int, nums: list[int]) -> int:
    seen = set(nums)
    for i in range(1, n + 1):
        if i not in seen:
            return i
    
    return -1

def main():

    n = int(input())
    nums = list(map(int, input().split()))
    
    start = time.time()
    print(solve(n, nums))
    end = time.time()
    # print(f"Elapsed: {end - start:.6f} seconds")

if __name__ == "__main__":
    main()