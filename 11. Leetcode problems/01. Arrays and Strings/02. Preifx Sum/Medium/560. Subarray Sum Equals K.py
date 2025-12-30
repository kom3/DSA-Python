# 560. Subarray Sum Equals K

# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107





from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Returns the number of continuous subarrays whose sum equals k.
        Uses prefix sum + hashmap technique.
        """
        
        # Dictionary to store counts of prefix sums seen so far
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1  # Base case: prefix sum of 0 occurs once
        
        prefix_sum = 0  # Running sum of elements
        total_count = 0  # Total number of subarrays with sum = k
        
        for num in nums:
            # Update the running prefix sum
            prefix_sum += num
            
            # If (prefix_sum - k) exists in prefix_counts,
            # it means there is a subarray ending at current index with sum = k
            total_count += prefix_counts.get(prefix_sum - k, 0)
            
            # Record the current prefix sum in the map
            prefix_counts[prefix_sum] += 1
            
        return total_count





# Time Complexity
    # Loop through nums → O(n)
    # We visit each element exactly once.
    # Dictionary operations (get and +=) → O(1) on average
    # HashMap lookup and update are average-case constant time.
    # ✅ Total Time Complexity: O(n)

# Space Complexity
    # prefix_counts dictionary stores prefix sums seen so far.
    # In the worst case, each prefix sum is unique → up to n+1 entries.
    # ✅ Total Space Complexity: O(n)

# Key Revision Points
    # prefix_sum keeps a running total of the array so far.
    # prefix_sum - k checks if there’s a previous sum that allows a subarray to equal k.
    # HashMap (prefix_counts) stores counts, not just existence.
    # Initialize prefix_counts[0] = 1 to handle subarrays starting at index 0.