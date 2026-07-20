"""
Consider an algorithm that takes as input a positive integer n. If n is even, the algorithm divides it by two, and if n is odd, 
the algorithm multiplies it by three and adds one. The algorithm repeats this, until n is one. 

Your task is to simulate the execution of the algorithm for a given value of n.
"""

def solve(n: int) -> list[int]:
    ans = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = (n * 3) + 1
        
        ans.append(n)
    
    return ans

def main():
    n = int(input())
    ans = solve(n)
    print(*ans)

if __name__ == "__main__":
    main()