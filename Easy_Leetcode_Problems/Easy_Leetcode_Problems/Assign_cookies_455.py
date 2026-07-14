# Logic:
#
# 1. Sort both the greed array and cookie array.
#
# 2. Start from the smallest child and smallest cookie.
#
# 3. If the cookie is big enough,
#    satisfy the child.
#
# 4. Move to the next child and next cookie.
#
# 5. Otherwise,
#    try a bigger cookie.
#
# 6. Return the number of satisfied children.

# Algorithm:
#
# 1. Sort g and s.
#
# 2. Initialize two pointers:
#    child = 0
#    cookie = 0
#
# 3. While both pointers are within the arrays:
#
#    - If cookie size >= greed factor:
#      - Increase satisfied count.
#      - Move both pointers.
#
#    - Else:
#      - Move only the cookie pointer.
#
# 4. Return the satisfied count.

from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort()
        s.sort()

        child = 0
        cookie = 0

        while child < len(g) and cookie < len(s):

            if s[cookie] >= g[child]:
                child += 1

            cookie += 1

        return child
    

# Interview Explanation:
#
# 1. I used the Greedy approach.
#
# 2. First, I sorted both the greed array
#    and the cookie array.
#
# 3. Then I used two pointers.
#
# 4. If the current cookie could satisfy
#    the current child, I assigned it
#    and moved to the next child.
#
# 5. Otherwise, I tried a larger cookie.
#
# 6. Finally, I returned the number of
#    satisfied children.
#
# Time Complexity: O(n log n + m log m)
# Space Complexity: O(1)