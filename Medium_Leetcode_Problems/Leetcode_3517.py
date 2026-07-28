# Logic:
#
# 1. Count the frequency of each character.
#
# 2. Build the first half of the palindrome
#    using frequency // 2 characters
#    in alphabetical order.
#
# 3. Find the middle character
#    (frequency is odd).
#
# 4. Reverse the first half
#    to create the second half.
#
# 5. Return:
#
#    firstHalf + middle + secondHalf

# Algorithm:
#
# 1. Count each character.
#
# 2. Traverse characters from 'a' to 'z'.
#
# 3. Add (count // 2) copies
#    to the first half.
#
# 4. If count is odd,
#    store it as the middle character.
#
# 5. Reverse the first half.
#
# 6. Return:
#
#    firstHalf + middle + reversed(firstHalf)

from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:

        count = Counter(s)

        first_half = []
        middle = ""

        for ch in sorted(count.keys()):

            first_half.append(ch * (count[ch] // 2))

            if count[ch] % 2 == 1:
                middle = ch

        first = "".join(first_half)

        return first + middle + first[::-1]

    # Interview Explanation:
#
# 1. I counted the frequency of each character.
#
# 2. I built the first half of the palindrome
#    using half of each character's count
#    in alphabetical order.
#
# 3. If a character had an odd count,
#    I placed one occurrence in the middle.
#
# 4. I reversed the first half
#    to form the second half.
#
# 5. This guarantees the smallest
#    lexicographical palindrome.
#
# Time Complexity: O(n)
#
# Space Complexity: O(n)