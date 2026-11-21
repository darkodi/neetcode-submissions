class Solution:
    def isPalindrome(self, s: str) -> bool:
         # use two pointers to check if the string is a palindrome
        left, right = 0, len(s) - 1
        while left < right:
            # skip non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            # both characters are alphanumeric, if their lowercases are NOT equal they are not palindroms
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1
        return True