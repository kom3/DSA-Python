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
    def maxArea(self, heights: List[int]) -> int:
        # Two pointers at both ends
        left, right = 0, len(heights) - 1

        # Maximum area found so far
        max_area = 0

        # Continue until pointers meet
        while left < right:
            # Width between the two lines
            width = right - left

            # Height is limited by the shorter line
            height = min(heights[left], heights[right])

            # Area formed by current pair
            max_area = max(max_area, width * height)

            # Move the pointer at the shorter line
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area



# One-line revision intuition

# Area is limited by the shorter line, so move the pointer at the smaller height.

# Time Complexity: O(n)
# Space Complexity: O(1)


