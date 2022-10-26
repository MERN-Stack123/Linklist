class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""
        for center in range(len(s)):
            for offset in [0, 1]:
                start, end = center, center + offset
                while True:
                    if start < 0 or end > len(s) - 1 or s[start] != s[end]:
                        break
                    else:
                        palin = s[start:end+1]
                        longest_palindrome = palin if len(palin) > len(longest_palindrome) else longest_palindrome   
                        start=start+1
                        end=end+1
        return longest_palindrome