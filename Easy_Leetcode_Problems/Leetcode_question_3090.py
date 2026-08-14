# We use the Sliding Window technique.
#
# 1. Use two pointers: left and right.
#
# 2. Move right through the string and add each
#    character to the frequency dictionary.
#
# 3. Every character can occur at most 2 times.
#
# 4. If the current character occurs more than
#    2 times, move left forward until its count
#    becomes at most 2.
#
# 5. For every valid window, calculate:
#
#       length = right - left + 1
#
# 6. Keep the maximum length in ans.

# Step 1: Create an empty frequency dictionary.
#
# Step 2: Set:
#
#       left = 0
#       ans = 0
#
# Step 3: Traverse the string using right.
#
# Step 4: Increase the frequency of s[right].
#
# Step 5: While frequency of s[right] > 2:
#
#       decrease count of s[left]
#       move left forward
#
# Step 6: Calculate the current window length.
#
# Step 7: Update ans with the maximum length.
#
# Step 8: Return ans.

##----------- Dry Run ---------##

# Input:
# s = "bcbbbcba"
#
# We need a substring where every character
# appears at most 2 times.
#
# Initially:
#
# left = 0
# ans = 0
#
# ------------------------------------------------
#
# right = 0
# window = "b"
# b = 1
# length = 1
# ans = 1
#
# ------------------------------------------------
#
# right = 1
# window = "bc"
# b = 1, c = 1
# length = 2
# ans = 2
#
# ------------------------------------------------
#
# right = 2
# window = "bcb"
# b = 2, c = 1
# length = 3
# ans = 3
#
# ------------------------------------------------
#
# right = 3
# window = "bcbb"
# b = 3 ❌
#
# b occurs more than 2 times.
# Move left:
#
# remove s[0] = 'b'
# b = 2
# left = 1
#
# Valid window = "cbb"
# length = 3
#
# ans = 3
#
# ------------------------------------------------
#
# right = 4
# window = "cbbb"
# b = 3 ❌
#
# Move left:
#
# remove 'c'
# c = 0
# left = 2
#
# remove 'b'
# b = 2
# left = 3
#
# Valid window = "bb"
# length = 2
#
# ans = 3
#
# ------------------------------------------------
#
# The remaining characters are processed
# in the same way.
#
# The maximum valid substring length is 4.
#
# Final Answer:
# 4

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:

        count = {}
        left = 0
        ans = 0

        for right in range(len(s)):

            count[s[right]] = count.get(s[right], 0) + 1

            while count[s[right]] > 2:
                count[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans

# I used the Sliding Window technique to solve
# this problem efficiently.
#
# I maintained two pointers, left and right,
# to represent the current substring.
#
# I also used a dictionary to store the frequency
# of each character.
#
# I expanded the window using the right pointer.
#
# If any character appeared more than two times,
# I moved the left pointer forward and decreased
# the corresponding frequencies until the window
# became valid again.
#
# For every valid window, I calculated its length
# and stored the maximum length.
#
# Time Complexity: O(n)
#
# Space Complexity: O(1)
#
# Because there are only 26 lowercase English
# letters, the frequency dictionary contains
# at most 26 characters.

