# 1004. Max Consecutive Ones III

# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length





from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Number of zeros currently inside the window
        zero_count = 0

        # Left pointer of the sliding window
        left = 0

        # Maximum length of a valid window found so far
        max_len = 0

        # Expand the window using the right pointer
        for right in range(len(nums)):

            # Include the current element
            if nums[right] == 0:
                zero_count += 1

            # If we exceed allowed zero flips, shrink the window
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Update the maximum window length
            max_len = max(max_len, right - left + 1)

        return max_len


# ⏱ Complexity

# Time: O(n)

# Space: O(1)