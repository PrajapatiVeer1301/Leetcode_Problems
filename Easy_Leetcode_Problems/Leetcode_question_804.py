
# ## UNIQUE MORSE CODE REPRESENTATIONS

# ## LOGIC:
# ## Each English letter has a corresponding Morse Code.
# ## Convert every word into its Morse Code representation.
# ## Store each complete transformation in a set.
# ## A set stores only unique values and automatically removes duplicates.
# ## Return the number of unique transformations using len().

class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:

        # ## Store the Morse Code for all 26 English letters.
        morse = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
            "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
            "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
            "-.--", "--.."
        ]

        # ## Create a set to store unique Morse Code transformations.
        transformations = set()

        # ## Process every word in the given list.
        for word in words:

            # ## Store the Morse Code of the current word.
            code = ""

            # ## Convert each letter into its Morse Code.
            for ch in word:

                # ## Find the letter's index: a = 0, b = 1, ..., z = 25.
                index = ord(ch) - ord('a')

                # ## Append the corresponding Morse Code to the word.
                code += morse[index]

            # ## Add the complete transformation to the set.
            # ## Duplicate transformations are stored only once.
            transformations.add(code)

        # ## Return the number of unique transformations.
        return len(transformations)


# ## EXAMPLE:
# ## Input: words = ["gin", "zen", "gig", "msg"]
# ##
# ## gin -> --...-.
# ## zen -> --...-.
# ## gig -> --...--.
# ## msg -> --...--.
# ##
# ## Output: 2


# ## DRY RUN:
# ## Input: words = ["gin", "zen", "gig", "msg"]
# ##
# ## Step 1: Process "gin".
# ## Transformation = "--...-."
# ## Set = {"--...-."}
# ##
# ## Step 2: Process "zen".
# ## Transformation = "--...-."
# ## This transformation already exists in the set.
# ## Set remains {"--...-."}
# ##
# ## Step 3: Process "gig".
# ## Transformation = "--...--."
# ## Add this new transformation to the set.
# ## Set contains two unique transformations.
# ##
# ## Step 4: Process "msg".
# ## Transformation = "--...--."
# ## This transformation already exists in the set.
# ## Set remains unchanged.
# ##
# ## Final Output: 2


# ## ALGORITHM:
# ## Step 1: Create a list containing Morse Codes for all 26 letters.
# ## Step 2: Create an empty set named transformations.
# ## Step 3: Traverse every word in words.
# ## Step 4: Create an empty string named code for each word.
# ## Step 5: Convert each letter into its Morse Code.
# ## Step 6: Append each letter's Morse Code to code.
# ## Step 7: Add the complete code to the transformations set.
# ## Step 8: Return len(transformations).


# ## INTERVIEW EXPLANATION:
# ## First, I store the Morse Code for all 26 English letters.
# ## Then, I iterate through each word in the input list.
# ## For every character, I calculate its alphabet index using
# ## ord(ch) - ord('a') and use that index to get its Morse Code.
# ## I concatenate the Morse Codes to form the complete transformation.
# ## I insert each transformation into a set to remove duplicates.
# ## Finally, I return the size of the set, which gives the number
# ## of unique Morse Code representations.


# ## KEY TRICK:
# ## ord(ch) - ord('a') converts a lowercase letter into an index.
# ## For example, 'a' -> 0, 'b' -> 1, and 'c' -> 2.
# ## A set automatically stores each unique transformation only once.
# ## len(transformations) returns the number of unique transformations.


# ## TIME AND SPACE COMPLEXITY:
# ## Let N be the number of words and L be the maximum word length.
# ##
# ## Time Complexity: O(N * L)
# ## Each character is processed once, assuming bounded-size Morse codes.
# ##
# ## Space Complexity: O(N * L)
# ## The set stores the unique Morse Code transformations.
