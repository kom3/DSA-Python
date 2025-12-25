# 1423. Maximum Points You Can Obtain from Cards

# There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

# In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

# Your score is the sum of the points of the cards you have taken.

# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

 

# Example 1:

# Input: cardPoints = [1,2,3,4,5,6,1], k = 3
# Output: 12
# Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
# Example 2:

# Input: cardPoints = [2,2,2], k = 2
# Output: 4
# Explanation: Regardless of which two cards you take, your score will always be 4.
# Example 3:

# Input: cardPoints = [9,7,7,9,7,7,9], k = 7
# Output: 55
# Explanation: You have to take all the cards. Your score is the sum of points of all cards.
 

# Constraints:

# 1 <= cardPoints.length <= 105
# 1 <= cardPoints[i] <= 104
# 1 <= k <= cardPoints.length





# Key Idea
# Instead of choosing k cards from the ends,
# find the minimum sum subarray of length n - k (cards left in the middle).




from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        n = len(cardPoints)
        
        # If we take all cards, no need to slide a window
        if k == n:
            return sum(cardPoints)

        total_sum = sum(cardPoints)

        # Window size represents cards we do NOT take
        window_size = n - k

        window_sum = 0              # current window sum
        min_window_sum = float("inf")  # track minimum leftover sum

        # 'i' acts as the right pointer of the window
        for i in range(n):
            # Expand the window by adding the right element
            window_sum += cardPoints[i]

            # Once we have exactly 'window_size' elements,
            # start processing the window
            if i >= window_size - 1:
                # Update minimum sum of leftover cards
                min_window_sum = min(min_window_sum, window_sum)

                # Shrink window from the left for next iteration
                window_sum -= cardPoints[i - (window_size - 1)]

        # Maximum score = total points - minimum leftover points
        return total_sum - min_window_sum


# ⏱️ Complexity
# Time: O(n)
# Space: O(1)


# One-Line Interview Explanation
# “I find the minimum sum subarray of length n - k using a fixed sliding window and subtract it from the total sum.”