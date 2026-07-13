# Logic:
#
# 1. Store the string "123456789".
#
# 2. Generate all possible sequential numbers
#    by taking substrings.
#
# 3. Convert each substring into an integer.
#
# 4. If the number lies between low and high,
#    add it to the answer.
#
# 5. Sort the answer.
#
# 6. Return the result.

# Algorithm:
#
# 1. Create the string "123456789".
#
# 2. Initialize an empty answer list.
#
# 3. Loop over possible lengths.
#
# 4. Generate every substring of that length.
#
# 5. Convert the substring to an integer.
#
# 6. If low <= number <= high,
#    add it to the answer list.
#
# 7. Sort the answer.
#
# 8. Return the answer.

from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        digits = "123456789"
        result = []

        for length in range(len(str(low)), len(str(high)) + 1):

            for i in range(10 - length):

                num = int(digits[i:i + length])

                if low <= num <= high:
                    result.append(num)

        result.sort()

        return result
    

# Interview Explanation:
#
# 1. I stored the digits "123456789" in a string.
#
# 2. Then I generated all possible sequential numbers
#    using substrings.
#
# 3. I converted each substring into an integer.
#
# 4. If the number was within the given range,
#    I added it to the result.
#
# 5. Finally, I sorted and returned the result.
#
# Time Complexity: O(1)
# Space Complexity: O(1)
