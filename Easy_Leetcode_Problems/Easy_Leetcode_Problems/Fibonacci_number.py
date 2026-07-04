
# 🚀 LeetCode 509 - Fibonacci Number

# 📝 Problem
# Given an integer n.
# Return the nth Fibonacci number.
# The Fibonacci sequence starts with 0 and 1.
# Each next number is the sum of the previous two numbers.



# 💡 Logic
# Initialize the first two Fibonacci numbers as 0 and 1.
# Handle the base cases when n is 0 or 1.
# Use a loop to calculate the next Fibonacci number.
# Update the previous two numbers after each iteration.
# Return the nth Fibonacci number.



# 📌 Algorithm
# 1. If n is 0, return 0.
# 2. If n is 1, return 1.
# 3. Initialize a = 0 and b = 1.
# 4. Traverse from 2 to n.
# 5. Calculate c = a + b.
# 6. Update a = b and b = c.
# 7. Return b.



# 💻 Python Code


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1:
            return 1

        a = 0
        b = 1

        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c

        return b



# ⏱️ Time Complexity
# O(n)

# 📦 Space Complexity
# O(1)



# 🎯 Interview Explanation
# I used an iterative approach to solve this problem.
# First, I handled the base cases for n = 0 and n = 1.
# Then, I initialized the first two Fibonacci numbers.
# Using a loop, I calculated each next Fibonacci number.
# After every iteration, I updated the previous two values.
# Finally, I returned the nth Fibonacci number.
# This solution runs in O(n) time and O(1) extra space.



