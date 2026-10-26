
class Solution:
    def checkRecord(self, s: str) -> bool:

        # ## LOGIC:
        # The student is eligible if:
        # 1. Total absences are fewer than 2.
        # 2. There are no 3 consecutive L characters.

        # Count the total number of absent days.
        absent_count = s.count('A')

        # If the student was absent 2 or more days,
        # they are not eligible for the award.
        if absent_count >= 2:
            return False

        # Check whether 3 consecutive late days exist.
        if 'LLL' in s:
            return False

        # If both conditions are satisfied, return True.
        return True


# ## EXAMPLE:
# Input: s = "PPALLP"
# Output: True

# ## DRY RUN:
# s = "PPALLP"
#
# Step 1: Count absences.
# absent_count = 1
#
# Step 2: Check if "LLL" exists.
# "LLL" is not present.
#
# Step 3: Both conditions are satisfied.
# Output = True

# ## ALGORITHM:
# 1. Count the number of 'A' characters.
# 2. If the count is 2 or more, return False.
# 3. If "LLL" occurs in the string, return False.
# 4. Otherwise, return True.

# ## INTERVIEW EXPLANATION:
# I count the total absences using s.count('A').
# Then I check whether the string contains "LLL".
# If either condition fails, I return False.
# Otherwise, the student is eligible, so I return True.

# ## KEY TRICK:
# s.count('A') counts absences.
# 'LLL' in s checks for three consecutive late days.

# ## TIME COMPLEXITY:
# O(n), where n is the length of the string.

# ## SPACE COMPLEXITY:
# O(1), because we use only a few variables.
