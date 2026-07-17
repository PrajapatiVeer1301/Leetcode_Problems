// Logic:
//
// 1. Copy and sort the score array.
//
// 2. Traverse the sorted array from highest to lowest.
//
// 3. Assign:
//    - Gold Medal
//    - Silver Medal
//    - Bronze Medal
//    - Rank number
//
// 4. Store score → rank in a HashMap.
//
// 5. Traverse the original array.
//
// 6. Return the rank of each score.

// Algorithm:
//
// 1. Clone the score array.
//
// 2. Sort the cloned array.
//
// 3. Create a HashMap.
//
// 4. Traverse from the largest score.
//
// 5. Assign medals or rank numbers.
//
// 6. Create the answer array.
//
// 7. Traverse the original array.
//
// 8. Fill the answer using the HashMap.
//
// 9. Return the answer.



import java.util.*;

class Solution {
    public String[] findRelativeRanks(int[] score) {

        int[] sorted = score.clone();
        Arrays.sort(sorted);

        HashMap<Integer, String> map = new HashMap<>();

        int n = sorted.length;

        for (int i = n - 1; i >= 0; i--) {

            int rank = n - i;

            if (rank == 1) {
                map.put(sorted[i], "Gold Medal");
            } 
            else if (rank == 2) {
                map.put(sorted[i], "Silver Medal");
            } 
            else if (rank == 3) {
                map.put(sorted[i], "Bronze Medal");
            } 
            else {
                map.put(sorted[i], String.valueOf(rank));
            }
        }

        String[] answer = new String[n];

        for (int i = 0; i < n; i++) {
            answer[i] = map.get(score[i]);
        }

        return answer;
    }
}

// Interview Explanation:
//
// 1. I copied and sorted the score array.
//
// 2. Then I traversed it from the highest score
//    to the lowest score.
//
// 3. I assigned Gold, Silver and Bronze medals
//    to the top three athletes.
//
// 4. The remaining athletes received
//    their rank number.
//
// 5. I stored the score-to-rank mapping
//    in a HashMap.
//
// 6. Finally, I traversed the original array
//    and returned the ranks in the original order.
//
// Time Complexity: O(n log n)
// Space Complexity: O(n)