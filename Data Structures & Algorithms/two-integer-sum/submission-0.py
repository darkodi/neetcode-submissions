class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # dict where key = nums value, value = nums key
        for i, v in enumerate(nums): # one pass
            complement = target - v
            if complement in seen:
                return [seen[complement], i]
            seen[v] = i
        return []
        