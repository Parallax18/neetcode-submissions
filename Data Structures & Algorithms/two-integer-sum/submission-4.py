class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = 0
        indecies = []
        seen = {}
        in_seen = {}
        # current = ()

        for index, num in enumerate(nums):
            # difference = target - num
            if not num in seen:
                
                difference = target - num
                if difference in nums:
                    diff_index = nums.index(difference)
                    if diff_index != index:
                        seen[num] = index
                        seen[difference] = diff_index
                        indecies.extend([index, diff_index])
                    # print(f"{seen[num]}, {index}")
            
        # print(f"Seen: {seen}")
        print(f"Indecies: {sorted(indecies)}")
        return sorted(indecies)
        # for index, num in enumerate(nums):
        #     seen[index] = num
       
        # for index, num in seen.items():
        #     difference = target - num
        #     print(f"Num: {num} + {difference} = {target}")
        #     # print(f"Difference: {difference}")
        #     print(f"Index: {index}, Num: {num}")
        #     # if num == difference:
        #     in_seen[difference] = index
        #     print(f"In seen: {in_seen}")
        #     if difference in in_seen:
        #         print(f"{difference} : {index}")

        # for index, num in enumerate(nums):
        #     if num <= target:
        #         # current[0] = num
        #         difference = target - num
        #         if difference in nums:
        #             indexes.insert(0, index)

        #             diff_index = nums.index(difference)

        #             indexes.insert(1, diff_index)

        #             print("indexes", sorted(indexes))

        #             break
        # return sorted(indexes)
        