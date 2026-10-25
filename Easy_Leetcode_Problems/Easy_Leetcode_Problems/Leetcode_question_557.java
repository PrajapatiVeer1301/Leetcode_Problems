// ## LOGIC:
        // Split the sentence into individual words.
        // Reverse each word separately.
        // Keep the original order of the words.
        
class Solution {
    public String reverseWords(String s) {

        String[] words = s.split(" ");

        // Use StringBuilder to store the final result.
        StringBuilder result = new StringBuilder();

        // Reverse each word one by one.
        for (int i = 0; i < words.length; i++) {

            // Convert the current word into StringBuilder
            // and reverse its characters.
            String reversedWord =
                new StringBuilder(words[i]).reverse().toString();

            // Add a space before every word except the first word.
            if (i > 0) {
                result.append(" ");
            }

            // Add the reversed word to the result.
            result.append(reversedWord);
        }

        // Return the final reversed sentence.
        return result.toString();
    }
}

/*
## EXAMPLE:
Input:  "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

## DRY RUN:
Input = "Mr Ding"

Step 1: Split the string.
words = ["Mr", "Ding"]

Step 2: Reverse each word.
"Mr"   -> "rM"
"Ding" -> "gniD"

Step 3: Join the words with spaces.
Output = "rM gniD"

## ALGORITHM:
1. Split the sentence into words using split(" ").
2. Create an empty StringBuilder.
3. Reverse each word using StringBuilder.reverse().
4. Append each reversed word to the result.
5. Add spaces between the words.
6. Return the final string.

## INTERVIEW EXPLANATION:
I split the sentence into individual words and reverse
each word using StringBuilder.reverse(). I then append
each reversed word to the result while preserving the
original order of the words.

## KEY TRICK:
new StringBuilder(word).reverse().toString()
reverses the characters of a word in Java.

## TIME COMPLEXITY:
O(n), where n is the length of the input string.

## SPACE COMPLEXITY:
O(n), because we store the words and the result.
*/
