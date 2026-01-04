# 220. Contains Duplicate III

# You are given an integer array nums and two integers indexDiff and valueDiff.

# Find a pair of indices (i, j) such that:

# i != j,
# abs(i - j) <= indexDiff.
# abs(nums[i] - nums[j]) <= valueDiff, and
# Return true if such pair exists or false otherwise.

 

# Example 1:

# Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
# Output: true
# Explanation: We can choose (i, j) = (0, 3).
# We satisfy the three conditions:
# i != j --> 0 != 3
# abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
# abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0
# Example 2:

# Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
# Output: false
# Explanation: After trying all the possible pairs (i, j), we cannot satisfy the three conditions, so we return false.
 

# Constraints:

# 2 <= nums.length <= 105
# -109 <= nums[i] <= 109
# 1 <= indexDiff <= nums.length
# 0 <= valueDiff <= 109


from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: List[int], indexDiff: int, valueDiff: int
    ) -> bool:

        # Edge case: valueDiff < 0 makes the condition impossible
        if valueDiff < 0:
            return False

        # Dictionary to store buckets:
        # key   -> bucket id
        # value -> number in that bucket
        buckets = {}

        # Bucket size is valueDiff + 1
        # This guarantees that two numbers in the same bucket
        # differ by at most valueDiff
        bucket_size = valueDiff + 1

        for i, num in enumerate(nums):

            # Compute bucket ID
            # Using floor division to correctly handle negative numbers
            bucket_id = num // bucket_size

            # 1️⃣ Check same bucket
            if bucket_id in buckets:
                return True

            # 2️⃣ Check neighboring buckets
            if (bucket_id - 1 in buckets and
                abs(num - buckets[bucket_id - 1]) <= valueDiff):
                return True

            if (bucket_id + 1 in buckets and
                abs(num - buckets[bucket_id + 1]) <= valueDiff):
                return True

            # Insert current number into its bucket
            buckets[bucket_id] = num

            # Maintain sliding window of size indexDiff
            # Remove the element that is too far away in index
            if i >= indexDiff:
                old_bucket_id = nums[i - indexDiff] // bucket_size
                del buckets[old_bucket_id]

        return False





# ⏱ Complexity
# Time: O(n)
# Space: O(indexDiff)


# 🔑 Mental model to remember
# Indices → sliding window
# Values → buckets



