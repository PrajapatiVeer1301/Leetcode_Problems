// ## 💡 Logic
// ##
// ## We are given an integer array nums.
// ## The length of the array is n.
// ##
// ## An element is special if its 1-based index i divides n
// ## completely, meaning n % i == 0.
// ##
// ## For every special element:
// ##     - Find its square.
// ##     - Add the square to the answer.
// ##
// ## Java uses 0-based indexing, so we access the element
// ## at position i using nums[i - 1].
// ##
// ## Finally, return the total sum of squares.


// ## 🔄 Algorithm
// ##
// ## 1. Find the length of the array and store it in n.
// ##
// ## 2. Initialize answer = 0.
// ##
// ## 3. Run a loop from index 1 to n.
// ##
// ## 4. Check whether n % i == 0.
// ##
// ## 5. If the condition is true:
// ##       - Access nums[i - 1].
// ##       - Calculate its square.
// ##       - Add the square to answer.
// ##
// ## 6. Return answer.


// ## 🧑‍💻 Java Code

class Solution {
    public int sumOfSquares(int[] nums) {

        // ## Find the length of the array
        int n = nums.length;

        // ## Store the sum of squares
        int answer = 0;

        // ## Check every 1-based index
        for (int i = 1; i <= n; i++) {

            // ## Check whether the index divides n
            if (n % i == 0) {

                // ## Add the square of the special element
                answer += nums[i - 1] * nums[i - 1];
            }
        }

        // ## Return the final sum
        return answer;
    }
}


// ## 🧪 Dry Run
// ##
// ## Input:
// ## nums = [1, 2, 3, 4]
// ##
// ## n = 4
// ## answer = 0
// ##
// ## i = 1:
// ## 4 % 1 == 0, so index 1 is special.
// ## Element = nums[0] = 1
// ## answer = 0 + 1 * 1 = 1
// ##
// ## i = 2:
// ## 4 % 2 == 0, so index 2 is special.
// ## Element = nums[1] = 2
// ## answer = 1 + 2 * 2 = 5
// ##
// ## i = 3:
// ## 4 % 3 != 0, so index 3 is not special.
// ## answer = 5
// ##
// ## i = 4:
// ## 4 % 4 == 0, so index 4 is special.
// ## Element = nums[3] = 4
// ## answer = 5 + 4 * 4 = 21
// ##
// ## Final Output:
// ## 21


// ## 🎯 Interview Explanation
// ##
// ## "First, I find the length of the array.
// ## Then I check every 1-based index to determine whether
// ## it divides the array length exactly.
// ## If the index is special, I square the corresponding
// ## element and add it to the answer.
// ## Since Java uses 0-based indexing, I access it using
// ## nums[i - 1].
// ## Finally, I return the total sum of squares."


// ## ⭐ Key Trick
// ##
// ## The important condition is:
// ## n % i == 0
// ##
// ## It checks whether index i is a divisor of n.
// ##
// ## Remember:
// ## 1-based index i corresponds to nums[i - 1] in Java.


// ## ⏱️ Complexity
// ##
// ## Time Complexity: O(n)
// ## We check every index exactly once.
// ##
// ## Space Complexity: O(1)
// ## We use only a fixed number of extra variables.