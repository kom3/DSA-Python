# 1074. Number of Submatrices That Sum to Target

# Given a matrix and a target, return the number of non-empty submatrices that sum to target.

# A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

# Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

# Example 1:
# Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
# Output: 4
# Explanation: The four 1x1 submatrices that only contain 0.

# Example 2:
# Input: matrix = [[1,-1],[-1,1]], target = 0
# Output: 5
# Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.

# Example 3:
# Input: matrix = [[904]], target = 0
# Output: 0

# Constraints:
# 1 <= matrix.length <= 100
# 1 <= matrix[0].length <= 100
# -1000 <= matrix[i][j] <= 1000
# -10^8 <= target <= 10^8




class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        """
        Count the number of submatrices that sum to a given target.
        
        Key patterns:
        1. Fix two columns (c1, c2) as the left and right boundaries.
        2. For these columns, compress rows into a 1D array representing
           the sum of elements between c1 and c2 for each row.
        3. Use 1D prefix sum + hash map (like Subarray Sum = K problem) 
           to count the number of contiguous row ranges with sum = target.
        """

        rows, cols = len(matrix), len(matrix[0])
        count = 0

        # Step 0: Precompute row-wise prefix sums for quick range sum calculation
        for r in range(rows):
            for c in range(1, cols):
                matrix[r][c] += matrix[r][c - 1]

        # Step 1: Fix column pairs (left c1, right c2)
        for c1 in range(cols):
            for c2 in range(c1, cols):
                # Step 2: Compress rows into 1D array
                prefix_sum = 0
                freq = {0: 1}  # prefix_sum 0 seen once before starting

                for r in range(rows):
                    # Step 3: Sum of row r between columns c1 and c2
                    row_sum = matrix[r][c2]
                    if c1 > 0:
                        row_sum -= matrix[r][c1 - 1]

                    # Step 4: 1D prefix sum logic
                    prefix_sum += row_sum

                    # Check how many previous prefix sums satisfy prefix_sum - target
                    count += freq.get(prefix_sum - target, 0)

                    # Update frequency of current prefix_sum
                    freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

        return count






# 🔑 Key Notes for Quick Revision
# Row-wise prefix sum:
    # matrix[r][c] += matrix[r][c-1] → helps compute sum of any row segment in O(1).
# Fix column pairs (c1, c2): 
    # Each pair defines a submatrix width.
    # For each pair, reduce the 2D problem to 1D array of row sums.
# Compress rows into 1D array:
    # row_sum = sum of elements from c1 to c2 in that row
    # Now the problem becomes count subarrays with sum = target.
# Use 1D prefix sum + hash map:
    # Pattern: prefix_sum[i] - prefix_sum[j] = target → subarray sum = target
    # Hash map stores frequency of prefix sums.

# Complexity:
    # Precompute row prefix sum: O(rows * cols)
    # Column pairs: O(cols^2)
    # For each pair, scan rows: O(rows)
    # ✅ Total: O(rows * cols^2)
    # ✅ Space: O(rows) for freq dictionary (max rows prefix sums)

# Pattern Recognition:
    # ✅ 2D → compress into 1D using fixed boundaries
    # ✅ Apply Subarray Sum = K logic
    # ✅ Count prefix sums for fast lookup