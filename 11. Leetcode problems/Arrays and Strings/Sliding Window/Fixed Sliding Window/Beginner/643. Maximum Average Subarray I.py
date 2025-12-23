# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000
 

# Constraints:

# n == nums.length
# 1 <= k <= n <= 105
# -104 <= nums[i] <= 104


# Pattern: Fixed Sliding Window + Running Sum / Average

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = float(-inf)
        window_sum = 0

        for i in range(len(nums)):    # carefully notice the upperbound(it's different from problem: 1984), memorize the way pointer 'i' moves. 'i' will become a right pointer
            window_sum += nums[i]

            if i >= k - 1:
                max_sum = max(max_sum, window_sum)
                window_sum -= nums[i - (k - 1)]
        return max_sum/k