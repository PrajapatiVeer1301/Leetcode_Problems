# Logic:
#
# 1. Count the frequency of each
#    character in the given word.
#
# 2. Sort the frequencies in
#    descending order.
#
# 3. The characters with the highest
#    frequency should require the
#    fewest key presses.
#
# 4. Assign:
#      First 8 characters  -> 1 push
#      Next 8 characters   -> 2 pushes
#      Next 8 characters   -> 3 pushes
#      Remaining characters-> 4 pushes
#
# 5. Multiply each character's
#    frequency by its assigned
#    number of pushes.
#
# 6. Add all the values to get
#    the minimum total pushes.
#
# 7. Return the answer.

# Algorithm:
#
# 1. Create an array freq[26]
#    initialized with 0.
#
# 2. Traverse the word and count
#    the frequency of each letter.
#
# 3. Sort the frequency array
#    in descending order.
#
# 4. Initialize answer = 0.
#
# 5. Traverse the sorted frequency
#    array.
#
# 6. If frequency is 0,
#    stop the loop.
#
# 7. Calculate the number of pushes:
#
#       pushes = (index // 8) + 1
#
# 8. Update:
#
#       answer += frequency * pushes
#
# 9. Return answer.

# Dry Run:
#
# Input:
#
# word = "aabbccddeeffgghhiiiiii"
#
# Frequency:
#
# a = 2
# b = 2
# c = 2
# d = 2
# e = 2
# f = 2
# g = 2
# h = 2
# i = 6
#
# After sorting (Descending):
#
# [6,2,2,2,2,2,2,2,2]
#
# answer = 0
#
# --------------------------
#
# index = 0
# frequency = 6
# pushes = (0 // 8) + 1 = 1
#
# answer = 0 + (6 × 1)
# answer = 6
#
# --------------------------
#
# index = 1
# frequency = 2
# pushes = 1
#
# answer = 6 + 2
# answer = 8
#
# --------------------------
#
# index = 2
# frequency = 2
# pushes = 1
#
# answer = 10
#
# --------------------------
#
# index = 3
# frequency = 2
# pushes = 1
#
# answer = 12
#
# --------------------------
#
# index = 4
# frequency = 2
# pushes = 1
#
# answer = 14
#
# --------------------------
#
# index = 5
# frequency = 2
# pushes = 1
#
# answer = 16
#
# --------------------------
#
# index = 6
# frequency = 2
# pushes = 1
#
# answer = 18
#
# --------------------------
#
# index = 7
# frequency = 2
# pushes = 1
#
# answer = 20
#
# --------------------------
#
# index = 8
# frequency = 2
# pushes = (8 // 8) + 1 = 2
#
# answer = 20 + (2 × 2)
# answer = 24
#
# --------------------------
#
# Final Answer:
#
# 24

class Solution:
    def minimumPushes(self, word: str) -> int:

        freq = [0] * 26

        # Count frequency
        for ch in word:
            freq[ord(ch) - ord('a')] += 1

        # Sort in descending order
        freq.sort(reverse=True)

        pushes = 0

        for i in range(26):

            if freq[i] == 0:
                break

            pushes += freq[i] * ((i // 8) + 1)

        return pushes

# Interview Explanation:
#
# 1. I first counted the frequency
#    of every character in the word.
#
# 2. Since frequently occurring
#    characters should require fewer
#    key presses, I sorted the
#    frequencies in descending order.
#
# 3. I assigned the first 8 highest
#    frequencies to 1 push, the next
#    8 to 2 pushes, the next 8 to
#    3 pushes, and so on.
#
# 4. For each character, I multiplied
#    its frequency by the assigned
#    push count and added it to
#    the final answer.
#
# 5. Finally, I returned the minimum
#    number of key presses required.
#
# Time Complexity: O(n)
#
# Space Complexity: O(1)
#
# (The frequency array size is
# fixed at 26.)