//-------- 💡 Logic -----------
// 1. Create a HashMap.
//
//       key   → sorted version of string
//       value → list of anagrams
//
// 2. Take each string.
//
// 3. Convert the string into a character array.
//
// 4. Sort the character array.
//
// 5. Convert it back into a String.
//    This becomes the key.
//
// 6. Add the original string to that key's list.
//
// 7. Finally, return all values of the HashMap.

//----- Algorithm --------
// Step 1: Create HashMap<String, List<String>>.
//
// Step 2: Traverse every string in strs.
//
// Step 3: Convert the string to char[].
//
// Step 4: Sort the char[] using Arrays.sort().
//
// Step 5: Create a String key from the sorted array.
//
// Step 6: If the key does not exist,
//         create a new ArrayList.
//
// Step 7: Add the original string to the group.
//
// Step 8: Return all HashMap values.

//-------- Dry Run ----------
// Input:
// strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
//
// --------------------------------
//
// word = "eat"
//
// Sorted:
// "eat" → "aet"
//
// Map:
// aet → [eat]
//
// --------------------------------
//
// word = "tea"
//
// Sorted:
// "tea" → "aet"
//
// Map:
// aet → [eat, tea]
//
// --------------------------------
//
// word = "tan"
//
// Sorted:
// "tan" → "ant"
//
// Map:
// aet → [eat, tea]
// ant → [tan]
//
// --------------------------------
//
// word = "ate"
//
// Sorted:
// "ate" → "aet"
//
// Map:
// aet → [eat, tea, ate]
// ant → [tan]
//
// --------------------------------
//
// word = "nat"
//
// Sorted:
// "nat" → "ant"
//
// Map:
// aet → [eat, tea, ate]
// ant → [tan, nat]
//
// --------------------------------
//
// word = "bat"
//
// Sorted:
// "bat" → "abt"
//
// Map:
// aet → [eat, tea, ate]
// ant → [tan, nat]
// abt → [bat]
//
// --------------------------------
//
// Final Output:
//
// [[eat, tea, ate],
//  [tan, nat],
//  [bat]]
//
// Order does not matter.


import java.util.*;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        Map<String, List<String>> groups = new HashMap<>();

        for (String word : strs) {

            // Convert string to character array
            char[] chars = word.toCharArray();

            // Sort characters
            Arrays.sort(chars);

            // Create key
            String key = new String(chars);

            // Create group if key does not exist
            if (!groups.containsKey(key)) {
                groups.put(key, new ArrayList<>());
            }

            // Add word to its group
            groups.get(key).add(word);
        }

        return new ArrayList<>(groups.values());
    }
}

//------- 🎯 Interview Explanation -----------
// I use a HashMap to group anagrams.
//
// For every string, I sort its characters.
// Anagrams always produce the same sorted string.
//
// For example:
//
// "eat" → "aet"
// "tea" → "aet"
// "ate" → "aet"
//
// Therefore, "aet" can be used as the key.
//
// All strings having the same key are stored
// in the same list.
//
// Finally, I return all the values of the HashMap.
//
// Time Complexity:
// O(n * k log k)
//
// n = number of strings
// k = maximum length of a string
//
// Space Complexity:
// O(n * k)
//
// because we store the strings in the HashMap.

//------ ⭐ Key Trick -----------
// Anagrams → Same Sorted Key
//
// "eat" → "aet"
// "tea" → "aet"
// "ate" → "aet"
//
// Same key
//    ↓
// Same group