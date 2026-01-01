# 525. Contiguous Array

# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

# Example 1:

# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
# Example 2:

# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Example 3:

# Input: nums = [0,1,1,1,1,1,0,0,0]
# Output: 6
# Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.




class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # max_len stores the length k of the longest valid subarray
        max_len = 0

        # prefix_sum:
        #   +1 for every 1
        #   -1 for every 0
        prefix_sum = 0

        # seen[prefix_sum] = earliest index j where this prefix_sum occurred
        # Initialize with prefix_sum = 0 at index -1
        # (helps handle subarrays starting from index 0)
        seen = {0: -1}

        for i, num in enumerate(nums):
            # Build prefix sum
            if num == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1

            # ---- Key Formula Reference ----
            # For a subarray (j + 1) to i:
            #   prefix_sum[i] - prefix_sum[j] = 0
            # ⇒ prefix_sum[i] = prefix_sum[j]
            #
            # Length of subarray:
            #   k = i - j
            #
            # This matches the pattern:
            #   i - j = k
            # --------------------------------

            if prefix_sum in seen:
                # j = seen[prefix_sum]
                # k = i - j
                max_len = max(max_len, i - seen[prefix_sum])
            else:
                # Store the first (earliest) index j only
                # to maximize i - j
                seen[prefix_sum] = i

        return max_len




# | Resource | Complexity | Explanation                                    |
# | -------- | ---------- | ---------------------------------------------- |
# | Time     | O(n)       | Single pass + O(1) dict operations per element |
# | Space    | O(n)       | Dictionary stores up to n+1 prefix sums        |

