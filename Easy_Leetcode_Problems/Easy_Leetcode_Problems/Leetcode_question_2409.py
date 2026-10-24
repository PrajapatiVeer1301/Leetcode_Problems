
# ## ROBOT RETURN TO ORIGIN 2409

# ## LOGIC:
# ## The robot starts at position (0, 0).
# ## Use x to track horizontal movement and y to track vertical movement.
# ## R increases x by 1, and L decreases x by 1.
# ## U increases y by 1, and D decreases y by 1.
# ## If both x and y are zero after all moves, return True.
# ## Otherwise, return False.

class Solution:
    def judgeCircle(self, moves: str) -> bool:

        # ## Initialize the horizontal position.
        x = 0

        # ## Initialize the vertical position.
        y = 0

        # ## Process every move in the given string.
        for move in moves:

            # ## Move one step to the right.
            if move == 'R':
                x += 1

            # ## Move one step to the left.
            elif move == 'L':
                x -= 1

            # ## Move one step upward.
            elif move == 'U':
                y += 1

            # ## Move one step downward.
            elif move == 'D':
                y -= 1

        # ## Return True if the robot returns to the origin.
        return x == 0 and y == 0


# ## EXAMPLE:
# ## Input: moves = "UD"
# ## U moves the robot up one step.
# ## D moves the robot down one step.
# ## Final position = (0, 0)
# ## Output: True


# ## DRY RUN:
# ## Input: moves = "UDLR"
# ##
# ## Start: x = 0, y = 0
# ##
# ## Move U: x = 0, y = 1
# ## Move D: x = 0, y = 0
# ## Move L: x = -1, y = 0
# ## Move R: x = 0, y = 0
# ##
# ## Final position = (0, 0)
# ## Output: True


# ## ALGORITHM:
# ## Step 1: Initialize x = 0 and y = 0.
# ## Step 2: Traverse each character in moves.
# ## Step 3: If the move is R, increase x by 1.
# ## Step 4: If the move is L, decrease x by 1.
# ## Step 5: If the move is U, increase y by 1.
# ## Step 6: If the move is D, decrease y by 1.
# ## Step 7: Check whether x == 0 and y == 0.
# ## Step 8: Return True if both are zero; otherwise, return False.


# ## INTERVIEW EXPLANATION:
# ## I initialize the robot's horizontal and vertical positions to zero.
# ## I iterate through the moves string one character at a time.
# ## Right and left moves update the horizontal coordinate.
# ## Up and down moves update the vertical coordinate.
# ## After processing all moves, I check the final coordinates.
# ## If both coordinates are zero, the robot has returned to the origin.
# ## Otherwise, the robot has ended at a different position.


# ## KEY TRICK:
# ## R and L cancel each other when their counts are equal.
# ## U and D cancel each other when their counts are equal.
# ## The robot returns to the origin only when both coordinates are zero.
# ## Use x == 0 and y == 0 to check the final position.


# ## TIME AND SPACE COMPLEXITY:
# ## Let n be the length of the moves string.
# ##
# ## Time Complexity: O(n)
# ## Each move is processed exactly once.
# ##
# ## Space Complexity: O(1)
# ## Only two coordinate variables are used.
