# 219. Contains Duplicate II

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# 0 <= k <= 105



from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Dictionary to store the last index where each number was seen
        indices_map = {}

        # Iterate through the array
        for current_index, num in enumerate(nums):
            # If the number has been seen before
            # and the distance between indices is <= k, return True
            if num in indices_map and current_index - indices_map[num] <= k:
                return True

            # Update the last seen index of the current number
            indices_map[num] = current_index

        # If no nearby duplicate was found, return False
        return False



# 1. Time Complexity: O(n)
# 2. Space Complexity: O(n)

