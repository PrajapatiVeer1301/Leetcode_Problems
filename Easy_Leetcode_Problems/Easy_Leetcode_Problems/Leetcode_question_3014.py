# Logic:
#
# 1. Traverse every character.
#
# 2. Every 8 characters,
#    increase the push count.
#
# 3. Add the current push count
#    to the answer.
#
# 4. Return the total pushes.

# Algorithm:
#
# 1. Initialize answer = 0.
#
# 2. Traverse the word using index.
#
# 3. Push count is:
#
#      (index // 8) + 1
#
# 4. Add it to answer.
#
# 5. Return answer.

class Solution:
    def minimumPushes(self, word: str) -> int:

        pushes = 0

        for i in range(len(word)):
            pushes += (i // 8) + 1

        return pushes

# Interview Explanation:
#
# 1. Since there are 8 available keys,
#    the first 8 letters can each be
#    assigned to a different key and
#    require only 1 push.
#
# 2. The next 8 letters require 2 pushes,
#    then the next 8 require 3 pushes,
#    and so on.
#
# 3. For each character at index i,
#    the required pushes are:
#
#       (i // 8) + 1
#
# 4. I summed these values for all
#    characters and returned the total.
#
# Time Complexity: O(n)
#
# Space Complexity: O(1)

