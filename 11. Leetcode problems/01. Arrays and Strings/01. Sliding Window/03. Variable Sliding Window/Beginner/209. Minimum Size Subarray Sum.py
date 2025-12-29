# 209. Minimum Size Subarray Sum

# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
 

# Constraints:

# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104
 

# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Initialize minimum length to infinity (we haven't found any valid subarray yet)
        min_len = float('inf')
        
        # Current sum of the sliding window
        sum = 0
        
        # Left pointer of the sliding window
        left = 0

        # Right pointer moves through the array
        for right in range(len(nums)):
            # Add the current number to the window sum
            sum += nums[right]

            # While the current window sum is at least the target
            # try to shrink the window from the left to find the smallest length
            while sum >= target:
                # Update the minimum length if the current window is smaller
                min_len = min(min_len, right - left + 1)
                
                # Remove the leftmost element from the window sum
                sum -= nums[left]
                
                # Move the left pointer to the right, shrinking the window
                left += 1
        
        # If min_len was never updated, no subarray meets the target, return 0
        if min_len == float('inf'):
            return 0
        else:
            # Otherwise, return the smallest length found
            return min_len
        

# Time Complexity
    # The outer loop goes through each element once (right pointer moves from 0 to n-1) → O(n).
    # The inner while loop moves the left pointer at most n times in total because each element can only be removed once.
    # So, the total time complexity is: O(n)+O(n)=O(n)

# Space Complexity
    # You are using a few variables: min_len, sum, left, right.
    # No extra arrays or data structures are used.
    # ✅ Space Complexity: O(1) (constant space)





# Another solution of which the time complexity is O(n log(n)), this approach uses prefix sums + binary search

from bisect import bisect_left
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        # Build prefix sum array
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]

        min_len = float('inf')

        # For each starting index, use binary search to find the end index
        for i in range(n):
            required_sum = target + prefix[i]
            # Find the smallest j such that prefix[j] >= required_sum
            j = bisect_left(prefix, required_sum)
            if j <= n:
                min_len = min(min_len, j - i)

        return 0 if min_len == float('inf') else min_len



# Complexities
# Time Complexity:
    # Building prefix sum → O(n)
    # Loop over n elements, each doing a binary search → O(n log n)
    # ✅ Total: O(n log n)

# Space Complexity:
    # Prefix sum array of size n+1 → O(n)
