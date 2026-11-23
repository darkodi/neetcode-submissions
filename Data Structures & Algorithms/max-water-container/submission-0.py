class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights)-1
        best = (j - i) * min(heights[i], heights[j])
        while i < j:
            if heights[i] <= heights[j]:
                i += 1
                if heights[i] > heights[i-1]:
                    best = max(best, (j - i) * min(heights[i], heights[j]))
            else:
                j -= 1
                if heights[j] > heights[j+1]:
                    best = max(best, (j - i) * min(heights[i], heights[j]))
        return best

            

