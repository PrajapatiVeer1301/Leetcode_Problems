# ---------- 💡 Logic ----------

# 1. Start with k.
#
# 2. Check whether k is present in nums.
#
# 3. If k is present in nums:
#       Move to the next multiple of k.
#
#       multiple += k
#
# 4. If the current multiple is not present in nums:
#       Return that multiple.


# ---------- 🔄 Algorithm ----------

# Step 1: Store the original value of k.
#
# Step 2: Create a set from nums for fast searching.
#
# Step 3: Start with multiple = k.
#
# Step 4: While multiple is present in nums:
#
#         multiple += k
#
# Step 5: When multiple is not present:
#
#         return multiple


# ---------- 🧪 Dry Run ----------

# Input:
# nums = [8,2,3,4,6]
# k = 2
#
# --------------------------------
#
# num_set = {8,2,3,4,6}
#
# multiple = 2
#
# --------------------------------
#
# Check 2:
#
# 2 is present
#
# multiple = 2 + 2
#          = 4
#
# --------------------------------
#
# Check 4:
#
# 4 is present
#
# multiple = 4 + 2
#          = 6
#
# --------------------------------
#
# Check 6:
#
# 6 is present
#
# multiple = 6 + 2
#          = 8
#
# --------------------------------
#
# Check 8:
#
# 8 is present
#
# multiple = 8 + 2
#          = 10
#
# --------------------------------
#
# Check 10:
#
# 10 is NOT present
#
# Therefore:
#
# Output = 10


# ---------- 🐍 Python Code ----------

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:

        num_set = set(nums)

        multiple = k

        while multiple in num_set:
            multiple += k

        return multiple


# ---------- 🎯 Simple Understanding ----------

# k = 2
#
# 2  → found
# 4  → found
# 6  → found
# 8  → found
# 10 → not found
#
# Answer = 10


# ---------- ⭐ Key Trick ----------

# Multiples are generated using:
#
# multiple += k
#
# Example:
#
# k = 3
#
# 3 → 6 → 9 → 12 → 15 → ...
#
# Stop at the first number that is
# not present in nums.


# ---------- ⏱️ Complexity ----------

# Time Complexity: O(n) approximately
#
# Creating the set takes O(n).
#
# Each set lookup takes O(1) average.
#
# Space Complexity: O(n)
#
# Because we create a set containing nums.