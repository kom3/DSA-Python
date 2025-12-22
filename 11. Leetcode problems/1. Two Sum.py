class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # solution1 brute force O(n2)
        # if len(nums) == 2:
        #     return [0,1]
        # for i in range(0, len(nums)):
        #     for j in range(i+1, len(nums)):
        #         sum = nums[i] + nums[j]
        #         if sum == target:
        #             return [i, j]

        # solution2 Efficient method, O(n)
        # seen = {}
        # for i in range(0, len(nums)):
        #     diff = target - nums[i]
        #     if diff in seen:
        #         return [seen[diff], i]
        #     seen[nums[i]] = i

        # solution3 Efficient method, O(n)
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i

        