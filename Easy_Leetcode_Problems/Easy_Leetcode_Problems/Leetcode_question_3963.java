
class Solution {
    public String[] createGrid(int m, int n) {

        // ## LOGIC:
        // Fill the entire grid with '#'.
        // Make the first row '.'.
        // Make the last column '.'.
        // This creates exactly one valid path from
        // the top-left cell to the bottom-right cell.

        // Create a grid of size m x n.
        char[][] grid = new char[m][n];

        // Fill every cell with an obstacle.
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                grid[i][j] = '#';
            }
        }

        // Open every cell in the first row.
        for (int j = 0; j < n; j++) {
            grid[0][j] = '.';
        }

        // Open every cell in the last column.
        for (int i = 0; i < m; i++) {
            grid[i][n - 1] = '.';
        }

        // Convert each row into a String.
        String[] result = new String[m];

        for (int i = 0; i < m; i++) {
            result[i] = new String(grid[i]);
        }

        // Return the grid.
        return result;
    }
}

/*
## EXAMPLE:
Input: m = 2, n = 3

Output:
["...", "##."]

## DRY RUN:
Step 1: Fill all cells with '#'.

###
###

Step 2: Open the first row.

...
###

Step 3: Open the last column.

...
##.

Final output: ["...", "##."]

Unique path:
(0,0) -> (0,1) -> (0,2) -> (1,2)

## ALGORITHM:
1. Create an m x n character grid.
2. Fill all cells with '#'.
3. Change the first row to '.'.
4. Change the last column to '.'.
5. Convert each row into a String.
6. Return the String array.

## INTERVIEW EXPLANATION:
I initialize every cell as an obstacle. Then I open
the first row and the last column. The only valid path
moves right along the first row and then down the last
column, so exactly one valid path exists.

## KEY TRICK:
First row = '.'
Last column = '.'
All remaining cells = '#'

## TIME COMPLEXITY:
O(m * n), because we initialize the entire grid.

## SPACE COMPLEXITY:
O(m * n), because we store the grid.
*/
