## 💡 Main Logic
##
## We use two nested loops to generate all possible subarrays.
##
## The outer loop selects the starting index of each subarray.
##
## The inner loop extends the subarray one element at a time.
##
## We use a set to store distinct elements.
##
## For every subarray:
##     1. Add the current element to the set.
##     2. Count the distinct elements using len(unique).
##     3. Calculate the square of the distinct count.
##     4. Add the square to the answer.
##
## Finally, return the total answer.


## 🔄 Algorithm
##
## 1. Initialize answer = 0.
##
## 2. Loop through every starting index i.
##
## 3. Create an empty set called unique.
##
## 4. Loop through every ending index j from i to n - 1.
##
## 5. Add nums[j] to the unique set.
##
## 6. Calculate the distinct count:
##       distinct_count = len(unique)
##
## 7. Add its square to answer:
##       answer += distinct_count * distinct_count
##
## 8. Return answer after processing all subarrays.


## 🧑‍💻 Python Code

from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:

        ## Find the length of the array
        n = len(nums)

        ## Store the sum of squared distinct counts
        answer = 0

        ## Select the starting index of each subarray
        for i in range(n):

            ## Store distinct elements for the current subarray
            unique = set()

            ## Extend the subarray from index i to n - 1
            for j in range(i, n):

                ## Add the current element to the set
                unique.add(nums[j])

                ## Count the distinct elements
                distinct_count = len(unique)

                ## Add the square of the distinct count
                answer += distinct_count * distinct_count

        ## Return the final answer
        return answer


## 🧪 Dry Run
##
## Input:
## nums = [1, 2, 1]
##
## Initially:
## answer = 0
##
## Starting index i = 0:
##
## Subarray [1]
## unique = {1}
## distinct_count = 1
## answer = 0 + 1 * 1 = 1
##
## Subarray [1, 2]
## unique = {1, 2}
## distinct_count = 2
## answer = 1 + 2 * 2 = 5
##
## Subarray [1, 2, 1]
## unique = {1, 2}
## distinct_count = 2
## answer = 5 + 2 * 2 = 9
##
## Starting index i = 1:
##
## Subarray [2]
## unique = {2}
## distinct_count = 1
## answer = 9 + 1 * 1 = 10
##
## Subarray [2, 1]
## unique = {1, 2}
## distinct_count = 2
## answer = 10 + 2 * 2 = 14
##
## Starting index i = 2:
##
## Subarray [1]
## unique = {1}
## distinct_count = 1
## answer = 14 + 1 * 1 = 15
##
## Final Output:
## 15


## 🎯 Interview Explanation
##
## "I use two nested loops to generate every possible subarray.
## For each starting index, I create an empty set to track
## distinct elements.
## As I extend the subarray, I add each new element to the set.
## I calculate the number of distinct elements, square that
## count, and add it to the answer.
## After processing all subarrays, I return the total sum."


## ⭐ Key Trick
##
## A set automatically stores only distinct elements.
##
## unique.add(nums[j])
##
## The number of distinct elements is:
##
## len(unique)
##
## Its square is:
##
## len(unique) * len(unique)
##
## Reset the set for each new starting index.


## ⏱️ Complexity
##
## Time Complexity: O(n^2) average
## There are O(n^2) subarrays, and set operations take
## O(1) average time.
##
## Space Complexity: O(n)
## The set can store up to n distinct elements.