
class Solution {
    public int countPrimeSetBits(int left, int right) {

        // ## LOGIC:
        // ## Count the number of 1s in the binary representation of each number.
        // ## If the number of set bits is prime, increase the count.
        // ## Return the total count of numbers with a prime number of set bits.

        // ## Store all possible prime set-bit counts for this constraint.
        // ## Since right <= 10^6, a number has at most 20 set bits.
        int[] primes = {2, 3, 5, 7, 11, 13, 17, 19};

        // ## Initialize the count of valid numbers.
        int count = 0;

        // ## Check every number in the inclusive range [left, right].
        for (int num = left; num <= right; num++) {

            // ## Count the set bits (1s) in the binary representation.
            int setBits = Integer.bitCount(num);

            // ## Check whether the set-bit count is prime.
            for (int prime : primes) {
                if (setBits == prime) {

                    // ## Increase the count if the set-bit count is prime.
                    count++;
                    break;
                }
            }
        }

        // ## Return the total number of valid integers.
        return count;
    }
}

/*
## EXAMPLE:
## Input: left = 6, right = 10
##
## 6  -> 110  -> 2 set bits -> Prime -> Count = 1
## 7  -> 111  -> 3 set bits -> Prime -> Count = 2
## 8  -> 1000 -> 1 set bit  -> Not prime -> Count = 2
## 9  -> 1001 -> 2 set bits -> Prime -> Count = 3
## 10 -> 1010 -> 2 set bits -> Prime -> Count = 4
##
## Output: 4


## ALGORITHM:
## Step 1: Store the possible prime set-bit counts.
## Step 2: Initialize count = 0.
## Step 3: Iterate through every number from left to right.
## Step 4: Use Integer.bitCount(num) to count the 1 bits.
## Step 5: Check whether the set-bit count is prime.
## Step 6: If it is prime, increment count.
## Step 7: Return count.


## INTERVIEW EXPLANATION:
## I iterate through every number in the given range.
## I use Integer.bitCount(num) to count the 1s in its binary representation.
## Then, I check whether this count belongs to the list of prime numbers.
## If it does, I increment the counter.
## Finally, I return the total count of valid numbers.


## KEY TRICK:
## Integer.bitCount(num) counts the 1 bits in an integer.
## The maximum possible set-bit count is 19 for numbers up to 10^6.
## Therefore, checking prime counts from 2 to 19 is sufficient.
## A set-bit count of 1 is not prime.


## TIME AND SPACE COMPLEXITY:
## Let N = right - left + 1.
##
## Time Complexity: O(N)
## Each number needs a constant number of bit-count and prime checks.
##
## Auxiliary Space Complexity: O(1)
## Only a fixed-size array and a few variables are used.
*/
