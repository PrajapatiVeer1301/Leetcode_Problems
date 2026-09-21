# 💡 Logic
#
# We need to find the maximum length of a palindrome
# that can be created using the characters of the string.
#
# A palindrome needs characters in pairs:
#
# Example:
# "cc" → can be placed on the left and right sides.
#
# For every character, we can use the largest even part
# of its frequency.
#
# For example:
#
# frequency = 5
# usable part = 4
#
# frequency = 4
# usable part = 4
#
# frequency = 3
# usable part = 2
#
# If at least one character has an odd frequency,
# we can place ONE such character in the center of
# the palindrome.
#
# Therefore:
#
# - Add (frequency // 2) * 2 for every character.
# - If any frequency is odd, add 1 for the center.
#
#
# 🔄 Algorithm
#
# 1. Use Counter to count the frequency of every character.
#
# 2. For each frequency:
#    - Add (frequency // 2) * 2 to answer.
#    - If the frequency is odd, remember that we have
#      an odd character.
#
# 3. If at least one odd frequency exists,
#    add 1 to answer for the center character.
#
# 4. Return answer.
#
#
# 🧑‍💻 Python Code

from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:

        # Count the frequency of each character
        count = Counter(s)

        # Store the length of the longest palindrome
        answer = 0

        # Check the frequency of every character
        for freq in count.values():

            # Add the largest even part of the frequency
            answer += (freq // 2) * 2

        # If any character has an odd frequency,
        # one character can be placed in the center
        if any(freq % 2 == 1 for freq in count.values()):
            answer += 1

        # Return the maximum palindrome length
        return answer


# 🧪 Dry Run
#
# s = "abccccdd"
#
# Frequency:
#
# a → 1
# b → 1
# c → 4
# d → 2
#
# Calculate the usable even parts:
#
# a → 0
# b → 0
# c → 4
# d → 2
#
# Total:
#
# 0 + 0 + 4 + 2 = 6
#
# There are odd frequencies:
#
# a → 1
# b → 1
#
# We can use ONE odd character in the center.
#
# Therefore:
#
# 6 + 1 = 7
#
# ✅ Answer = 7
#
#
# ⏱️ Complexity
#
# Time Complexity: O(n)
#
# We traverse the string to count characters and then
# traverse the frequency values.
#
# Space Complexity: O(k)
#
# k = number of distinct characters.
#
# Since the input contains only uppercase and lowercase
# English letters, k is at most 52.
#
#
# 🎯 Interview Explanation
#
# "I first count the frequency of every character using Counter.
# A palindrome requires matching pairs, so for each character
# I take the largest even part of its frequency.
# If there is at least one character with an odd frequency,
# I can place one occurrence of that character in the center.
# Therefore, I add all usable even frequencies and then add
# one if any odd frequency exists.
# This gives the maximum possible palindrome length."