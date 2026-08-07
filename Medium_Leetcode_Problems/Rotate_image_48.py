# Logic:
#
# 1. Find the size of matrix.
#
# 2. Transpose the matrix
#    by swapping:
#
#      matrix[i][j]
#      matrix[j][i]
#
# 3. Reverse every row.
#
# 4. The matrix becomes
#    rotated by 90°
#    clockwise.

# Algorithm:
#
# 1. Find n.
#
# 2. Perform transpose.
#
# 3. Reverse each row.
#
# 4. Matrix is rotated.

# Dry Run:
#
# Input:
#
# 1 2 3
# 4 5 6
# 7 8 9
#
# --------------------
#
# Step 1
#
# Transpose
#
# 1 4 7
# 2 5 8
# 3 6 9
#
# --------------------
#
# Step 2
#
# Reverse each row
#
# Row1
#
# 7 4 1
#
# Row2
#
# 8 5 2
#
# Row3
#
# 9 6 3
#
# --------------------
#
# Final Output
#
# 7 4 1
# 8 5 2
# 9 6 3

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        n = len(matrix)

        # Step 1: Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse every row
        for row in matrix:
            row.reverse()


# Interview Explanation:
#
# 1. Since creating another matrix
#    is not allowed,
#    I rotated the matrix in-place.
#
# 2. First, I transposed the matrix
#    by swapping rows and columns.
#
# 3. Then, I reversed every row.
#
# 4. Transpose + Reverse
#    gives a 90° clockwise rotation.
#
# Time Complexity: O(n²)
#
# Space Complexity: O(1)