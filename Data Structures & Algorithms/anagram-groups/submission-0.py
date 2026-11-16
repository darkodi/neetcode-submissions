class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # so I don't check if key in dict exists
        for s in strs:
            chFreq = 26 * [0] # for every string initialize new empty 26-size list
            for ch in s:
                chFreq[ord(ch) - ord('a')] += 1
            res[tuple(chFreq)].append(s) # append to extend the list
        return list(res.values())

        