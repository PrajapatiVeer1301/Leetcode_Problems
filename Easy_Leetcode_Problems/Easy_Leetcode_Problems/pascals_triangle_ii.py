# Approach
# Instead of generating the full Pascal’s Triangle, we only generate the required row.
#
# We start with the first row [1] and iteratively build the next rows until reaching rowIndex.
#
# For each new row:
# - The first and last elements are always 1
# - The middle elements are formed by adding two adjacent elements from the previous row
#
# This way, we only store one row at a time and return the final row.

# Logic
# Pascal’s Triangle follows this rule:
# - First element = 1
# - Last element = 1
# - Middle element = sum of two adjacent elements from the previous row
#
# Formula:
# new_row[j] = row[j - 1] + row[j]
#
# We use the previous row to construct the current row and keep updating it until the required row is reached.

# Complexity
# Time Complexity: O(rowIndex^2)
# Space Complexity: O(rowIndex)

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]

        for i in range(1, rowIndex + 1):
            new_row = [1]

            for j in range(1, i):
                new_row.append(row[j - 1] + row[j])

            new_row.append(1)
            row = new_row

        return row