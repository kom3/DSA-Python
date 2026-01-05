# 15. 3Sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105





class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Step 1: Sort the array to use two-pointer approach
        nums.sort()
        res = []

        # Step 2: Iterate through the array, stopping 2 elements before the end
        for i in range(len(nums) - 2):
            # Skip duplicates for the first element to avoid repeated triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Initialize two pointers for the remaining part of the array
            left, right = i + 1, len(nums) - 1

            # Step 3: Two-pointer scan for pairs that sum with nums[i] to zero
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                if curr_sum == 0:
                    # Found a valid triplet
                    res.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after processing duplicates
                    left += 1
                    right -= 1

                # If sum is too small, move left pointer to increase sum
                elif curr_sum < 0:
                    left += 1

                # If sum is too large, move right pointer to decrease sum
                else:
                    right -= 1

        return res





# ⏱ Complexity
# Time: O(n²) (outer loop × two-pointer scan)
# Space: O(1) extra (excluding output)