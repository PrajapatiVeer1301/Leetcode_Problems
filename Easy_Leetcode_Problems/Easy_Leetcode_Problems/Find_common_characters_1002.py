
class Solution:
    def commonChars(self, words: list[str]) -> list[str]:

        # ## LOGIC:
        # Count the frequency of each character in the first word.
        # For every next word, count its characters.
        # Keep the minimum frequency of each character.
        # Add each common character to the answer according
        # to its minimum frequency.

        # ## ALGORITHM:
        # 1. Count characters in the first word.
        # 2. Traverse all remaining words.
        # 3. Count characters in each word.
        # 4. Update each character's frequency to the minimum
        #    of its current frequency and the new word's frequency.
        # 5. Add common characters to the result.
        # 6. Return the result.

        # ## CODE:

        # Store the character frequencies of the first word.
        common = [0] * 26

        for ch in words[0]:
            common[ord(ch) - ord('a')] += 1

        # Check every remaining word.
        for word in words[1:]:

            # Count characters in the current word.
            freq = [0] * 26

            for ch in word:
                freq[ord(ch) - ord('a')] += 1

            # Keep only the minimum frequency for each character.
            for i in range(26):
                common[i] = min(common[i], freq[i])

        # Build the answer using the common frequencies.
        result = []

        for i in range(26):
            for _ in range(common[i]):
                result.append(chr(i + ord('a')))

        return result


# ## DRY RUN:
# Input: words = ["bella", "label", "roller"]
#
# Step 1: Count characters in "bella".
# a = 1, b = 1, e = 1, l = 2
#
# Step 2: Check "label".
# Keep only the minimum frequency of each character.
# a = 1, b = 1, e = 1, l = 2
#
# Step 3: Check "roller".
# a = 0, b = 0, e = 1, l = 2
#
# Step 4: Add characters with positive frequencies.
# e appears 1 time.
# l appears 2 times.
#
# Output: ["e", "l", "l"]


# ## INTERVIEW EXPLANATION:
# I count the characters in the first word using an array
# of size 26. For every other word, I count its characters
# and update the common frequency using the minimum count.
# Finally, I add each character to the result according to
# its remaining frequency and return the list.


# ## TIME COMPLEXITY:
# O(n * k + 26 * n), where n is the number of words
# and k is the maximum length of a word.
# Since 26 is constant, this simplifies to O(n * k).


# ## SPACE COMPLEXITY:
# O(1) auxiliary space for the two frequency arrays,
# because each array always has 26 elements.
# The output list requires additional space.


# ## TRICK TO REMEMBER:
# Common characters = minimum frequency in every word.
# Use ord(ch) - ord('a') to get the character's array index.
# Use min() to keep only the characters shared by all words.
