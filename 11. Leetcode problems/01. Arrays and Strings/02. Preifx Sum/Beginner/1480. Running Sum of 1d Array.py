# 1480. Running Sum of 1d Array

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# Example 2:

# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
# Example 3:

# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]
 

# Constraints:

# 1 <= nums.length <= 1000
# -10^6 <= nums[i] <= 10^6






class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = [0] * len(nums)

        running_sum[0] = nums[0]
        for right in range(1, len(nums)):
            running_sum[right] = running_sum[right - 1] + nums[right]

        return running_sum



# Time Complexity:
#     Loop runs from 1 to n-1 → O(n)
#     Other operations are O(1)
#     ✅ Total: O(n)

#     Space Complexity:
#     You create a new array of the same length as nums → O(n)
#     ✅ Total: O(n)



# Optional tip: you could also do it in-place to save memory:
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for right in range(1, len(nums)):
            nums[right] += nums[right - 1]

        return nums
    



# Time Complexity:
    # Loop runs from 1 to n-1 → O(n)
    # ✅ Total: O(n)

# Space Complexity:
    # No extra array is created. Only modifying input → O(1)
    # ✅ Total: O(1)