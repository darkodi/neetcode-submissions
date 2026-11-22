class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
         # TWO POINTERS
        left, right = 0, len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target: # try with a bigger number
                left += 1
            else: # try with a smaller number
                right -= 1
        return [] # no solution found