# 128. Longest Consecutive Sequence

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:

# Input: nums = [1,0,1,2]
# Output: 3
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109


from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Finds the length of the longest consecutive elements sequence in an array.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        
        # Step 1: Put all numbers in a set for O(1) lookup
        num_set = set(nums)
        max_len = 0  # to keep track of the longest consecutive sequence found
        
        # Step 2: Iterate through each number in the set
        for num in num_set:
            
            # Step 3: Only start a sequence if 'num' is the start of a sequence
            # i.e., num-1 is NOT in the set
            if num - 1 not in num_set:
                current_num = num       # start of the current sequence
                current_len = 1         # current sequence length
                
                # Step 4: Count consecutive numbers in the sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_len += 1
                
                # Step 5: Update maximum length if current sequence is longer
                max_len = max(max_len, current_len)
        
        # Step 6: Return the length of the longest consecutive sequence
        return max_len

# Example usage:
sol = Solution()
nums = [100, 4, 200, 1, 3, 2]
print(sol.longestConsecutive(nums))  # Output: 4






# | Aspect | Complexity | Reason                                     |
# | ------ | ---------- | ------------------------------------------ |
# | Time   | O(n)       | Each number is checked at most twice.      |
# | Space  | O(n)       | The set stores all numbers from the array. |
