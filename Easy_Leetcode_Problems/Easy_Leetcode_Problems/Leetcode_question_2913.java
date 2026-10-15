// ## 💡 Main Logic
// ##
// ## We use two nested loops to generate all possible subarrays.
// ##
// ## The outer loop selects the starting index of each subarray.
// ## The inner loop extends the subarray one element at a time.
// ##
// ## We use a HashSet to store distinct elements.
// ##
// ## For every subarray:
// ## 1. Add the current element to the set.
// ## 2. Count distinct elements using set.size().
// ## 3. Calculate the square of the distinct count.
// ## 4. Add the square to the answer.
// ##
// ## Finally, return the total answer.


// ## 🔄 Algorithm
// ##
// ## 1. Initialize answer = 0.
// ## 2. Loop through every starting index i.
// ## 3. Create an empty HashSet called unique.
// ## 4. Loop through every ending index j from i to n - 1.
// ## 5. Add nums[j] to the set.
// ## 6. Calculate the distinct count using unique.size().
// ## 7. Add its square to answer.
// ## 8. Return answer after processing all subarrays.


// ## 🧑‍💻 Java Code

import java.util.*;

class Solution {
    public int sumCounts(List<Integer> nums) {

        int n = nums.size();
        int answer = 0;

        for (int i = 0; i < n; i++) {
            Set<Integer> unique = new HashSet<>();

            for (int j = i; j < n; j++) {
                unique.add(nums.get(j));

                int distinctCount = unique.size();
                answer += distinctCount * distinctCount;
            }
        }

        return answer;
    }
}

// ## 🧪 Dry Run
// ##
// ## Input:
// ## nums = [1, 2, 1]
// ##
// ## Initially:
// ## answer = 0
// ##
// ## Starting index i = 0:
// ##
// ## Subarray [1]
// ## unique = {1}
// ## distinctCount = 1
// ## answer = 0 + 1 * 1 = 1
// ##
// ## Subarray [1, 2]
// ## unique = {1, 2}
// ## distinctCount = 2
// ## answer = 1 + 2 * 2 = 5
// ##
// ## Subarray [1, 2, 1]
// ## unique = {1, 2}
// ## distinctCount = 2
// ## answer = 5 + 2 * 2 = 9
// ##
// ## Starting index i = 1:
// ##
// ## Subarray [2]
// ## unique = {2}
// ## distinctCount = 1
// ## answer = 9 + 1 * 1 = 10
// ##
// ## Subarray [2, 1]
// ## unique = {1, 2}
// ## distinctCount = 2
// ## answer = 10 + 2 * 2 = 14
// ##
// ## Starting index i = 2:
// ##
// ## Subarray [1]
// ## unique = {1}
// ## distinctCount = 1
// ## answer = 14 + 1 * 1 = 15
// ##
// ## Final Output:
// ## 15


// ## 🎯 Interview Explanation
// ##
// ## "I use two nested loops to generate every possible subarray.
// ## For each starting index, I create a HashSet to track
// ## distinct elements.
// ## As I extend the subarray, I add each element to the set.
// ## I calculate the number of distinct elements, square that
// ## count, and add it to the answer.
// ## After processing all subarrays, I return the total sum."


// ## ⭐ Key Trick
// ##
// ## A HashSet automatically stores only distinct elements.
// ##
// ## unique.add(nums[j]);
// ##
// ## The number of distinct elements is:
// ## unique.size();
// ##
// ## Its square is:
// ## distinctCount * distinctCount
// ##
// ## Create a new set for each starting index.


// ## ⏱️ Complexity
// ##
// ## Time Complexity: O(n^2) average
// ## There are O(n^2) subarrays, and HashSet operations
// ## take O(1) average time.
// ##
// ## Space Complexity: O(n)
// ## The set can store up to n distinct elements.