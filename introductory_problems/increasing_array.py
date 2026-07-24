"""
You are given an array of n integers. You want to modify the array so that it is increasing, 
i.e., every element is at least as large as the previous element.
On each move, you may increase the value of any element by one. What is the minimum number of moves required?
"""

def solve(n: int, nums: list[int]) -> int:
   num_moves = 0
   for i in range(1, n):
       if nums[i] < nums[i - 1]:
           # if the current value (which is more advanced) is less than the one before

           # calculate the difference
           diff = nums[i - 1] - nums[i] 
           
           # min number of moves to atleast match 
           num_moves += diff

           # update current value of the number, to match the greater value before 
           nums[i] = nums[i - 1]

   return num_moves

def main():
    n = int(input())
    nums = list(map(int, input().split()))

    ans = solve(n, nums)
    print(ans)

if __name__ == "__main__":
    main()