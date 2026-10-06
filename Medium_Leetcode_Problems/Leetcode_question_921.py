## 💡 LOGIC
##
## We need to find the minimum number of parentheses
## that must be inserted to make the string valid.
##
## We use two variables:
##
## balance -> number of unmatched opening brackets '('
## answer  -> number of parentheses that need to be inserted
##
##
## When we find '(':
##
##     balance += 1
##
## Because we have one unmatched opening bracket.
##
##
## When we find ')':
##
## If balance > 0:
##
##     balance -= 1
##
## The ')' can match with an existing '('.
##
## Otherwise, if balance == 0:
##
##     answer += 1
##
## There is no '(' available for this ')'.
## Therefore, we need to insert one '(' before it.
##
##
## At the end:
##
## If balance is greater than 0, some '(' are still unmatched.
## Each unmatched '(' needs one ')' to close it.
##
## Therefore:
##
##     answer += balance
##
##
## ⭐ KEY TRICK
##
## We do not need a stack.
##
## We only need to track the number of unmatched brackets.
##
## Final answer:
##
##     answer = unmatched ')' + unmatched '('
##
##
## 🔄 ALGORITHM
##
## 1. Initialize:
##
##       balance = 0
##       answer = 0
##
## 2. Traverse every character of the string.
##
## 3. If the character is '(':
##
##       balance += 1
##
## 4. If the character is ')':
##
##       If balance > 0:
##           balance -= 1
##
##       Otherwise:
##           answer += 1
##
## 5. After processing the entire string:
##
##       answer += balance
##
## 6. Return answer.
##
##
## 🧑‍💻 PYTHON CODE

class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        ## Store the number of unmatched opening brackets
        balance = 0

        ## Store the number of parentheses that need to be inserted
        answer = 0

        ## Traverse every character in the string
        for ch in s:

            ## If it is an opening bracket
            if ch == '(':

                ## Increase the number of unmatched '('
                balance += 1

            ## If it is a closing bracket
            else:

                ## If an opening bracket is available
                if balance > 0:

                    ## Match ')' with the existing '('
                    balance -= 1

                else:

                    ## No '(' is available.
                    ## We need to insert one '('.
                    answer += 1

        ## Any remaining '(' needs a corresponding ')'
        answer += balance

        ## Return the minimum number of insertions
        return answer


## 🧪 DRY RUN — EXAMPLE 1
##
## s = "())"
##
## Initially:
##
## balance = 0
## answer = 0
##
##
## Process '(':
##
## balance = 1
## answer = 0
##
##
## Process ')':
##
## balance > 0
##
## balance = 0
## answer = 0
##
##
## Process ')':
##
## balance = 0
##
## No '(' is available.
##
## answer = 1
##
##
## End:
##
## balance = 0
## answer = 1
##
## Output = 1
##
##
## 🧪 DRY RUN — EXAMPLE 2
##
## s = "((("
##
## Initially:
##
## balance = 0
## answer = 0
##
##
## Process '(':
##
## balance = 1
##
## Process '(':
##
## balance = 2
##
## Process '(':
##
## balance = 3
##
##
## End:
##
## balance = 3
## answer = 0
##
## Three '(' are unmatched.
## Therefore, three ')' must be inserted.
##
## answer = 0 + 3
## answer = 3
##
## Output = 3
##
##
## 🎯 INTERVIEW EXPLANATION
##
## "I use a balance counter to track unmatched opening brackets.
## Whenever I see an opening bracket, I increase the balance.
##
## When I see a closing bracket, if there is an unmatched
## opening bracket, I decrease the balance because the brackets
## can be matched.
##
## If there is no unmatched opening bracket, the current
## closing bracket cannot be matched, so I need to insert
## one opening bracket and increment the answer.
##
## After processing the complete string, any remaining opening
## brackets need closing brackets. Therefore, I add the remaining
## balance to the answer.
##
## This gives the minimum number of insertions without using
## a stack."
##
##
## ⏱️ COMPLEXITY
##
## Time Complexity: O(n)
##
## We traverse the string only once.
##
## Space Complexity: O(1)
##
## We use only two variables:
##
##     balance
##     answer
##
##
## ⭐ IMPORTANT POINT
##
## We do not need to actually insert the brackets.
##
## We only count how many brackets are missing.
##
##     answer = unmatched ')' + unmatched '('
##
## Therefore, the solution uses O(1) extra space.