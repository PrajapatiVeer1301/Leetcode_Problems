# Logic:
#
# 1. Traverse every cell in the grid.
#
# 2. If the current cell is land (1), add 4 to the perimeter.
#
# 3. If the upper neighbor is also land, subtract 2.
#
# 4. If the left neighbor is also land, subtract 2.
#
# 5. Continue until all cells are processed.
#
# 6. Return the total perimeter.

# Algorithm:
#
# 1. Initialize perimeter = 0.
#
# 2. Traverse each cell of the grid.
#
# 3. If the current cell is land:
#    - Add 4 to perimeter.
#
# 4. If the upper cell is land:
#    - Subtract 2 from perimeter.
#
# 5. If the left cell is land:
#    - Subtract 2 from perimeter.
#
# 6. Return the final perimeter.

from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        perimeter = 0

        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == 1:
                    perimeter += 4

                    if i > 0 and grid[i - 1][j] == 1:
                        perimeter -= 2

                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 2

        return perimeter
    

    # Interview Explanation:
#
# 1. Traverse every cell in the grid.
#
# 2. Whenever a land cell is found, add 4 to the perimeter.
#
# 3. If the land cell shares a side with the upper land cell,
#    subtract 2 because that side is common.
#
# 4. If the land cell shares a side with the left land cell,
#    subtract 2 for the same reason.
#
# 5. Continue until all cells are processed.
#
# 6. Return the calculated perimeter.
#
# Time Complexity: O(rows × cols)
# Space Complexity: O(1)
