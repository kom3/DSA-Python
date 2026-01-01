# 363. Max Sum of Rectangle No Larger Than K


# Given an m x n matrix matrix and an integer k, return the max sum of a rectangle in the matrix such that its sum is no larger than k.

# It is guaranteed that there will be a rectangle with a sum no larger than k.

# Example 1:
# Input: matrix = [[1,0,1],[0,-2,3]], k = 2
# Output: 2
# Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the max number no larger than k (k = 2).

# Example 2:
# Input: matrix = [[2,2,-1]], k = 3
# Output: 3
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -100 <= matrix[i][j] <= 100
# -105 <= k <= 105
 

# Follow up: What if the number of rows is much larger than the number of columns?


import bisect
from typing import List

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """
        Finds the maximum sum of a rectangle in the matrix
        such that the sum is no larger than k.
        
        Approach:
        1. Precompute row-wise prefix sums to quickly get the sum
           of any row segment.
        2. Iterate over all pairs of columns (c1, c2) to define
           the left and right boundaries of the rectangle.
        3. For each column pair, compress the rows into a 1D array
           representing the sum of elements between c1 and c2 for each row.
        4. Use prefix sums + binary search (bisect) to find the maximum
           subarray sum ≤ k efficiently.
        """

        rows, cols = len(matrix), len(matrix[0])
        max_sum = float('-inf')

        # Step 0: Precompute row-wise prefix sums
        for r in range(rows):
            for c in range(1, cols):
                matrix[r][c] += matrix[r][c - 1]

        # Step 1: Iterate over all pairs of columns
        for c1 in range(cols):
            for c2 in range(c1, cols):
                prefix_sum = 0
                prefix_sums_list = [0]  # Stores previous prefix sums in sorted order

                # Step 2: Compress rows into a 1D array for this column segment
                for r in range(rows):
                    # Sum of row r between columns c1 and c2
                    row_sum = matrix[r][c2] - (matrix[r][c1 - 1] if c1 > 0 else 0)
                    
                    # Running prefix sum of the compressed 1D array
                    prefix_sum += row_sum

                    # Step 3: Binary search for the smallest prefix_sum >= prefix_sum - k
                    target = prefix_sum - k
                    idx = bisect.bisect_left(prefix_sums_list, target)

                    # Update max_sum if a valid previous prefix_sum is found
                    if idx < len(prefix_sums_list):
                        max_sum = max(max_sum, prefix_sum - prefix_sums_list[idx])

                    # Step 4: Insert current prefix_sum into the sorted list
                    bisect.insort(prefix_sums_list, prefix_sum)

        return max_sum

# Example usage:
matrix = [
    [1, 0, 1],
    [0, -2, 3]
]
k = 2
solution = Solution()
print(solution.maxSumSubmatrix(matrix, k))  # Output: 2





# ✅ Key points to remember for revision:

# Row-wise prefix sums:
    # matrix[r][c] = sum(matrix[r][0..c]) → lets you get any row segment in O(1).

# Column pairs (c1, c2):
    # Reduces the 2D problem to a 1D maximum subarray problem for each column segment.

# 1D max subarray ≤ k:
    # Keep running prefix sums.
    # Use a sorted list + binary search (bisect_left) to efficiently find the closest previous prefix sum that keeps the subarray ≤ k.

# Important formula:
    # subarray_sum = prefix_sum - prefix_sums_list[idx]
    # prefix_sums_list[idx] is the closest previous prefix sum ≥ prefix_sum - k.
    # This gives the largest subarray sum ≤ k.

# Time complexity:
    # O(cols² * rows * log(rows)) — efficient for moderate matrices.






# -----------------------------------------------------------------------------------------------


# 1️⃣ In the above approach

# Right now, we do:

    # for c1 in range(cols):
    #     for c2 in range(c1, cols):
    #         ...


# For each column pair, we process all rows with a prefix sum + binary search.

# Time complexity: O(cols^2 * rows * log(rows)) ✅ fine if cols is small, rows is moderate.

# 2️⃣ If rows > columns

    # Suppose:

    # rows = 10,000

    # cols = 10

    # Then cols^2 * rows * log(rows) ≈ 10^2 * 10^4 * log(10^4) ≈ a few million → still doable.

    # But if rows were even bigger, it might be slow.

    # 3️⃣ Optimization idea

    # We swap the roles of rows and columns:

    # Instead of iterating over column pairs, iterate over row pairs.

    # For each row pair, compress columns into a 1D array and apply the same max subarray ≤ k logic.



import bisect
from typing import List

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """
        Finds the maximum sum of a rectangle in the matrix
        such that the sum is no larger than k.

        Optimized to handle tall or wide matrices:
        - Always iterate over the smaller dimension to reduce complexity.
        """

        rows, cols = len(matrix), len(matrix[0])

        # If rows > cols, transpose the matrix to iterate over the smaller dimension
        if rows > cols:
            matrix = [list(row) for row in zip(*matrix)]
            rows, cols = cols, rows  # swap dimensions

        # Step 0: Precompute row-wise prefix sums
        for r in range(rows):
            for c in range(1, cols):
                matrix[r][c] += matrix[r][c - 1]

        max_sum = float('-inf')

        # Step 1: Iterate over all pairs of columns (or rows if transposed)
        for c1 in range(cols):
            for c2 in range(c1, cols):
                prefix_sum = 0
                prefix_sums_list = [0]  # sorted list of previous prefix sums

                # Step 2: Compress rows into a 1D array for this column segment
                for r in range(rows):
                    # Sum of row r between columns c1 and c2
                    row_sum = matrix[r][c2] - (matrix[r][c1 - 1] if c1 > 0 else 0)
                    prefix_sum += row_sum

                    # Step 3: Binary search to find closest previous prefix sum
                    # that keeps the subarray sum <= k
                    target = prefix_sum - k
                    idx = bisect.bisect_left(prefix_sums_list, target)
                    if idx < len(prefix_sums_list):
                        max_sum = max(max_sum, prefix_sum - prefix_sums_list[idx])

                    # Step 4: Insert current prefix_sum into sorted list
                    bisect.insort(prefix_sums_list, prefix_sum)

        return max_sum


# Example usage:
matrix = [
    [1, 0, 1],
    [0, -2, 3]
]
k = 2
solution = Solution()
print(solution.maxSumSubmatrix(matrix, k))  # Output: 2




# ✅ Key Features of This Version
    # Handles tall matrices efficiently
    # If rows > cols, it transposes the matrix so the smaller dimension is iterated over.
    # This minimizes the O(min(rows, cols)^2 * max(rows, cols) * log(max(rows, cols))) complexity.
    # Row-wise prefix sum precompute
    # Lets you calculate the sum of any row segment in O(1).
    # Prefix sums + binary search
    # Finds the max subarray sum ≤ k efficiently.
    # bisect_left finds the closest prefix sum ≥ prefix_sum - k.

# Overall time complexity
    # Before transpose: if rows ≤ cols → R = rows, C = cols
    # After transpose: if rows > cols → R = cols, C = rows
    # So the algorithm automatically optimizes for tall matrices.

# | Aspect | Complexity                                                    |
# | ------ | ------------------------------------------------------------- |
# | Time   | O(min(rows, cols)^2 * max(rows, cols) * log(max(rows, cols))) |
# | Space  | O(min(rows, cols))                                            |
