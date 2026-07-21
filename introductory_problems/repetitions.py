"""
You are given a DNA sequence: a string consisting of characters A, C, G, and T. 
Your task is to find the longest repetition in the sequence. 
This is a maximum-length substring containing only one type of character.
"""

def solve(s: str):
    longest = 1
    cur_longest = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            cur_longest += 1
            longest = max(longest, cur_longest)
        else:
            cur_longest = 1
    
    return longest

def main():
    s = str(input())
    ans = solve(s)
    print(ans)
    

if __name__ == "__main__":
    main()