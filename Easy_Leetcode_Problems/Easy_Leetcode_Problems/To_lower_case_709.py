## 💡 LOGIC
##
## We need to convert every uppercase letter in the string
## into its corresponding lowercase letter.
##
## Example:
##
## "Hello"  →  "hello"
## "LOVELY" →  "lovely"
## "here"   →  "here"
##
## The string may also contain numbers and special characters.
## These characters should remain unchanged.
##
##
## ⭐ KEY TRICK — ASCII
##
## Uppercase letters are between:
##
## 'A' to 'Z'
##
## Lowercase letters are between:
##
## 'a' to 'z'
##
## The ASCII difference between an uppercase letter
## and its lowercase letter is 32.
##
## For example:
##
## 'A' = 65
## 'a' = 97
##
## 65 + 32 = 97
##
## Therefore, we can convert an uppercase letter to lowercase
## using:
##
## chr(ord(ch) + 32)
##
##
## 🔄 ALGORITHM
##
## 1. Create an empty result string.
##
## 2. Traverse every character of the string.
##
## 3. Check whether the character is an uppercase letter:
##
##       'A' <= ch <= 'Z'
##
## 4. If it is uppercase:
##       Convert it to lowercase using ASCII values.
##
## 5. If it is already lowercase or is a special character:
##       Keep it unchanged.
##
## 6. Add the character to the result.
##
## 7. Return the final result.
##
##
## 🧑‍💻 PYTHON CODE

class Solution:
    def toLowerCase(self, s: str) -> str:

        ## Store the final result
        result = ""

        ## Traverse every character in the string
        for ch in s:

            ## Check if the character is uppercase
            if 'A' <= ch <= 'Z':

                ## Convert uppercase character to lowercase
                ## ASCII difference between uppercase and
                ## lowercase letters is 32
                ch = chr(ord(ch) + 32)

            ## Add the character to the result
            result += ch

        ## Return the converted string
        return result


## 🧪 DRY RUN
##
## Example:
##
## s = "Hello"
##
## Process each character:
##
## H → h
## e → e
## l → l
## l → l
## o → o
##
## Final result:
##
## "hello"
##
## Answer = "hello"
##
##
## 🎯 INTERVIEW EXPLANATION
##
## "I traverse the string character by character.
## If the current character is an uppercase letter between
## A and Z, I convert it to lowercase using its ASCII value.
##
## The ASCII difference between an uppercase and lowercase
## letter is 32, so I add 32 to the uppercase character.
##
## If the character is already lowercase or is another
## printable character, I keep it unchanged.
##
## Finally, I return the resulting string."
##
##
## ⏱️ COMPLEXITY
##
## Time Complexity: O(n)
##
## Every character is processed exactly once.
##
## Space Complexity: O(n)
##
## We create a new string containing the converted characters.
##
## Here, n is the length of the input string.
##
##
## ⭐ IMPORTANT POINT
##
## We are not using the built-in lower() method.
## Instead, we manually convert uppercase letters using
## ASCII values.