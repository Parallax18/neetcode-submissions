class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # unique = set()
        # for num in nums:
        #     unique.add(num)

        # return len(nums) > len(unique)   

        existing = {}
        for num in nums:
            if num in existing:
                return True
            else:
                existing[num] = num
        return False