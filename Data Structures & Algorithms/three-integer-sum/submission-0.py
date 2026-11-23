class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array to use two pointers
        nums.sort()
        res = []
        # i goes from 0 to len(nums) - 2 because we need at least 3 numbers
        for i in range(len(nums)-2):
            # skip duplicates for the first number
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # use two pointers to find the other two numbers
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0: # too small, move left
                    left += 1
                elif total > 0: # too big, move right
                    right -= 1
                else: # found a triplet
                    res.append([nums[i], nums[left], nums[right]])
                    # skip duplicates for the second number
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # skip duplicates for the third number
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # move both pointers after finding a valid triplet is necessary
                    # because if only one moved, the sum would no longer be 0.     
                    left += 1
                    right -= 1
        return res
        