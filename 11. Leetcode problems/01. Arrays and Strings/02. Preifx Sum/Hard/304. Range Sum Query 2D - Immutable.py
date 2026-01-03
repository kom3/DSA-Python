# 304. Range Sum Query 2D - Immutable

# Given a 2D matrix matrix, handle multiple queries of the following type:

# Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# Implement the NumMatrix class:

# NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
# int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# You must design an algorithm where sumRegion works on O(1) time complexity.


# Input
# ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
# [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
# Output
# [null, 8, 11, 12]

# Explanation
# NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
# numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
# numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
# numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# -104 <= matrix[i][j] <= 104
# 0 <= row1 <= row2 < m
# 0 <= col1 <= col2 < n
# At most 104 calls will be made to sumRegion.


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        """
        We store a DEEP COPY of the matrix because we will
        modify it in-place to become the prefix sum matrix.
        """
        self.prefix_sum_matrix = [row[:] for row in matrix]
        self.generate_prefix_sum()

    def generate_prefix_sum(self):
        """
        Build the 2D prefix sum matrix.

        PREFIX SUM DEFINITION:
        prefix_sum[r][c] = sum of all elements in rectangle
                           from (0,0) to (r,c) inclusive

        FORMULA (Inclusion–Exclusion):
        prefix_sum[r][c] =
            matrix[r][c]
          + prefix_sum[r-1][c]        (top)
          + prefix_sum[r][c-1]        (left)
          - prefix_sum[r-1][c-1]      (overlap, counted twice)
        """
        rows = len(self.prefix_sum_matrix)
        cols = len(self.prefix_sum_matrix[0])

        for r in range(rows):
            for c in range(cols):
                if r > 0:
                    self.prefix_sum_matrix[r][c] += self.prefix_sum_matrix[r - 1][c]
                if c > 0:
                    self.prefix_sum_matrix[r][c] += self.prefix_sum_matrix[r][c - 1]
                if r > 0 and c > 0:
                    self.prefix_sum_matrix[r][c] -= self.prefix_sum_matrix[r - 1][c - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        Compute sum of submatrix from (row1, col1) to (row2, col2).

        QUERY FORMULA (Inclusion–Exclusion):
        sum =
            prefix_sum[row2][col2]                (full rectangle)
          - prefix_sum[row1-1][col2]              (remove top strip)
          - prefix_sum[row2][col1-1]              (remove left strip)
          + prefix_sum[row1-1][col1-1]            (add overlap back)
        """
        total = self.prefix_sum_matrix[row2][col2]

        if row1 > 0:
            total -= self.prefix_sum_matrix[row1 - 1][col2]
        if col1 > 0:
            total -= self.prefix_sum_matrix[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            total += self.prefix_sum_matrix[row1 - 1][col1 - 1]

        return total




# ⏱ Complexity
# | Operation     | Time     |
# | ------------- | -------- |
# | Preprocessing | O(m × n) |
# | Each Query    | O(1)     |
# | Space         | O(m × n) |



# 🧠 Key Formulas to Memorize (Interview Gold)
# Prefix Sum Construction
    # ps[r][c] = matrix[r][c]
    #      + ps[r-1][c]
    #      + ps[r][c-1]
    #      - ps[r-1][c-1]


# Rectangle Query
    # sum = ps[r2][c2]
    # - ps[r1-1][c2]
    # - ps[r2][c1-1]
    # + ps[r1-1][c1-1]

