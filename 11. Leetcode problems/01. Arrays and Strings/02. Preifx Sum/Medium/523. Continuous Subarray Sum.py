# 523. Continuous Subarray Sum

# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

# A good subarray is a subarray where:

# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.
# Note that:

# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
 

# Example 1:

# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
# Example 2:

# Input: nums = [23,2,6,4,7], k = 6
# Output: true
# Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
# 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
# Example 3:

# Input: nums = [23,2,6,4,7], k = 13
# Output: false
 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109
# 0 <= sum(nums[i]) <= 231 - 1
# 1 <= k <= 231 - 1




from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        Returns True if the array has a continuous subarray of size at least 2
        whose sum is a multiple of k.
        """
        
        # Map to store first occurrence of each remainder
        # Initialize with 0 mapped to -1 to handle subarrays starting at index 0
        remainder_index_map = {0: -1}
        
        prefix_sum = 0  # Running sum of elements
        
        for i, num in enumerate(nums):
            prefix_sum += num  # Add current number to running sum
            
            # Only take modulo if k is not zero
            if k != 0:
                prefix_sum %= k
            
            # Check if this remainder has been seen before
            if prefix_sum in remainder_index_map:
                # Subarray length = current index - previous index of same remainder
                if i - remainder_index_map[prefix_sum] >= 2:
                    return True  # Found valid subarray
            else:
                # Store the first occurrence of this remainder
                remainder_index_map[prefix_sum] = i
        
        return False  # No valid subarray found





# ✅ Key Points in the Code
#     Prefix sum modulo k: Helps reduce the problem to checking if two prefix sums have the same remainder.
#     Map stores first occurrence: Ensures we always get the longest possible subarray starting after that index.
#     Length check >= 2: Ensures subarrays are at least size 2.
#     Handle k == 0: Avoid division/modulo by zero errors.




# | Complexity | Value        |
# | ---------- | ------------ |
# | Time       | O(n)         |
# | Space      | O(min(n, k)) |
