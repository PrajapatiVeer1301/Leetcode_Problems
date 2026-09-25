# 💡 LOGIC
#
# We are given an array of words.
#
# We need to find two words that do NOT have any common characters.
#
# For every valid pair of words:
#
#     product = length(word1) * length(word2)
#
# We need to return the maximum product.
#
#
# ⭐ Main Idea:
#
# We use a BITMASK to represent the characters present in each word.
#
# There are only 26 lowercase English letters.
#
# We can represent each character using one bit:
#
#     a -> bit 0
#     b -> bit 1
#     c -> bit 2
#     ...
#     z -> bit 25
#
# For example:
#
#     word = "abc"
#
# Its bitmask will have bits for a, b, and c set to 1.
#
# If two words do not have any common character:
#
#     mask1 & mask2 == 0
#
# The bitwise AND is zero because they have no common set bits.
#
#
# 🔄 ALGORITHM
#
# 1. Create an empty list called masks.
#
# 2. For every word:
#       - Create a bitmask.
#       - For every character:
#             Find its position using:
#
#             ord(ch) - ord('a')
#
#       - Set that bit using:
#
#             mask |= (1 << bit)
#
#       - Store the mask.
#
# 3. Create answer = 0.
#
# 4. Compare every pair of words.
#
# 5. Check:
#
#       if masks[i] & masks[j] == 0
#
#    This means the two words have no common characters.
#
# 6. If they are valid:
#
#       product = len(words[i]) * len(words[j])
#
# 7. Update the maximum product.
#
# 8. Return answer.
#
#
# ⭐ KEY TRICK — BITMASK
#
# Suppose:
#
#     word1 = "abcw"
#     word2 = "xtfn"
#
# word1 contains:
#
#     a, b, c, w
#
# word2 contains:
#
#     x, t, f, n
#
# They have no common characters.
#
# Therefore:
#
#     mask1 & mask2 == 0
#
# So this is a valid pair.
#
#
# Then:
#
#     len("abcw") = 4
#     len("xtfn") = 4
#
#     product = 4 * 4 = 16
#
#
# 🧑‍💻 PYTHON CODE
#
class Solution:
    def maxProduct(self, words: list[str]) -> int:

        # Store the bitmask of every word
        masks = []

        # Create a bitmask for each word
        for word in words:

            # Initially, no characters are present
            mask = 0

            # Process every character in the word
            for ch in word:

                # Find the character position
                #
                # 'a' -> 0
                # 'b' -> 1
                # 'c' -> 2
                # ...
                # 'z' -> 25
                bit = ord(ch) - ord('a')

                # Set the corresponding bit to 1
                mask |= (1 << bit)

            # Store the mask of this word
            masks.append(mask)

        # Store the maximum product
        answer = 0

        # Compare every pair of words
        for i in range(len(words)):

            for j in range(i + 1, len(words)):

                # Check if the two words have no common characters
                #
                # If AND is 0, there are no common characters.
                if masks[i] & masks[j] == 0:

                    # Calculate the product of their lengths
                    product = len(words[i]) * len(words[j])

                    # Update the maximum product
                    answer = max(answer, product)

        # Return the maximum product
        return answer


# 🧪 DRY RUN
#
# Input:
#
#     words = ["abcw", "xtfn"]
#
#
# Word 1:
#
#     "abcw"
#
# Characters:
#
#     a, b, c, w
#
#
# Word 2:
#
#     "xtfn"
#
# Characters:
#
#     x, t, f, n
#
#
# There is no common character.
#
# Therefore:
#
#     mask1 & mask2 = 0
#
#
# Lengths:
#
#     len("abcw") = 4
#     len("xtfn") = 4
#
#
# Product:
#
#     4 * 4 = 16
#
#
# Therefore:
#
#     answer = 16
#
#
# 🎯 INTERVIEW EXPLANATION
#
# "I use a bitmask to represent the characters present in each word.
# Since there are only 26 lowercase English letters, each character
# can be represented using one bit.
#
# For every pair of words, I use bitwise AND between their masks.
# If the result is zero, the two words do not share any characters.
#
# Then I calculate the product of their lengths and keep track of
# the maximum product.
#
# Finally, I return the maximum product."
#
#
# ⭐ WHY BITMASK?
#
# Without a bitmask, we would need to repeatedly compare characters.
#
# With a bitmask, checking whether two words have a common character
# becomes very fast:
#
#     mask1 & mask2 == 0
#
# This is an efficient way to solve the problem because there are
# only 26 possible lowercase characters.
#
#
# ⏱️ COMPLEXITY
#
# Let:
#
#     n = number of words
#     L = total number of characters in all words
#
# Creating all bitmasks:
#
#     O(L)
#
# Comparing every pair:
#
#     O(n²)
#
# Therefore:
#
#     Time Complexity = O(L + n²)
#
#     Space Complexity = O(n)
#
# The O(n) space is used to store the bitmask of every word.