
class Solution:
    def customSortString(self, order: str, s: str) -> str:

        # ## LOGIC:
        # Count how many times each character appears in s.
        # Traverse order and add each character according
        # to its frequency.
        # Then add characters that are not present in order.

        # Count the frequency of every character in s.
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Store the final answer.
        result = []

        # Add characters according to the custom order.
        for ch in order:
            if ch in freq:
                result.append(ch * freq[ch])

                # Remove the character after adding it.
                del freq[ch]

        # Add characters that were not in order.
        for ch in freq:
            result.append(ch * freq[ch])

        # Convert the list into a string.
        return "".join(result)


# ## EXAMPLE:
# Input:
# order = "cba"
# s = "abcd"
#
# Output: "cbad"

# ## DRY RUN:
# order = "cba"
# s = "abcd"
#
# Step 1: Count characters in s.
# freq = {'a': 1, 'b': 1, 'c': 1, 'd': 1}
#
# Step 2: Traverse order.
# 'c' -> Add 'c'
# 'b' -> Add 'b'
# 'a' -> Add 'a'
#
# result = ['c', 'b', 'a']
#
# Step 3: 'd' is not in order.
# Add 'd'.
#
# Final result = "cbad"

# ## ALGORITHM:
# 1. Count the frequency of each character in s.
# 2. Traverse each character in order.
# 3. Add that character according to its frequency.
# 4. Remove the processed character from the frequency map.
# 5. Add all remaining characters.
# 6. Return the final string.

# ## INTERVIEW EXPLANATION:
# I use a frequency dictionary to count the characters
# in s. Then I traverse order and append each character
# according to its frequency. Finally, I append characters
# that do not appear in order and return the result.

# ## KEY TRICK:
# freq.get(ch, 0) + 1 counts characters.
# ch * freq[ch] repeats a character the required number of times.

# ## TIME COMPLEXITY:
# O(n + k), where n is the length of s and k is the
# length of order.

# ## SPACE COMPLEXITY:
# O(n), for the frequency dictionary and output.
