
# ## COUNT PRIME SET BITS

# ## LOGIC:
# ## Count the number of 1s in the binary representation of each number.
# ## If the number of set bits is prime, increase the count.
# ## Return the total count of numbers with a prime number of set bits.

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:

        # ## Store all possible prime set-bit counts.
        # ## Since right <= 10^6, a number has at most 20 binary digits.
        primes = {2, 3, 5, 7, 11, 13, 17, 19}

        # ## Initialize the count of valid numbers.
        count = 0

        # ## Check every number in the inclusive range [left, right].
        for num in range(left, right + 1):

            # ## Count the 1s in the binary representation.
            set_bits = bin(num).count('1')

            # ## Check whether the set-bit count is prime.
            if set_bits in primes:

                # ## Increase the count if the set-bit count is prime.
                count += 1

        # ## Return the total number of valid integers.
        return count


# ## EXAMPLE:
# ## Input: left = 6, right = 10
# ##
# ## 6  -> 110  -> 2 set bits -> Prime -> Count = 1
# ## 7  -> 111  -> 3 set bits -> Prime -> Count = 2
# ## 8  -> 1000 -> 1 set bit  -> Not prime -> Count = 2
# ## 9  -> 1001 -> 2 set bits -> Prime -> Count = 3
# ## 10 -> 1010 -> 2 set bits -> Prime -> Count = 4
# ##
# ## Output: 4


# ## DRY RUN:
# ## Input: left = 6, right = 10
# ##
# ## Step 1: Check number 6.
# ## Binary = 110, set bits = 2, which is prime.
# ## Count = 1
# ##
# ## Step 2: Check number 7.
# ## Binary = 111, set bits = 3, which is prime.
# ## Count = 2
# ##
# ## Step 3: Check number 8.
# ## Binary = 1000, set bits = 1, which is not prime.
# ## Count = 2
# ##
# ## Step 4: Check number 9.
# ## Binary = 1001, set bits = 2, which is prime.
# ## Count = 3
# ##
# ## Step 5: Check number 10.
# ## Binary = 1010, set bits = 2, which is prime.
# ## Count = 4
# ##
# ## Final Output: 4


# ## ALGORITHM:
# ## Step 1: Create a set containing possible prime set-bit counts.
# ## Step 2: Initialize count = 0.
# ## Step 3: Iterate through every number from left to right.
# ## Step 4: Use bin(num).count('1') to count its set bits.
# ## Step 5: Check whether the set-bit count exists in the prime set.
# ## Step 6: If it exists, increment count.
# ## Step 7: Return count.


# ## INTERVIEW EXPLANATION:
# ## I iterate through every number in the given range.
# ## I use bin(num).count('1') to count the 1s in its binary representation.
# ## Then, I check whether the number of set bits is prime.
# ## I store the possible prime counts in a set for fast lookup.
# ## If the set-bit count is prime, I increment the counter.
# ## Finally, I return the total count of valid numbers.


# ## KEY TRICK:
# ## bin(num).count('1') counts the set bits of a number.
# ## A set allows fast membership checks using "in".
# ## A set-bit count of 1 is not prime.
# ## Since right <= 10^6, at most 19 set bits can occur.
# ## Therefore, checking prime counts from 2 to 19 is sufficient.


# ## TIME AND SPACE COMPLEXITY:
# ## Let N = right - left + 1.
# ##
# ## Time Complexity: O(N)
# ## Each number requires a bounded number of bit-counting and lookup operations.
# ##
# ## Auxiliary Space Complexity: O(1)
# ## The prime set has a fixed size, and only a few extra variables are used.
