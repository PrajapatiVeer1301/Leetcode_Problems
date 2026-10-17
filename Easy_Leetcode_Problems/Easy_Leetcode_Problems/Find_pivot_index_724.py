## ⭐ Main Logic
##
## We use two variables:
##
## total = Sum of all elements in the array.
##
## left_sum = Sum of elements strictly to the left
## of the current index.
##
## For every index i, calculate the right sum using:
##
## right_sum = total - left_sum - nums[i]
##
## If left_sum == right_sum, the current index is
## the pivot index.
##
## We traverse from left to right, so the first pivot
## index found is the leftmost pivot index.
## If no pivot index exists, return -1.


## 🔄 Algorithm
##
## 1. Calculate the sum of all elements and store it in total.
##
## 2. Initialize left_sum = 0.
##
## 3. Traverse every index i in the array.
##
## 4. Calculate:
##    right_sum = total - left_sum - nums[i]
##
## 5. If left_sum == right_sum, return i.
##
## 6. Otherwise, add nums[i] to left_sum.
##
## 7. If no pivot index is found, return -1.


## 🧑‍💻 Python Code

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:

        ## Calculate the sum of the entire array
        total = sum(nums)

        ## Initialize the sum of elements on the left
        left_sum = 0

        ## Check each index from left to right
        for i in range(len(nums)):

            ## Calculate the sum of elements on the right
            right_sum = total - left_sum - nums[i]

            ## Check whether left and right sums are equal
            if left_sum == right_sum:
                return i

            ## Add the current element to the left sum
            left_sum += nums[i]

        ## Return -1 if no pivot index exists
        return -1


## 🧪 Dry Run
##
## Input:
## nums = [1, 7, 3, 6, 5, 6]
##
## total = 1 + 7 + 3 + 6 + 5 + 6 = 28
## left_sum = 0
##
## Index 0:
## nums[0] = 1
## right_sum = 28 - 0 - 1 = 27
## left_sum = 0, right_sum = 27
## Not equal.
## Update left_sum = 0 + 1 = 1
##
## Index 1:
## nums[1] = 7
## right_sum = 28 - 1 - 7 = 20
## left_sum = 1, right_sum = 20
## Not equal.
## Update left_sum = 1 + 7 = 8
##
## Index 2:
## nums[2] = 3
## right_sum = 28 - 8 - 3 = 17
## left_sum = 8, right_sum = 17
## Not equal.
## Update left_sum = 8 + 3 = 11
##
## Index 3:
## nums[3] = 6
## right_sum = 28 - 11 - 6 = 11
## left_sum = 11, right_sum = 11
## Both sums are equal!
##
## Final Output:
## 3


## 🎯 Interview Explanation
##
## "First, I calculate the total sum of the array.
## Then I traverse the array while maintaining the left sum.
## For each index, I calculate the right sum by subtracting
## the left sum and the current element from the total sum.
## If both sums are equal, I return that index immediately.
## Since I traverse from left to right, this gives the
## leftmost pivot index.
## If no pivot index is found, I return -1."


## ⭐ Key Trick
##
## right_sum = total - left_sum - nums[i]
##
## This formula calculates the right sum without using
## another loop.
##
## ⏱️ Complexity
##
## Time Complexity: O(n)
## Calculating the total and traversing the array take O(n).
##
## Space Complexity: O(1)
## Only a fixed number of extra variables are used.