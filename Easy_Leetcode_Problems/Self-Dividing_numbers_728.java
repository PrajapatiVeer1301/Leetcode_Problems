
/*
## SELF-DIVIDING NUMBERS

## LOGIC:
## A self-dividing number is divisible by every digit it contains.
## A number containing digit 0 cannot be self-dividing.
## Check every number from left to right.
## Extract each digit using % 10 and remove it using / 10.
## If every digit divides the original number exactly, add it to the result.
*/

import java.util.*;

class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {

        // ## Store all valid self-dividing numbers.
        List<Integer> result = new ArrayList<>();

        // ## Check every number in the inclusive range [left, right].
        for (int num = left; num <= right; num++) {

            // ## Keep a copy of the original number.
            int temp = num;

            // ## Assume the number is self-dividing.
            boolean isSelfDividing = true;

            // ## Process every digit of the number.
            while (temp > 0) {

                // ## Extract the last digit.
                int digit = temp % 10;

                // ## If the digit is zero, the number is invalid.
                if (digit == 0) {
                    isSelfDividing = false;
                    break;
                }

                // ## Check if the original number is divisible by the digit.
                if (num % digit != 0) {
                    isSelfDividing = false;
                    break;
                }

                // ## Remove the last digit.
                temp = temp / 10;
            }

            // ## Add the number if all digits pass the checks.
            if (isSelfDividing) {
                result.add(num);
            }
        }

        // ## Return the list of valid numbers.
        return result;
    }
}

/*
## EXAMPLE:
## Input: left = 1, right = 22
## Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]


## DRY RUN:
## Input: left = 10, right = 15
##
## Number 10: Contains digit 0 -> Reject
## Number 11: Divisible by 1 and 1 -> Accept
## Number 12: Divisible by 1 and 2 -> Accept
## Number 13: 13 % 3 = 1 -> Reject
## Number 14: 14 % 4 = 2 -> Reject
## Number 15: Divisible by 1 and 5 -> Accept
##
## Final Output: [11, 12, 15]


## ALGORITHM:
## Step 1: Create an empty result list.
## Step 2: Iterate through each number from left to right.
## Step 3: Copy the current number into temp.
## Step 4: Extract the last digit using temp % 10.
## Step 5: If the digit is zero, reject the number.
## Step 6: If num % digit != 0, reject the number.
## Step 7: Remove the last digit using temp / 10.
## Step 8: If all digits are valid, add the number to result.
## Step 9: Return result.


## INTERVIEW EXPLANATION:
## I iterate through every number in the given range.
## For each number, I examine its digits one by one.
## I use modulo 10 to extract the last digit.
## If the digit is zero or does not divide the original number,
## I mark the number as invalid and stop checking it.
## Otherwise, I remove the last digit using integer division by 10.
## If every digit passes the checks, I add the number to the result.
## Finally, I return the list of self-dividing numbers.


## KEY TRICK:
## num % digit == 0 checks whether the original number
## is divisible by the current digit.
## temp % 10 extracts the last digit.
## temp / 10 removes the last digit because both values are integers.
## Always check digit == 0 before performing modulo by digit.


## TIME AND SPACE COMPLEXITY:
## Let n = right - left + 1 and M = right.
## Time Complexity: O(n * log M)
## Each number requires checking at most log10(M) digits.
##
## Space Complexity: O(n)
## The result list may contain up to n numbers.
*/

