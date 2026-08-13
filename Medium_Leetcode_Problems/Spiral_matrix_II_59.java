
// Logic:
//
// We use four boundaries:
//
// top    = first row
// bottom = last row
// left   = first column
// right  = last column
//
// We fill the matrix in 4 directions:
//
// 1. Left → Right
//    Fill the top row.
//
// 2. Top → Bottom
//    Fill the right column.
//
// 3. Right → Left
//    Fill the bottom row.
//
// 4. Bottom → Top
//    Fill the left column.
//
// After completing one outer layer,
// move the boundaries inward.
//
// Main idea:
//
// Top → Right → Bottom → Left
//              ↓
//        Move boundaries inward
//              ↓
//             Repeat


// Algorithm:
//
// 1. Create an n × n matrix.
//
// 2. Initialize:
//
//       top = 0
//       bottom = n - 1
//       left = 0
//       right = n - 1
//       num = 1
//
// 3. While top <= bottom and left <= right:
//
//       Fill top row from left to right.
//       top++
//
//       Fill right column from top to bottom.
//       right--
//
//       Fill bottom row from right to left.
//       bottom--
//
//       Fill left column from bottom to top.
//       left++
//
// 4. Return the matrix.

class Solution {
    public int[][] generateMatrix(int n) {

        int[][] matrix = new int[n][n];

        int top = 0;
        int bottom = n - 1;
        int left = 0;
        int right = n - 1;

        int num = 1;

        while (top <= bottom && left <= right) {

            // Left -> Right
            for (int col = left; col <= right; col++) {
                matrix[top][col] = num;
                num++;
            }
            top++;

            // Top -> Bottom
            for (int row = top; row <= bottom; row++) {
                matrix[row][right] = num;
                num++;
            }
            right--;

            // Right -> Left
            if (top <= bottom) {
                for (int col = right; col >= left; col--) {
                    matrix[bottom][col] = num;
                    num++;
                }
                bottom--;
            }

            // Bottom -> Top
            if (left <= right) {
                for (int row = bottom; row >= top; row--) {
                    matrix[row][left] = num;
                    num++;
                }
                left++;
            }
        }

        return matrix;
    }
}

// ----------Dry Run --------
// Input:
//
// n = 3
//
// Initial:
//
// [0, 0, 0]
// [0, 0, 0]
// [0, 0, 0]
//
// num = 1
//
// -------------------------
//
// Left → Right:
//
// [1, 2, 3]
// [0, 0, 0]
// [0, 0, 0]
//
// top = 1
//
// -------------------------
//
// Top → Bottom:
//
// [1, 2, 3]
// [0, 0, 4]
// [0, 0, 5]
//
// right = 1
//
// -------------------------
//
// Right → Left:
//
// [1, 2, 3]
// [0, 0, 4]
// [7, 6, 5]
//
// bottom = 1
//
// -------------------------
//
// Bottom → Top:
//
// [1, 2, 3]
// [8, 0, 4]
// [7, 6, 5]
//
// left = 1
//
// -------------------------
//
// Remaining center:
//
// [1, 2, 3]
// [8, 9, 4]
// [7, 6, 5]
//
// Final Answer:
//
// [[1,2,3],
//  [8,9,4],
//  [7,6,5]]

// Interview Explanation:
//
// I used four boundaries: top, bottom, left,
// and right to track the current layer.
//
// I fill the matrix in four directions:
//
// Left → Right
// Top → Bottom
// Right → Left
// Bottom → Top
//
// After completing each direction, I move the
// corresponding boundary inward.
//
// I repeat this process until all positions
// are filled with numbers from 1 to n².
//
// Time Complexity: O(n²)
//
// Space Complexity: O(n²)
// because we create the output matrix.


//-------- ⭐ Remember ----------
// Top → Right → Bottom → Left
//              ↓
//       Move boundaries inward
//              ↓
//            Repeat
