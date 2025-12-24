# 1984. Minimum Difference Between Highest and Lowest of K Scores

# You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.

# Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.

# Return the minimum possible difference.

 

# Example 1:

# Input: nums = [90], k = 1
# Output: 0
# Explanation: There is one way to pick score(s) of one student:
# - [90]. The difference between the highest and lowest score is 90 - 90 = 0.
# The minimum possible difference is 0.
# Example 2:

# Input: nums = [9,4,1,7], k = 2
# Output: 2
# Explanation: There are six ways to pick score(s) of two students:
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
# - [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
# - [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
# - [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
# The minimum possible difference is 2.
 

# Constraints:

# 1 <= k <= nums.length <= 1000
# 0 <= nums[i] <= 105



# Pattern: Sort + Fixed Sliding Window (Range Minimization)


class Solution:
    def minimumDifference(self, nums, k):
        # If we pick only 1 student, difference is always 0
        if k == 1:
            return 0
        
        nums.sort()
        min_diff = float("inf")

        # Sliding window of size k
        # wrapping k-1 within () for understanding purposes, we always use (k-1) to add to index to find the last(right most) element and subract the array lenght to get the ith valid window position.
        for i in range(len(nums) - (k - 1)): # carefully notice the upperbound(it's different from problem: 1343), memorize the way pointer 'i' moves. 'i' will become a left pointer
            lowest_score_in_window = nums[i]
            highest_score_in_window = nums[i + (k - 1)]
            diff = highest_score_in_window - lowest_score_in_window
            min_diff = min(min_diff, diff)

        return min_diff


# call the function to test the result

nums = [9,4,1,7]; k = 2

s = Solution()
min_diff = s.minimumDifference(nums, k)
print(f"Min diff is {min_diff}")
# Output: Min diff is 2


# Hint
# It sounds like a non contiguous problem, but sorting will totally change it to contiguous(since order is not important in this problem), and sliding window only works with contiguous problems.