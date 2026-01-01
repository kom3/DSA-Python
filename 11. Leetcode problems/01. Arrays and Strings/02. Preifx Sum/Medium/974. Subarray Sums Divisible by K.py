# 974. Subarray Sums Divisible by K

# Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

# A subarray is a contiguous part of an array.

 

# Example 1:

# Input: nums = [4,5,0,-2,-3,1], k = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by k = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
# Example 2:

# Input: nums = [5], k = 9
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -104 <= nums[i] <= 104
# 2 <= k <= 104




class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """
        Count the number of subarrays divisible by k.
        Pattern formula: i - j = length
        Subarray [j+1 ... i] is divisible by k if:
            prefix[i] % k == prefix[j] % k
        """

        # frequency map for prefix_sum % k
        remainder_freq = {0: 1}  # remainder 0 seen once (empty prefix)
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num

            # calculate normalized remainder
            # why normalized reminder?
            # In Python: -1 % 5  # → 4 So it’s usually safe. But in general, for clarity and safety, it’s best to normalize the remainder.
            # In other languages like C++ or Java, modulo with negative numbers works differently:
            # -1 % 5  // → -1 in C++
            # -2 % 5  → -2
            rem = (prefix_sum % k + k) % k  # handles negative numbers

            # add count of previous subarrays with same remainder
            count += remainder_freq.get(rem, 0)

            # update remainder frequency
            remainder_freq[rem] = remainder_freq.get(rem, 0) + 1

        return count



