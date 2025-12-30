# 303. Range Sum Query - Immutable

# Given an integer array nums, handle multiple queries of the following type:

# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

# Example 1:

# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]

# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
# numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
# numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
 

# Constraints:

# 1 <= nums.length <= 104
# -105 <= nums[i] <= 105
# 0 <= left <= right < nums.length
# At most 104 calls will be made to sumRange.





from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        """
        Initialize the NumArray object with the given list of integers.
        We precompute the prefix sum array to answer sumRange queries in O(1) time.
        """
        # Make a copy of nums to store prefix sums
        self.prefix_sum = nums[:]
        self.calc_prefix_sum()

    def calc_prefix_sum(self):
        """
        Convert self.prefix_sum into a prefix sum array.
        After this, prefix_sum[i] = sum of nums[0] to nums[i].
        """
        for i in range(1, len(self.prefix_sum)):
            self.prefix_sum[i] += self.prefix_sum[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        """
        Return the sum of elements nums[left] to nums[right], inclusive.
        """
        # If left is 0, the sum is just prefix_sum[right]
        if left == 0:
            return self.prefix_sum[right]
        # Otherwise, subtract prefix_sum[left - 1] to get the sum in range
        return self.prefix_sum[right] - self.prefix_sum[left - 1]


# Example usage:
# obj = NumArray([1, 2, 3, 4])
# param_1 = obj.sumRange(1, 3)  # Should return 2+3+4 = 9



# | Operation      | Time Complexity | Space Complexity |
# | -------------- | --------------- | ---------------- |
# | Initialization | O(n)            | O(n)             |
# | sumRange query | O(1)            | O(1)             |





# ✅ Key points to remember for revision:
    # Prefix sum array allows O(1) range sum queries after O(n) preprocessing.
    # prefix_sum[i] stores sum from index 0 to i.
    # sumRange(left, right) is:
    # prefix_sum[right] if left == 0
    # prefix_sum[right] - prefix_sum[left - 1] otherwise