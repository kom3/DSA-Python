# 42. Trapping Rain Water

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9
 

# Constraints:

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105


class Solution:
    def trap(self, height: List[int]) -> int:
        # Two pointers
        left, right = 0, len(height) - 1

        # Maximum height seen so far from each side
        left_max = 0
        right_max = 0

        # Total trapped water
        total = 0

        # Process until pointers meet
        while left < right:
            # The smaller side determines the water level
            if height[left] < height[right]:
                # Update max on the left
                left_max = max(left_max, height[left])

                # Water trapped at current left index
                total += left_max - height[left]

                # Move left pointer
                left += 1
            else:
                # Update max on the right
                right_max = max(right_max, height[right])

                # Water trapped at current right index
                total += right_max - height[right]

                # Move right pointer
                right -= 1

        return total





# One-line intuition (great for revision)
# Always move the pointer with the smaller height, because that side limits how much water can be trapped.

# Complexity
# Time: O(n)
# Space: O(1)