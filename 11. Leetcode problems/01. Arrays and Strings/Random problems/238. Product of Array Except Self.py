# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)




# Brute force

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        for i in range(n):
            prod = 1
            for j in range(n):
                if i != j:
                    prod *= nums[j] 
            res.append(prod)
        return res
    

# Time complexity: O(n^2)
# Space complexity: O(n) Output list res stores n elements


# Using prefix prod and suffix prod technique




from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Returns an array where each element is the product of all other elements 
        in the input array 'nums', without using division.
        """
        
        # Initialize result array with 1s
        res = [1] * len(nums)

        # ------------------------
        # Step 1: Compute prefix products
        # ------------------------
        # prefix will store the product of all elements to the left of current index
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix       # store product of all elements before nums[i]
            prefix *= nums[i]     # update prefix for next iteration

        # ------------------------
        # Step 2: Compute suffix products
        # ------------------------
        # suffix will store the product of all elements to the right of current index
        suffix = 1
        for j in range(len(nums) - 1, -1, -1):
            res[j] *= suffix      # multiply by product of all elements after nums[j]
            suffix *= nums[j]     # update suffix for next iteration

        return res


# O(n) time, O(1) extra space (excluding output array res).



















# Another solution using math

import math
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zero_count = nums.count(0)
        
        # Case 1: More than one zero → all products are 0
        if zero_count > 1:
            return [0] * n
        
        # Case 2: Exactly one zero
        if zero_count == 1:
            zero_index = nums.index(0)
            # Product of all non-zero numbers
            total = math.prod(num for num in nums if num != 0)
            return [0]*zero_index + [total] + [0]*(n - zero_index - 1)
        
        # Case 3: No zeros → divide total product by each number
        total = math.prod(nums)
        return [total // num for num in nums]  # safe for integers


# Note:
# Uses division, so it doesn’t follow the “no division” constraint in some interview versions.

# | Measure   | Complexity |
# | --------- | ---------- |
# | **Time**  | O(n)       |
# | **Space** | O(n)       |








