# 1248. Count Number of Nice Subarrays

# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

# Return the number of nice sub-arrays.

 

# Example 1:

# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
# Example 2:

# Input: nums = [2,4,6], k = 1
# Output: 0
# Explanation: There are no odd numbers in the array.
# Example 3:

# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# Output: 16
 

# Constraints:

# 1 <= nums.length <= 50000
# 1 <= nums[i] <= 10^5
# 1 <= k <= nums.length


# This problem is also under variable sliding window/hard, means it can solved using both sliding window(works with only positive numbers) and the prefix sum(works sub arrays with both positive & negative numbers)




from collections import defaultdict
from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
        Count the number of "nice" subarrays with exactly k odd numbers.
        """
        # Initialize result
        total_nice_array_count = 0
        
        # Map to store frequency of prefix odd counts
        odd_count_map = defaultdict(int)
        
        # There is 1 way to have 0 odd numbers before starting
        odd_count_map[0] = 1
        
        # Current count of odd numbers seen so far
        odd_count = 0
        
        # Traverse the array
        for num in nums:
            # Increment odd_count if current number is odd
            odd_count += num % 2
            
            # If there was a prefix with (odd_count - k) odd numbers,
            # it forms a nice subarray ending at current index
            total_nice_array_count += odd_count_map[odd_count - k]
            
            # Update the map with current odd_count
            odd_count_map[odd_count] += 1
        
        return total_nice_array_count





# | Complexity | Value |
# | ---------- | ----- |
# | Time       | O(n)  |
# | Space      | O(n)  |





