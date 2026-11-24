class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window approach
        char_set = set()
        l = 0
        max_length = 0
        for r in range(len(s)):
            # If the character is already in the set, 
            # remove characters from the left until it's not
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            # Add the current character to the set
            char_set.add(s[r])
            # Update the maximum length found
            max_length = max(max_length, r - l + 1)
        return max_length