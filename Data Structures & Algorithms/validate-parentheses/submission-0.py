class Solution:
    def isValid(self, s: str) -> bool:
        # if the length of the string is odd, it cannot be valid
        if len(s) % 2 != 0:
            return False
        brackets = []
        # store closing => opening brackets in a dictionary
        bracket_map = {")": "(", "]": "[", "}": "{"}
        for ch in s:
            # if the character is a closing bracket
            if ch in bracket_map:
                # if brackets is empty or the last bracket in the list is not the matching opening bracket
                if not brackets or brackets[-1] != bracket_map[ch]:
                    return False
                # else pop the last bracket from the list
                brackets.pop()
            else:
                # if the character is an opening bracket, add it to the list
                brackets.append(ch)
        # if brackets is empty, all brackets are matched
        return not brackets
        