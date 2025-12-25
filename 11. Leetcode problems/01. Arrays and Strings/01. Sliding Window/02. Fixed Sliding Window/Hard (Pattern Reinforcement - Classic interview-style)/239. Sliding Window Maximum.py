# 239. Sliding Window Maximum

# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

 

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length




from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # --------------------------------------------------
        # EDGE CASE:
        # If window size is larger than the array,
        # no valid sliding window exists.
        # --------------------------------------------------
        if len(nums) < k:
            return []

        # --------------------------------------------------
        # Deque (Double Ended Queue) used as a MONOTONIC QUEUE
        #
        # It stores INDICES (not values) of elements
        # The values corresponding to these indices are kept
        # in DECREASING order.
        #
        # Front of deque -> index of maximum element
        # --------------------------------------------------
        dq = deque()

        # Result array to store the maximum of each window
        result = []

        # --------------------------------------------------
        # Iterate through all elements
        # --------------------------------------------------
        for i in range(len(nums)):

            # --------------------------------------------------
            # STEP 1: Maintain monotonic decreasing order
            #
            # Remove indices from the back of the deque
            # whose values are <= current element,
            # since they can NEVER be the maximum again.
            # --------------------------------------------------
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            # --------------------------------------------------
            # STEP 2: Add current index to the deque
            # --------------------------------------------------
            dq.append(i)

            # --------------------------------------------------
            # STEP 3: Remove indices that are OUTSIDE
            # the current window
            #
            # Current window range:
            # [i - (k - 1), i]
            # --------------------------------------------------
            if dq[0] < i - (k - 1):
                dq.popleft()

            # --------------------------------------------------
            # STEP 4: Once the first window is complete
            # (i >= k - 1), record the maximum
            #
            # The front of the deque always stores the
            # index of the maximum element of the window
            # --------------------------------------------------
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result


# Notes:
# What “monotonic queue” means: Values in the deque are always in decreasing order

# ⏱️ Time & Space Complexity (Revision Friendly)
# Time	O(n) (each element added & removed once in a window)
# Space	O(k) (deque stores at most k indices)