# Logic:
#
# 1. Create two arrays:
#    - One for Roman numeral values.
#    - One for Roman symbols.
#
# 2. Start from the largest Roman value.
#
# 3. While the number is greater than or equal to that value:
#    - Append the corresponding Roman symbol.
#    - Subtract the value from the number.
#
# 4. Repeat until the number becomes 0.
#
# 5. Return the Roman numeral string.

# Algorithm:
#
# 1. Store Roman values in descending order.
#
# 2. Store their corresponding Roman symbols.
#
# 3. Initialize an empty result string.
#
# 4. Traverse all Roman values.
#
# 5. While num >= current value:
#    - Append the corresponding Roman symbol.
#    - Subtract the value from num.
#
# 6. Return the final Roman numeral.

class Solution:
    def intToRoman(self, num: int) -> str:

        values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        symbols = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

        result = ""

        for i in range(len(values)):
            while num >= values[i]:
                result += symbols[i]
                num -= values[i]

        return result
    
    # Interview Explanation:
#
# 1. I stored all Roman numeral values and symbols
#    in descending order.
#
# 2. Starting from the largest value,
#    I checked whether the number was greater than
#    or equal to the current Roman value.
#
# 3. If yes, I appended the corresponding Roman symbol
#    and subtracted its value from the number.
#
# 4. I repeated this process until the number became 0.
#
# 5. Finally, I returned the Roman numeral string.
#
# Time Complexity: O(1)
# Space Complexity: O(1)