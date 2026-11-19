class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         # 1. Count the frequency of each element
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        # 2. Create freq array where index is frequency and value is list of numbers with that frequency
        freq_array = [[] for _ in range(len(nums) + 1)] # + 1 because frequency can be at most len(nums)
        for num, freq in freq_map.items(): 
            freq_array[freq].append(num)
        # 3. Collect the top k frequent elements
        result = []
        for i in range(len(freq_array)-1, 0, -1):
            for num in freq_array[i]: # freq_array[i] contains a LIST of numbers with frequency i
                result.append(num)
                if len(result) == k:
                    return result
        return result
        