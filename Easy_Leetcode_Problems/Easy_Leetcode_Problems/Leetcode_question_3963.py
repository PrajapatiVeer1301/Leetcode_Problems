
class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:

        # ## LOGIC:
        # Make every cell an obstacle initially.
        # Then create one clear path:
        # 1. Open the entire first row.
        # 2. Open the entire last column.
        # All other cells remain obstacles.
        #
        # This creates exactly one path:
        # Move right along the first row,
        # then move down along the last column.

        # Create an m x n grid filled with obstacles.
        grid = [['#'] * n for _ in range(m)]

        # Open every cell in the first row.
        for j in range(n):
            grid[0][j] = '.'

        # Open every cell in the last column.
        for i in range(m):
            grid[i][n - 1] = '.'

        # Convert each row into a string.
        return [''.join(row) for row in grid]


# ## EXAMPLE:
# Input: m = 2, n = 3
#
# Output:
# ["..#", "###"]
#
# ## DRY RUN:
# m = 2, n = 3
#
# Step 1: Create the grid filled with '#'.
# ###
# ###
#
# Step 2: Open the first row.
# ...
# ###
#
# Step 3: Open the last column.
# .. .
# ## .
#
# Final grid:
# ["...", "##."]
#
# Path:
# (0,0) -> (0,1) -> (0,2)
#                     |
#                   (1,2)
#
# There is exactly one valid path.
#
# ## ALGORITHM:
# 1. Create an m x n grid filled with '#'.
# 2. Change every cell in the first row to '.'.
# 3. Change every cell in the last column to '.'.
# 4. Convert each row into a string.
# 5. Return the grid.
#
# ## INTERVIEW EXPLANATION:
# I initially block every cell. Then I open the first row
# and the last column. The only way to reach the destination
# is to move right along the first row and then down the
# last column. All other cells stay blocked, so the path
# is unique.
#
# ## TIME COMPLEXITY:
# O(m * n), because we create and process every grid cell.
#
# ## SPACE COMPLEXITY:
# O(m * n), because we store the grid.
