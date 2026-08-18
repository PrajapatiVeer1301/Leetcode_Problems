# ---------- 💡 Logic ----------

# 1. Create two stacks.
#    stack1 = input stack
#    stack2 = output stack
#
# 2. push(x):
#    Push x into stack1.
#
# 3. pop():
#    If stack2 is empty,
#    move all elements from stack1 to stack2.
#    Then pop from stack2.
#
# 4. peek():
#    If stack2 is empty,
#    move all elements from stack1 to stack2.
#    Return top of stack2.
#
# 5. empty():
#    Return True only when both stacks are empty.


# ---------- 🔄 Algorithm ----------

# Step 1: Create two empty stacks:
#         stack1 = []
#         stack2 = []
#
# Step 2: For push(x):
#         stack1.append(x)
#
# Step 3: For pop():
#         If stack2 is empty:
#             while stack1 is not empty:
#                 stack2.append(stack1.pop())
#
#         return stack2.pop()
#
# Step 4: For peek():
#         If stack2 is empty:
#             while stack1 is not empty:
#                 stack2.append(stack1.pop())
#
#         return stack2[-1]
#
# Step 5: For empty():
#         return not stack1 and not stack2


# ---------- 🧪 Dry Run ----------

# Input:
# push(1)
# push(2)
# peek()
# pop()
# empty()
#
# --------------------------------
#
# Initially:
# stack1 = []
# stack2 = []
#
# --------------------------------
#
# push(1)
#
# stack1 = [1]
# stack2 = []
#
# Queue = [1]
#
# --------------------------------
#
# push(2)
#
# stack1 = [1, 2]
# stack2 = []
#
# Queue = [1, 2]
#
# --------------------------------
#
# peek()
#
# stack2 is empty.
#
# Transfer stack1 → stack2:
#
# stack1 = []
# stack2 = [2, 1]
#
# Top of stack2 = 1
#
# peek() → 1
#
# --------------------------------
#
# pop()
#
# stack2 = [2, 1]
#
# Remove top element:
#
# pop() → 1
#
# stack2 = [2]
#
# Queue = [2]
#
# --------------------------------
#
# empty()
#
# stack1 = []
# stack2 = [2]
#
# Both stacks are NOT empty.
#
# empty() → False


# ---------- 🐍 Python Code ----------

class MyQueue:

    def __init__(self):
        # Create two empty stacks
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        # Add new element to stack1
        self.stack1.append(x)

    def pop(self) -> int:
        # If stack2 is empty, transfer elements
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        # Remove and return front element
        return self.stack2.pop()

    def peek(self) -> int:
        # If stack2 is empty, transfer elements
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        # Return front element
        return self.stack2[-1]

    def empty(self) -> bool:
        # Queue is empty when both stacks are empty
        return not self.stack1 and not self.stack2


# ---------- 🎯 Interview Explanation ----------

# I implemented a FIFO queue using two stacks.
#
# stack1 stores newly inserted elements.
#
# stack2 is used to access the front element.
#
# When stack2 is empty, I transfer all elements
# from stack1 to stack2.
#
# This reverses their order, so the oldest element
# comes to the top of stack2.
#
# Therefore, pop() and peek() work like a queue.
#
# Each element is transferred from stack1 to stack2
# at most once.
#
# Time Complexity:
# push()  → O(1)
# pop()   → Amortized O(1)
# peek()  → Amortized O(1)
# empty() → O(1)
#
# Space Complexity:
# O(n)


# ---------- ⭐ Key Trick ----------

# stack1:
# [1, 2, 3]
#          ↑
#         top
#
# Transfer to stack2:
# [3, 2, 1]
#          ↑
#         top
#
# Now 1 comes out first.
#
# Stack:
# LIFO
#   ↓
# Reverse using second stack
#   ↓
# Queue:
# FIFO