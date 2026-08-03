class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        more_than_half = (len(nums)//2)
        seen = {}
        for index, num in enumerate(nums):
            seen[num] = 1 + seen.get(num, 0)
            print(seen, more_than_half)
            if seen[num] > more_than_half:
                return num
            # if num in seen:
            #     seen[num] += 1
            #     if seen[num] >= more_than_half:
            #         return num
            # else:
            #     seen[num] = 1
        print(seen, more_than_half)