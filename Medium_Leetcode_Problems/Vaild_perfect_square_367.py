# ---------- 💡 Logic ----------

# 1. We need to check whether num is a perfect square.
#
# 2. A perfect square is a number that can be written as:
#
#       x * x = num
#
# 3. We use Binary Search to find x.
#
# 4. Set the search range:
#
#       left = 1
#       right = num
#
# 5. Find the middle value:
#
#       mid = (left + right) // 2
#
# 6. Calculate:
#
#       square = mid * mid
#
# 7. If square == num:
#       num is a perfect square.
#
# 8. If square < num:
#       Search on the right side.
#
#       left = mid + 1
#
# 9. If square > num:
#       Search on the left side.
#
#       right = mid - 1
#
# 10. If no value is found:
#        num is not a perfect square.


# ---------- 🔄 Algorithm ----------

# Step 1: Set:
#
#         left = 1
#         right = num
#
# Step 2: While left <= right:
#
#         mid = (left + right) // 2
#
# Step 3: Calculate:
#
#         square = mid * mid
#
# Step 4: If square == num:
#
#         return True
#
# Step 5: If square < num:
#
#         left = mid + 1
#
# Step 6: Otherwise:
#
#         right = mid - 1
#
# Step 7: If the loop ends:
#
#         return False


# ---------- 🧪 Dry Run ----------

# Input:
# num = 16
#
# --------------------------------
#
# left = 1
# right = 16
#
# --------------------------------
#
# mid = (1 + 16) // 2
#     = 8
#
# square = 8 * 8
#        = 64
#
# 64 > 16
#
# Therefore:
#
# right = 8 - 1
#       = 7
#
# --------------------------------
#
# left = 1
# right = 7
#
# mid = (1 + 7) // 2
#     = 4
#
# square = 4 * 4
#        = 16
#
# 16 == 16
#
# Therefore:
#
# return True
#
# --------------------------------
#
# Final Answer:
#
# True


# ---------- 🐍 Python Code ----------

class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        left = 1
        right = num

        while left <= right:

            mid = (left + right) // 2

            square = mid * mid

            if square == num:
                return True

            elif square < num:
                left = mid + 1

            else:
                right = mid - 1

        return False


# ---------- 🎯 Interview Explanation ----------

# I use Binary Search to check whether there is an integer
# whose square is equal to num.
#
# I maintain a search range from 1 to num.
#
# In every iteration, I calculate the middle value
# and check mid * mid.
#
# If mid * mid equals num, then num is a perfect square.
#
# If mid * mid is smaller than num, I search on the right side.
#
# If mid * mid is greater than num, I search on the left side.
#
# If the binary search finishes without finding an exact square,
# I return False.
#
# Time Complexity: O(log n)
#
# Space Complexity: O(1)


# ---------- ⭐ Key Trick ----------

# Perfect Square:
#
#       mid * mid == num
#
# Example:
#
# num = 25
#
# 5 * 5 = 25
#
# Therefore → True
#
#
# Example:
#
# num = 26
#
# No integer x satisfies:
#
# x * x = 26
#
# Therefore → False


# ---------- 📌 Simple Understanding ----------

# Binary Search:
#
# If mid * mid is too small:
#
#       Move RIGHT
#
#       left = mid + 1
#
#
# If mid * mid is too large:
#
#       Move LEFT
#
#       right = mid - 1
#
#
# If mid * mid == num:
#
#       Perfect Square ✅
#
#
# Otherwise:
#
#       Not a Perfect Square ❌