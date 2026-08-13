# Logic:
#
# We use four boundaries:
#
# top    = first row
# bottom = last row
# left   = first column
# right  = last column
#
# We fill the matrix in 4 directions:
#
# 1. Left → Right
#    Fill the top row.
#
# 2. Top → Bottom
#    Fill the right column.
#
# 3. Right → Left
#    Fill the bottom row.
#
# 4. Bottom → Top
#    Fill the left column.
#
# After completing one outer layer,
# move the boundaries inward:
#
# top += 1
# bottom -= 1
# left += 1
# right -= 1
#
# Continue until all cells are filled.
#
# Main idea:
#
# Top → Right → Bottom → Left
#
# Then move inward and repeat.


# Algorithm:
#
# 1. Create an n × n matrix filled with 0.
#
# 2. Set:
#       top = 0
#       bottom = n - 1
#       left = 0
#       right = n - 1
#
# 3. Set num = 1.
#
# 4. While top <= bottom and left <= right:
#
#       Fill top row from left to right.
#       Increase top.
#
#       Fill right column from top to bottom.
#       Decrease right.
#
#       Fill bottom row from right to left.
#       Decrease bottom.
#
#       Fill left column from bottom to top.
#       Increase left.
#
# 5. Return the matrix.



#------------DRY RUN -------#
# Initial matrix:
#
# [0, 0, 0]
# [0, 0, 0]
# [0, 0, 0]
#
# num = 1
#
# -------------------------
#
# 1. Left → Right
#
# [1, 2, 3]
# [0, 0, 0]
# [0, 0, 0]
#
# top = 1
#
# -------------------------
#
# 2. Top → Bottom
#
# [1, 2, 3]
# [0, 0, 4]
# [0, 0, 5]
#
# right = 1
#
# -------------------------
#
# 3. Right → Left
#
# [1, 2, 3]
# [0, 0, 4]
# [7, 6, 5]
#
# bottom = 1
#
# -------------------------
#
# 4. Bottom → Top
#
# [1, 2, 3]
# [8, 0, 4]
# [7, 6, 5]
#
# left = 1
#
# -------------------------
#
# Inner layer:
#
# Put 9 in the remaining cell.
#
# [1, 2, 3]
# [8, 9, 4]
# [7, 6, 5]
#
# Final Answer:
#
# [[1,2,3],
#  [8,9,4],
#  [7,6,5]]


# Interview Explanation:
#
# I used four boundaries: top, bottom, left,
# and right to keep track of the current layer.
#
# I fill the matrix in four directions:
# left to right, top to bottom, right to left,
# and bottom to top.
#
# After completing each direction, I move the
# corresponding boundary inward.
#
# I continue this process until all cells
# are filled with numbers from 1 to n².
#
# Time Complexity: O(n²)
#
# Space Complexity: O(n²)
# because we need to create the output matrix.

##⭐ Easy way to remember
##
# Top → Right → Bottom → Left
##          ↓
##    Move inward
##          ↓
##       Repeat
##
##
##
##