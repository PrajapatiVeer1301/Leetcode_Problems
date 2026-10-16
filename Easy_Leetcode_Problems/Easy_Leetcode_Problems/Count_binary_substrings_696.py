# ## ⭐ Main Logic
# ##
# ## We use consecutive groups of identical characters.
# ## For example:
# ## s = "00110011"
# ## Groups = [2, 2, 2, 2]
# ##
# ## Every pair of adjacent groups can form valid substrings.
# ## The number of valid substrings is the minimum of
# ## the previous group length and the current group length.
# ##
# ## Formula:
# ## min(previous, current)
# ##
# ## Add this value to the answer whenever the character changes.


# ## 🔄 Algorithm
# ##
# ## 1. Initialize previous = 0, current = 1, answer = 0.
# ##
# ## 2. Start traversing the string from index 1.
# ##
# ## 3. If the current character equals the previous character:
# ##       Increase current by 1.
# ##
# ## 4. Otherwise:
# ##       Add min(previous, current) to answer.
# ##       Set previous = current.
# ##       Reset current = 1.
# ##
# ## 5. After the loop, add min(previous, current) to answer.
# ##
# ## 6. Return answer.


# ## 🧑‍💻 Python Code

class Solution:
    def countBinarySubstrings(self, s: str) -> int:

        # ## Length of the previous group of characters
        previous = 0

        # ## Length of the current group of characters
        current = 1

        # ## Store the total number of valid substrings
        answer = 0

        # ## Traverse the string from the second character
        for i in range(1, len(s)):

            # ## If consecutive characters are the same
            if s[i] == s[i - 1]:
                current += 1

            # ## If the character changes, a new group starts
            else:

                # ## Count valid substrings from adjacent groups
                answer += min(previous, current)

                # ## Move the current group to the previous group
                previous = current

                # ## Start counting the new group
                current = 1

        # ## Count valid substrings from the final two groups
        answer += min(previous, current)

        # ## Return the total number of valid substrings
        return answer


# ## 🧪 Dry Run
# ##
# ## Input:
# ## s = "00110011"
# ##
# ## Consecutive groups:
# ## [00] [11] [00] [11]
# ## Group lengths = [2, 2, 2, 2]
# ##
# ## Initially:
# ## previous = 0
# ## current = 1
# ## answer = 0
# ##
# ## First group: "00"
# ## current = 2
# ##
# ## Character changes from 0 to 1:
# ## answer += min(0, 2) = 0
# ## previous = 2
# ## current = 1
# ##
# ## Second group: "11"
# ## current = 2
# ##
# ## Character changes from 1 to 0:
# ## answer += min(2, 2) = 2
# ## previous = 2
# ## current = 1
# ##
# ## Third group: "00"
# ## current = 2
# ##
# ## Character changes from 0 to 1:
# ## answer += min(2, 2) = 2
# ## answer = 4
# ## previous = 2
# ## current = 1
# ##
# ## Fourth group: "11"
# ## current = 2
# ##
# ## After the loop:
# ## answer += min(2, 2) = 2
# ## Final answer = 6
# ##
# ## Output: 6
# ##
# ## Valid substrings:
# ## "01", "0011", "10", "1100", "01", "0011"
# ## Each occurrence is counted separately.


# ## 🎯 Interview Explanation
# ##
# ## "I count consecutive groups of identical characters.
# ## Whenever the character changes, I add the minimum of
# ## the previous group length and the current group length
# ## to the answer.
# ## This minimum represents the number of valid substrings
# ## that can be formed using those two adjacent groups.
# ## After processing the string, I count the final pair
# ## of groups and return the answer."


# ## ⭐ Key Trick
# ##
# ## Use:
# ## answer += min(previous, current)
# ##
# ## For example, groups of lengths 3 and 2 can form
# ## min(3, 2) = 2 valid substrings.
# ##
# ## We do not need to generate every substring.


# ## ⏱️ Complexity
# ##
# ## Time Complexity: O(n)
# ## Each character is processed once.
# ##
# ## Space Complexity: O(1)
# ## Only three variables are used.