class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = 0
        indecies = []
        seen = {}

        for index, num in enumerate(nums):
            if not num in seen:
                difference = target - num
                if difference in nums:
                    diff_index = nums.index(difference)
                    if diff_index != index:
                        seen[num] = index
                        seen[difference] = diff_index
                        indecies.extend([index, diff_index])
        return sorted(indecies)
       
        