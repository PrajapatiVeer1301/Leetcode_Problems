// Logic:
//
// 1. Find the size of the matrix.
//
// 2. Transpose the matrix
//    by swapping:
//
//      matrix[i][j]
//      matrix[j][i]
//
// 3. Reverse every row.
//
// 4. The matrix becomes
//    rotated by 90° clockwise.

// Algorithm:
//
// 1. Find n.
//
// 2. Perform transpose.
//
// 3. Reverse each row.
//
// 4. Matrix is rotated
//    by 90° clockwise.

// Dry Run:
//
// Input:
//
// 1 2 3
// 4 5 6
// 7 8 9
//
// ----------------------
//
// Step 1
//
// Transpose
//
// 1 4 7
// 2 5 8
// 3 6 9
//
// ----------------------
//
// Step 2
//
// Reverse Row 1
//
// 7 4 1
//
// Reverse Row 2
//
// 8 5 2
//
// Reverse Row 3
//
// 9 6 3
//
// ----------------------
//
// Final Output
//
// 7 4 1
// 8 5 2
// 9 6 3



class Solution {
    public void rotate(int[][] matrix) {

        int n = matrix.length;

        // Step 1: Transpose
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {

                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }

        // Step 2: Reverse each row
        for (int i = 0; i < n; i++) {

            int left = 0;
            int right = n - 1;

            while (left < right) {

                int temp = matrix[i][left];
                matrix[i][left] = matrix[i][right];
                matrix[i][right] = temp;

                left++;
                right--;
            }
        }
    }
}

// Interview Explanation:
//
// 1. Since creating another
//    matrix is not allowed,
//    I performed the rotation
//    in-place.
//
// 2. First, I transposed the
//    matrix by swapping rows
//    and columns.
//
// 3. Then, I reversed every row.
//
// 4. Transpose followed by
//    reversing each row gives
//    a 90° clockwise rotation.
//
// Time Complexity: O(n²)



//⭐ Easy Interview Trick

// Space Complexity: O(1)

//90° Clockwise Rotation

//Step 1 → Transpose
//(Row ↔ Column)

//Step 2 → Reverse Every Row

//Remember:

//Transpose + Reverse Row = 90° Clockwise

//Reverse Row + Transpose = 90° Anti-Clockwise