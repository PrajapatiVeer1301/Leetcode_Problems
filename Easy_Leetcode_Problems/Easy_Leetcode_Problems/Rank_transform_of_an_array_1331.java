// Logic:
//
// 1. Create a copy of the original array.
//
// 2. Sort the copied array.
//
// 3. Assign ranks to unique elements using a HashMap.
//
// 4. Traverse the original array.
//
// 5. Replace each element with its corresponding rank.
//
// 6. Return the ranked array.


// Algorithm:
//
// 1. Clone the original array.
//
// 2. Sort the cloned array.
//
// 3. Create a HashMap to store element → rank.
//
// 4. Traverse the sorted array.
//    - If the element is not in the HashMap,
//      assign the next rank.
//
// 5. Create a result array.
//
// 6. Traverse the original array.
//    - Store the rank of each element in the result.
//
// 7. Return the result array.


import java.util.*;

class Solution {
    public int[] arrayRankTransform(int[] arr) {

        int[] temp = arr.clone();
        Arrays.sort(temp);

        HashMap<Integer, Integer> map = new HashMap<>();
        int rank = 1;

        for (int i = 0; i < temp.length; i++) {
            if (!map.containsKey(temp[i])) {
                map.put(temp[i], rank);
                rank++;
            }
        }

        for (int i = 0; i < arr.length; i++) {
            arr[i] = map.get(arr[i]);
        }

        return arr;
    }
}


// Interview Explanation:
//
// 1. I copied and sorted the original array.
//
// 2. Then, I assigned ranks only to unique elements
//    using a HashMap.
//
// 3. Finally, I traversed the original array
//    and replaced each element with its assigned rank.
//
// 4. Using a HashMap makes rank lookup very fast.
//
// Time Complexity: O(n log n)
// Space Complexity: O(n)