# 11. Container With Most Water

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
 

# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104



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

