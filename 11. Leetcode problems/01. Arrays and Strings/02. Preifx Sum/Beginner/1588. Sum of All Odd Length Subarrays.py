# 1588. Sum of All Odd Length Subarrays

# Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

# A subarray is a contiguous subsequence of the array.

 

# Example 1:

# Input: arr = [1,4,2,5,3]
# Output: 58
# Explanation: The odd-length subarrays of arr and their sums are:
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
# Example 2:

# Input: arr = [1,2]
# Output: 3
# Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.
# Example 3:

# Input: arr = [10,11,12]
# Output: 66
 

# Constraints:

# 1 <= arr.length <= 100
# 1 <= arr[i] <= 1000
 

# Follow up:

# Could you solve this problem in O(n) time complexity?



# (brute-force)

from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        """
        Returns the sum of all subarrays of arr with odd length.
        """
        
        n = len(arr)
        total_sum = 0
        
        # Iterate over all possible subarray lengths (1, 3, 5, ...)
        for length in range(1, n + 1, 2):  # only odd lengths
            # Slide the window of size 'length' across the array
            for start in range(n - length + 1):
                # Sum the subarray arr[start:start+length] and add to total
                subarray_sum = sum(arr[start:start + length])
                total_sum += subarray_sum
                
        return total_sum


# Time Complexity
    # Outer loop → O(n) (for lengths)
    # Inner loop → O(n) (for starting indices)
    # Sum of subarray → O(length)
    # Total:O(n3)

# Space Complexity
#     Only a few variables → O(1)




# Using prefix sums for efficiency

from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        """
        Returns the sum of all subarrays of arr with odd length,
        using prefix sums for efficient computation.
        """
        
        n = len(arr)
        total_sum = 0
        
        # Step 1: Compute prefix sums
        # prefix[i] = sum of arr[0..i-1]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]
        
        # Step 2: Iterate over all odd-length subarrays
        for length in range(1, n + 1, 2):  # only odd lengths
            for start in range(n - length + 1):
                end = start + length
                # Sum of subarray arr[start:end] = prefix[end] - prefix[start]
                total_sum += prefix[end] - prefix[start]
        
        return total_sum
    


# | Aspect | Complexity |
# | ------ | ---------- |
# | Time   | O(n²)      |
# | Space  | O(n)       |






# Most optimized O(n) solution using a mathematical counting trick.

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total_sum = 0
        n = len(arr)

        for i in range(n):
            left = i + 1           # number of elements on the left including arr[i]
            right = n - i          # number of elements on the right including arr[i]

            # Count of odd/even elements on left
            left_odd = (left + 1) // 2
            left_even = left // 2

            # Count of odd/even elements on right
            right_odd = (right + 1) // 2
            right_even = right // 2

            # Total subarrays of odd length that include arr[i]
            total_sum += arr[i] * (left_odd * right_odd + left_even * right_even)

        return total_sum





# | Aspect | Complexity |
# | ------ | ---------- |
# | Time   | O(n)       |
# | Space  | O(1)       |



