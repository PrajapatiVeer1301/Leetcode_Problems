# Logic:
#
# 1. Convert the 2D grid into a 1D list.
#
# 2. Rotate the list to the right by k positions.
#
# 3. Convert the rotated list back into a 2D grid.
#
# 4. Return the new grid.

# Algorithm:
#
# 1. Find rows (m) and columns (n).
#
# 2. Store all elements in one list.
#
# 3. Compute:
#       k = k % total_elements
#
# 4. Rotate the list:
#       new_list = last k elements + remaining elements
#
# 5. Fill a new 2D grid using the rotated list.
#
# 6. Return the result.

from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        m = len(grid)
        n = len(grid[0])

        arr = []

        # Convert 2D grid to 1D list
        for row in grid:
            for num in row:
                arr.append(num)

        total = m * n
        k = k % total

        # Rotate the list
        arr = arr[-k:] + arr[:-k]

        # Convert back to 2D grid
        result = []
        index = 0

        for i in range(m):
            row = []
            for j in range(n):
                row.append(arr[index])
                index += 1
            result.append(row)

        return result

# Interview Explanation:
#
# 1. First, I flattened the 2D grid into a 1D list.
#
# 2. Then I rotated the list to the right by k positions.
#
# 3. After rotation, I reconstructed the 2D grid.
#
# 4. Finally, I returned the shifted grid.
#
# Time Complexity: O(m × n)
# Space Complexity: O(m × n)