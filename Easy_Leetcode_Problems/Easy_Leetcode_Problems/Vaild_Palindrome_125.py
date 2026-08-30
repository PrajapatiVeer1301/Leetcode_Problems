# 💡 Logic
#
# We use the Two Pointer approach.
#
# left  = points to the beginning of the string
# right = points to the end of the string
#
# We ignore all non-alphanumeric characters.
#
# We convert uppercase letters to lowercase.
#
# Then we compare the characters from both sides.
#
# If they are different:
#     return False
#
# If they are same:
#     move left forward
#     move right backward
#
# If all characters match:
#     return True


# 🔄 Algorithm
#
# Step 1: Set left = 0.
#
# Step 2: Set right = len(s) - 1.
#
# Step 3: Run a loop while left < right.
#
# Step 4: If s[left] is not alphanumeric:
#         left += 1
#         continue
#
# Step 5: If s[right] is not alphanumeric:
#         right -= 1
#         continue
#
# Step 6: Convert both characters to lowercase.
#
# Step 7: Compare the characters.
#
#         If they are different:
#             return False
#
# Step 8: Move both pointers:
#
#         left += 1
#         right -= 1
#
# Step 9: If the loop finishes:
#         return True


# 🧪 Dry Run
#
# Input:
# s = "A man, a plan, a canal: Panama"
#
# Ignore spaces and symbols.
#
# After removing non-alphanumeric characters:
#
# "AmanaplanacanalPanama"
#
# Convert to lowercase:
#
# "amanaplanacanalpanama"
#
# --------------------------------
#
# Compare from both sides:
#
# left = 'a'
# right = 'a'
# Same ✅
#
# left = 'm'
# right = 'm'
# Same ✅
#
# left = 'a'
# right = 'a'
# Same ✅
#
# Continue...
#
# All characters match.
#
# --------------------------------
#
# Final Answer:
#
# True


class Solution:

    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        while left < right:

            # Skip non-alphanumeric characters from left
            while left < right and not s[left].isalnum():
                left += 1

            # Skip non-alphanumeric characters from right
            while left < right and not s[right].isalnum():
                right -= 1

            # Convert both characters to lowercase
            leftChar = s[left].lower()
            rightChar = s[right].lower()

            # If characters are different
            if leftChar != rightChar:
                return False

            # Move both pointers
            left += 1
            right -= 1

        return True

# 🎯 Interview Explanation
#
# I use the Two Pointer technique.
#
# One pointer starts from the left and another
# pointer starts from the right.
#
# I skip all non-alphanumeric characters
# such as spaces, commas, and colons.
#
# I compare the lowercase characters from both sides.
#
# If any pair is different, the string is not
# a palindrome, so I return False.
#
# If all valid characters match, I return True.
#
# Time Complexity: O(n)
#
# Space Complexity: O(1)
#
# We do not create another string,
# so the solution uses constant extra space.


# ⭐ Key Trick
#
# Two pointers:
#
# left  →
#
# "A man, a plan, a canal: Panama"
#  ↑
#
# right
#                              ↑
#
# Skip:
#
# spaces
# commas
# colons
# other non-alphanumeric characters
#
# Compare:
#
# lowercase(left) == lowercase(right)
#
# If same:
#     left += 1
#     right -= 1
#
# If different:
#     return False
#
# Finally:
#     return True

