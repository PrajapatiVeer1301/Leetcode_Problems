        # ## LOGIC:
        # Split the sentence into individual words.
        # Reverse each word separately.
        # Join all reversed words using a single space.

class Solution:
    def reverseWords(self, s: str) -> str:

        # Split the sentence into words.
        words = s.split()

        # Reverse each word using slicing [::-1].
        reversed_words = [word[::-1] for word in words]

        # Join the reversed words with spaces.
        return " ".join(reversed_words)


# ## EXAMPLE:
# Input:  "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

# ## DRY RUN:
# s = "Mr Ding"
#
# Step 1: Split into words
# words = ["Mr", "Ding"]
#
# Step 2: Reverse each word
# reversed_words = ["rM", "gniD"]
#
# Step 3: Join using spaces
# Output = "rM gniD"

# ## ALGORITHM:
# 1. Split the string into words.
# 2. Reverse each word using [::-1].
# 3. Join the reversed words with a single space.
# 4. Return the final string.

# ## INTERVIEW EXPLANATION:
# I split the input sentence into words, reverse each word
# using Python slicing, and join the reversed words with spaces.
# The original order of words remains unchanged.

# ## KEY TRICK:
# word[::-1] reverses a string in Python.
# "Hello"[::-1] becomes "olleH".

# ## TIME COMPLEXITY:
# O(n), where n is the length of the input string.

# ## SPACE COMPLEXITY:
# O(n), because we store the words and the reversed result.
