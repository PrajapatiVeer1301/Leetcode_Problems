// ## LOGIC:
        // ## Each English letter has a corresponding Morse Code.
        // ## Convert every word into its Morse Code representation.
        // ## Store each complete transformation in a HashSet.
        // ## A HashSet stores only unique values and removes duplicates.
        // ## Return the number of unique transformations using size().

        
import java.util.*;

class Solution {

    public int uniqueMorseRepresentations(String[] words) {
        // ## Store the Morse Code for all 26 English letters.
        String[] morse = {
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
            "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
            "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
            "-.--", "--.."
        };

        // ## Create a HashSet to store unique Morse Code transformations.
        Set<String> transformations = new HashSet<>();

        // ## Process every word in the given array.
        for (String word : words) {

            // ## Store the Morse Code of the current word.
            StringBuilder code = new StringBuilder();

            // ## Convert each character into its Morse Code.
            for (char ch : word.toCharArray()) {

                // ## Find the letter's index: a = 0, b = 1, ..., z = 25.
                int index = ch - 'a';

                // ## Append the corresponding Morse Code.
                code.append(morse[index]);
            }

            // ## Add the complete transformation to the HashSet.
            // ## Duplicate transformations are stored only once.
            transformations.add(code.toString());
        }

        // ## Return the number of unique transformations.
        return transformations.size();
    }
}

/*
## EXAMPLE:
## Input: words = ["gin", "zen", "gig", "msg"]
##
## gin -> --...-.
## zen -> --...-.
## gig -> --...--.
## msg -> --...--.
##
## Output: 2


## DRY RUN:
## Step 1: Process "gin".
## Transformation = "--...-."
## Set = {"--...-."}
##
## Step 2: Process "zen".
## Transformation = "--...-."
## This transformation already exists in the set.
## Set remains unchanged.
##
## Step 3: Process "gig".
## Transformation = "--...--."
## Add this new transformation to the set.
## Set contains two unique transformations.
##
## Step 4: Process "msg".
## Transformation = "--...--."
## This transformation already exists in the set.
## Set remains unchanged.
##
## Final Output: 2


## ALGORITHM:
## Step 1: Create an array containing Morse Codes for all 26 letters.
## Step 2: Create an empty HashSet named transformations.
## Step 3: Traverse every word in words.
## Step 4: Create a StringBuilder for each word.
## Step 5: Convert each character into its Morse Code.
## Step 6: Append each Morse Code to the StringBuilder.
## Step 7: Add the complete transformation to the HashSet.
## Step 8: Return transformations.size().


## INTERVIEW EXPLANATION:
## First, I store the Morse Code for all 26 English letters.
## Then, I iterate through each word in the input array.
## For every character, I calculate its alphabet index using ch - 'a'.
## I use that index to find the corresponding Morse Code.
## I concatenate the Morse Codes using a StringBuilder.
## I insert each complete transformation into a HashSet to remove duplicates.
## Finally, I return the size of the HashSet to get the number
## of unique Morse Code representations.


## KEY TRICK:
## ch - 'a' converts a lowercase letter into an index.
## For example, 'a' -> 0, 'b' -> 1, and 'c' -> 2.
## A HashSet automatically stores each unique transformation only once.
## StringBuilder efficiently joins the Morse Codes.
## transformations.size() returns the number of unique transformations.


## TIME AND SPACE COMPLEXITY:
## Let N be the number of words and L be the maximum word length.
##
## Time Complexity: O(N * L)
## Each character is processed once, assuming bounded-size Morse codes.
##
## Space Complexity: O(N * L)
## The HashSet stores the unique Morse Code transformations.
*/
