class Solution:

    def encode(self, strs: List[str]) -> str:
        # each string is encoded as <length>#<string>
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            # 1. read the length of the string
            while s[j] != '#':
                j += 1
            length = int(s[i:j]) # not including j (which is #)
            # 2. read the string
            str_val = s[j + 1 : j + 1 + length]
            # 3. add to list
            res.append(str_val)
            # 4. move to the next string pointing to its length
            i = j + 1 + length
        return res