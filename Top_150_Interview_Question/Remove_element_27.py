# Logic:
#
# 1. Initialize k = 0.
#
# 2. Traverse the array.
#
# 3. If the current element is
#    not equal to val,
#    copy it to index k.
#
# 4. Increment k.
#
# 5. Continue until the end.
#
# 6. Return k.

# Algorithm:
#
# 1. Set k = 0.
#
# 2. Traverse the array.
#
# 3. If nums[i] != val:
#
#       nums[k] = nums[i]
#
#       k = k + 1
#
# 4. Return k.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0

        for i in range(len(nums)):

            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k

# Dry Run:
#
# Input:
#
# nums = [3,2,2,3]
# val = 3
#
# k = 0
#
# -----------------------
#
# i = 0
# nums[0] = 3
#
# 3 == val
#
# Ignore
#
# k = 0
#
# -----------------------
#
# i = 1
# nums[1] = 2
#
# 2 != val
#
# nums[0] = 2
#
# k = 1
#
# -----------------------
#
# i = 2
# nums[2] = 2
#
# 2 != val
#
# nums[1] = 2
#
# k = 2
#
# -----------------------
#
# i = 3
# nums[3] = 3
#
# Ignore
#
# -----------------------
#
# Final Array:
#
# [2,2,_,_]
#
# Return:
#
# k = 2

# Interview Explanation:
#
# 1. I used a pointer k to keep
#    track of the next position
#    for a valid element.
#
# 2. I traversed the array once.
#
# 3. Whenever I found an element
#    different from val,
#    I copied it to index k.
#
# 4. Then I incremented k.
#
# 5. At the end, the first k
#    elements contain all valid
#    elements, and I returned k.
#
# Time Complexity: O(n)
#
# Space Complexity: O(1)
