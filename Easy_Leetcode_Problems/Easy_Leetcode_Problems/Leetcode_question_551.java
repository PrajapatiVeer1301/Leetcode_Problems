
class Solution {
    public boolean checkRecord(String s) {

        // ## LOGIC:
        // A student is eligible for the award if:
        // 1. Total absences are fewer than 2.
        // 2. There are no 3 consecutive late days.

        // Count the total number of absent days.
        int absentCount = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'A') {
                absentCount++;
            }
        }

        // If absences are 2 or more, return false.
        if (absentCount >= 2) {
            return false;
        }

        // Check for 3 consecutive late days.
        if (s.contains("LLL")) {
            return false;
        }

        // If both conditions are satisfied, return true.
        return true;
    }
}

/*
## EXAMPLE:
Input:  s = "PPALLP"
Output: true

## DRY RUN:
s = "PPALLP"

Step 1: Count absent days.
A appears 1 time.
absentCount = 1

Step 2: Check whether absentCount >= 2.
1 >= 2 is false.

Step 3: Check whether "LLL" exists.
It does not exist.

Output = true

## ALGORITHM:
1. Count the number of 'A' characters.
2. If the count is 2 or more, return false.
3. If the string contains "LLL", return false.
4. Otherwise, return true.

## INTERVIEW EXPLANATION:
I count the total absences by traversing the string.
If the student has two or more absences, they are not eligible.
I also check whether the string contains three consecutive
late days using contains("LLL"). If neither rule is violated,
I return true.

## KEY TRICK:
s.contains("LLL") checks for three consecutive late days.

## TIME COMPLEXITY:
O(n), where n is the length of the string.

## SPACE COMPLEXITY:
O(1), because only a fixed number of variables are used.
*/
