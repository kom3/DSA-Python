# 930. Binary Subarrays With Sum

# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

# A subarray is a contiguous part of the array.

 

# Example 1:

# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# Example 2:

# Input: nums = [0,0,0,0,0], goal = 0
# Output: 15
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# nums[i] is either 0 or 1.
# 0 <= goal <= nums.length





class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
        Count the number of subarrays with sum equal to `goal`.
        Uses the prefix sum + hashmap pattern.

        Pattern formula:
            prefix_sum[i] - prefix_sum[j] = goal
            => If prefix_sum[j] = prefix_sum[i] - goal, subarray (j+1 ... i) has sum = goal
        """

        # prefix_sum: running sum of nums[0..i]
        prefix_sum = 0

        # count: total number of subarrays with sum == goal
        count = 0

        # freq maps each prefix_sum value to how many times it has occurred
        # Initialize freq[0] = 1 to handle subarrays starting from index 0
        freq = {0: 1}

        for num in nums:
            # Update prefix sum
            prefix_sum += num

            # Calculate the required prefix sum to form a subarray with sum = goal
            required = prefix_sum - goal

            # If required prefix sum exists, add its frequency to the count
            if required in freq:
                count += freq[required]

            # Update frequency of current prefix_sum
            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

        return count



# 🧠 Pattern Memory Hook

# Formula:
    # prefix_sum[i] - prefix_sum[j] = goal
    # → j = index where prefix_sum[j] = prefix_sum[i] - goal
    # → length of subarray = i - j


# freq hashmap stores prefix_sum[j] → occurrences
# so you can count all valid j’s for each i in O(1).

# Works for binary arrays, but can generalize to arbitrary arrays for sum = k.


# | Resource | Complexity | Reason                                     |
# | -------- | ---------- | ------------------------------------------ |
# | Time     | O(n)       | Single pass + O(1) hash lookup per element |
# | Space    | O(n)       | Stores prefix sums in hashmap              |


