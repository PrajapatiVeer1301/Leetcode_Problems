## ⭐ Main Logic
##
## We use a variable called `balance` to track the current
## depth of parentheses.
##
## When `(` comes:
##     balance += 1
##
## When `)` comes:
##     balance -= 1
##
## The outermost `(` of a primitive string occurs when
## balance is 0 before adding the `(`.
##
## The outermost `)` occurs when balance becomes 0 after
## removing the `)`.
##
## Therefore:
##
## - If `(` comes and balance == 0, it is the outermost `(`,
##   so we skip it.
##
## - If `)` makes balance == 0, it is the outermost `)`,
##   so we skip it.
##
## - All other parentheses are added to the result.


## 🔄 Algorithm
##
## 1. Create an empty string called `result`.
##
## 2. Initialize `balance = 0`.
##
## 3. Traverse every character of the string.
##
## 4. If the character is `(`:
##       - If balance > 0, add `(` to result.
##       - Increase balance by 1.
##
## 5. If the character is `)`:
##       - Decrease balance by 1.
##       - If balance > 0, add `)` to result.
##
## 6. Continue until all characters are processed.
##
## 7. Return the result.


## 🧑‍💻 Python Code

class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        ## Store the final answer
        result = ""

        ## Track the current parentheses depth
        balance = 0

        ## Traverse every character
        for ch in s:

            ## If it is an opening parenthesis
            if ch == '(':

                ## If balance is greater than 0,
                ## this is not the outermost '('
                if balance > 0:
                    result += ch

                ## Increase the balance
                balance += 1

            ## If it is a closing parenthesis
            else:

                ## Decrease the balance
                balance -= 1

                ## If balance is greater than 0,
                ## this is not the outermost ')'
                if balance > 0:
                    result += ch

        ## Return the string after removing
        ## the outermost parentheses
        return result


## 🧪 Dry Run
##
## Example:
##
## s = "(()())(())"
##
## First primitive:
##
## "(()())"
##
## Remove the outermost `(` and `)`:
##
## "()()"
##
## Second primitive:
##
## "(())"
##
## Remove the outermost `(` and `)`:
##
## "()"
##
## Final answer:
##
## "()()" + "()" = "()()()"


## 🎯 Interview Explanation
##
## "I use a balance variable to track the depth of parentheses.
## When an opening parenthesis appears at balance 0, it is the
## outermost parenthesis, so I do not add it to the result.
## For a closing parenthesis, I first decrease the balance.
## If the balance becomes 0, it is the outermost closing
## parenthesis, so I skip it.
## All other parentheses are added to the result."


## ⭐ Key Trick
##
## The important condition is:
##
## For `(`:
##     balance == 0 → skip it
##
## For `)`:
##     balance becomes 0 → skip it
##
## This automatically removes the outermost parentheses
## of every primitive substring.


## ⏱️ Complexity
##
## Time Complexity: O(n)
## Every character is processed exactly once.
##
## Space Complexity: O(n)
## The result can contain up to n characters.