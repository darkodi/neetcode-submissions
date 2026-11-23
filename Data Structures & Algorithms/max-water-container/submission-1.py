class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        maxAmount = 0
        while i < j:
            currentAmount = (j - i) * min(heights[i], heights[j])
            maxAmount = max(maxAmount, currentAmount)
            # always move the pointer pointing to the shorter line
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1

        return maxAmount
