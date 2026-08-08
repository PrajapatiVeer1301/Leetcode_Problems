# Logic:
#
# 1. Use Backtracking to try
#    different partitions.
#
# 2. Start from index 0.
#
# 3. Choose a substring from
#    current index to i.
#
# 4. Check whether the substring
#    is a palindrome.
#
# 5. If it is a palindrome,
#    add it to the current list.
#
# 6. Recursively process the
#    remaining string.
#
# 7. After recursion,
#    remove the substring
#    and try another partition.
#
# 8. When we reach the end of
#    the string, store the
#    current partition.

# Algorithm:
#
# 1. Create an empty result list.
#
# 2. Create a backtracking function:
#
#       backtrack(start)
#
# 3. If start == len(s):
#       add current partition
#       to result.
#
# 4. For i from start to len(s)-1:
#
#       substring = s[start:i+1]
#
#       If substring is palindrome:
#
#           add substring
#
#           backtrack(i+1)
#
#           remove substring
#
# 5. Return result.

# Dry Run:
#
# Input:
#
# s = "aab"
#
# -------------------------
#
# start = 0
#
# Try "a"
#
# current = ["a"]
#
# -------------------------
#
# start = 1
#
# Try "a"
#
# current = ["a", "a"]
#
# -------------------------
#
# start = 2
#
# Try "b"
#
# current = ["a", "a", "b"]
#
# start = 3
#
# End of string
#
# Store:
#
# ["a", "a", "b"]
#
# -------------------------
#
# Backtrack
#
# Remove "b"
#
# current = ["a", "a"]
#
# -------------------------
#
# Backtrack
#
# Remove second "a"
#
# current = ["a"]
#
# -------------------------
#
# Try "ab"
#
# "ab" is not palindrome
#
# Ignore
#
# -------------------------
#
# Backtrack
#
# Remove first "a"
#
# current = []
#
# -------------------------
#
# Try "aa"
#
# "aa" is palindrome
#
# current = ["aa"]
#
# -------------------------
#
# start = 2
#
# Try "b"
#
# current = ["aa", "b"]
#
# End
#
# Store:
#
# ["aa", "b"]
#
# -------------------------
#
# Final Answer:
#
# [
#   ["a", "a", "b"],
#   ["aa", "b"]
# ]


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        result = []
        current = []

        def backtrack(start):

            if start == len(s):
                result.append(current.copy())
                return

            for i in range(start, len(s)):

                part = s[start:i + 1]

                if part == part[::-1]:

                    current.append(part)

                    backtrack(i + 1)

                    current.pop()

        backtrack(0)

        return result

# Interview Explanation:
#
# 1. I used Backtracking because
#    I need to find all possible
#    partitions.
#
# 2. At every index, I tried every
#    possible substring.
#
# 3. I checked whether the substring
#    was a palindrome.
#
# 4. If it was a palindrome, I added
#    it to the current partition and
#    recursively processed the
#    remaining string.
#
# 5. After recursion, I removed the
#    substring using pop() so that
#    another partition could be tried.
#
# 6. When the complete string was
#    processed, I stored the partition.
#
# Time Complexity: O(n * 2^n)
#
# Space Complexity: O(n)
