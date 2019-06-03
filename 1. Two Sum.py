class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_to_indices = {}
        index = 0
        for num in nums:
            needed_num = target - num
            if needed_num in nums_to_indices:
                return [nums_to_indices[needed_num], index]
            nums_to_indices[num] = index
            index += 1
