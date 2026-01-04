# 347. Top K Frequent Elements

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2

# Output: [1,2]

# Example 2:

# Input: nums = [1], k = 1

# Output: [1]

# Example 3:

# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

# Output: [1,2]

 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
 

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.




from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency of each number
        freq = defaultdict(int)  # key = number, value = frequency
        for num in nums:
            freq[num] += 1

        # Step 2: Create buckets where index = frequency
        # Each bucket at index i will hold all numbers that appear i times
        buckets = [[] for _ in range(len(nums) + 1)]  # max frequency = len(nums)
        for num, count in freq.items():
            buckets[count].append(num)

        # Step 3: Collect top k frequent numbers
        res = []
        # Start from the bucket with highest frequency
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)  # add number to result
                if len(res) == k:  # stop once we have k elements
                    return res




# ✅ Key Notes for Revision:
    # Frequency counting → O(n)
    # Bucket creation → O(n)
    # Scanning buckets → O(n) in worst case
    # Overall complexity → O(n)
    # Space complexity → O(n) for freq + O(n) for buckets → O(n)





