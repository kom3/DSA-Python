# 992. Subarrays with K Different Integers

# Given an integer array nums and an integer k, return the number of good subarrays of nums.

# A good array is an array where the number of different integers in that array is exactly k.

# For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
# A subarray is a contiguous part of an array.

 

# Example 1:

# Input: nums = [1,2,1,2,3], k = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
# Example 2:

# Input: nums = [1,2,1,3,4], k = 3
# Output: 3
# Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# 1 <= nums[i], k <= nums.length


from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        # Helper function to count subarrays with at most k distinct integers
        def atMostK(k: int) -> int:
            freq = {}       # Frequency map of numbers in the window
            left = 0        # Left pointer of sliding window
            count = 0       # Total valid subarrays

            for right in range(len(nums)):
                # Add current number to the window
                freq[nums[right]] = freq.get(nums[right], 0) + 1

                # Shrink window if distinct count exceeds k
                while len(freq) > k:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        del freq[nums[left]]
                    left += 1

                # All subarrays ending at 'right' are valid
                count += right - left + 1

            return count

        # Exactly K = At Most K - At Most (K - 1)
        return atMostK(k) - atMostK(k - 1)



# Why right - left + 1 Works
    # At each right index:
    # The window [left ... right] is valid
    # Every start index between left and right forms a valid subarray
    # That gives right - left + 1 subarrays

# ⏱ Complexity
    # Time: O(n)
    # Space: O(k)

# 🔗 Pattern Connections
    # This same idea applies to:
    # LC 992 – Subarrays with K Different Integers
    # Exactly K distinct characters
    # Exactly K unique elements in subarray

# ❝If the problem says EXACTLY K, think At Most K − At Most (K − 1)❞







# This can be solved using two pointer technique as well, but for interviews perfer the above sliding window solution

from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        freq = [0] * (len(nums) + 1)   # Frequency of numbers in current window

        total_subarrays = 0            # Final result

        left_big = 0                   # Left boundary of the largest valid window
        left_small = 0                 # Left boundary of the smallest valid window

        remaining_distinct = k         # How many new distinct numbers we can still add

        for right in range(len(nums)):
            num = nums[right]

            # Add current number to the window
            freq[num] += 1

            # If this is a new distinct number
            if freq[num] == 1:
                remaining_distinct -= 1

                # Too many distinct numbers → reset window
                if remaining_distinct < 0:
                    # Remove everything before left_small
                    freq[nums[left_small]] = 0
                    left_small += 1
                    left_big = left_small
                    remaining_distinct = 0

            # If window contains exactly k distinct numbers
            if remaining_distinct == 0:
                # Shrink the small window to remove duplicates
                while freq[nums[left_small]] > 1:
                    freq[nums[left_small]] -= 1
                    left_small += 1

                # Count all valid subarrays ending at 'right'
                total_subarrays += left_small - left_big + 1

        return total_subarrays
