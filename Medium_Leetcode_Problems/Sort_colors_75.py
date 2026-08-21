# ---------- 💡 Logic ----------

# 0 → Move to the LEFT
# 1 → Keep in the MIDDLE
# 2 → Move to the RIGHT
#
# low  = position for 0
# mid  = current element
# high = position for 2
#
# If nums[mid] == 0:
#     Swap low and mid
#     low += 1
#     mid += 1
#
# If nums[mid] == 1:
#     mid += 1
#
# If nums[mid] == 2:
#     Swap mid and high
#     high -= 1
#
# Important:
# When we find 2, we do NOT increase mid.
# The swapped element still needs to be checked.


# ---------- 🔄 Algorithm ----------

# Step 1: Set:
#
#         low = 0
#         mid = 0
#         high = len(nums) - 1
#
# Step 2: Run a loop while mid <= high.
#
# Step 3: If nums[mid] == 0:
#
#         Swap nums[low] and nums[mid]
#         low += 1
#         mid += 1
#
# Step 4: If nums[mid] == 1:
#
#         Move mid forward
#         mid += 1
#
# Step 5: If nums[mid] == 2:
#
#         Swap nums[mid] and nums[high]
#         high -= 1
#
#         Do NOT increase mid,
#         because the swapped element must be checked.
#
# Step 6: Continue until mid > high.
#
# Step 7: The array is sorted in-place:
#
#         0 → 0 → ... → 1 → 1 → ... → 2 → 2


# ---------- 🧪 Dry Run ----------

# Input:
# nums = [2,0,2,1,1,0]
#
# Initial:
# low = 0
# mid = 0
# high = 5
#
# --------------------------------
#
# nums[mid] = 2
#
# Swap nums[mid] and nums[high]
#
# nums = [0,0,2,1,1,2]
#
# high = 4
# mid = 0
#
# --------------------------------
#
# nums[mid] = 0
#
# Swap nums[low] and nums[mid]
#
# nums = [0,0,2,1,1,2]
#
# low = 1
# mid = 1
#
# --------------------------------
#
# nums[mid] = 0
#
# Swap nums[low] and nums[mid]
#
# nums = [0,0,2,1,1,2]
#
# low = 2
# mid = 2
#
# --------------------------------
#
# nums[mid] = 2
#
# Swap nums[mid] and nums[high]
#
# nums = [0,0,1,1,2,2]
#
# high = 3
# mid = 2
#
# --------------------------------
#
# nums[mid] = 1
#
# mid = 3
#
# --------------------------------
#
# nums[mid] = 1
#
# mid = 4
#
# --------------------------------
#
# mid > high
#
# Stop.
#
# Final:
# [0,0,1,1,2,2]


# ---------- 🐍 Python Code ----------

class Solution:
    def sortColors(self, nums: List[int]) -> None:

        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:

            if nums[mid] == 0:

                # Swap nums[low] and nums[mid]
                nums[low], nums[mid] = nums[mid], nums[low]

                low += 1
                mid += 1

            elif nums[mid] == 1:

                # 1 is already in the correct area
                mid += 1

            else:

                # Swap nums[mid] and nums[high]
                nums[mid], nums[high] = nums[high], nums[mid]

                high -= 1

                # Do NOT increase mid here


# ---------- 🎯 Interview Explanation ----------

# I use the Dutch National Flag algorithm.
#
# I maintain three pointers:
# low, mid, and high.
#
# low represents the position for 0.
# mid checks the current element.
# high represents the position for 2.
#
# If the current element is 0,
# I swap it with the low position.
#
# If it is 1,
# I simply move mid forward.
#
# If it is 2,
# I swap it with the high position
# and decrease high.
#
# I don't increase mid after finding 2
# because the newly swapped element must be checked.
#
# Time Complexity: O(n)
#
# Space Complexity: O(1)
#
# The array is modified in-place.


# ---------- ⭐ Key Trick ----------

# 0 → LEFT
# 1 → MIDDLE
# 2 → RIGHT
#
#        low    mid       high
#         ↓      ↓          ↓
# [  0  |  1  | unknown |  2  ]
#
# 0 → swap + low++ + mid++
# 1 → mid++
# 2 → swap + high--
#
# IMPORTANT:
#
# For 2:
# high--
# but mid does NOT increase.