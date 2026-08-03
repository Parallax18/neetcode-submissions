class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        more_than_half = (len(nums)//2)
        seen = {}
        for index, num in enumerate(nums):
            seen[num] = 1 + seen.get(num, 0)
            if seen[num] > more_than_half:
                return num
         