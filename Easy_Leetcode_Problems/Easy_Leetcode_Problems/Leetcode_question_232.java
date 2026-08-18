//---------- 💡 Logic --------
// 1. Create two stacks.
//
//       stack1 = input stack
//       stack2 = output stack
//
// 2. push(x):
//       Push x into stack1.
//
// 3. pop():
//       If stack2 is empty,
//       move all elements from stack1 to stack2.
//
//       Then pop from stack2.
//
// 4. peek():
//       If stack2 is empty,
//       move all elements from stack1 to stack2.
//
//       Return top of stack2.
//
// 5. empty():
//       Return true only when both stacks are empty.

//-------- 🔄 Algorithm ------
// Step 1: Create two Stack<Integer>.
//
// Step 2: In push(x), push x into stack1.
//
// Step 3: In pop():
//
//       If stack2 is empty:
//           while stack1 is not empty:
//               stack2.push(stack1.pop())
//
//       return stack2.pop()
//
// Step 4: In peek():
//
//       If stack2 is empty:
//           transfer stack1 → stack2
//
//       return stack2.peek()
//
// Step 5: In empty():
//
//       return stack1.isEmpty() && stack2.isEmpty()


//------ Dry Run ----------

// Initially:
//
// stack1 = []
// stack2 = []
//
// --------------------------------
//
// push(1)
//
// stack1 = [1]
// stack2 = []
//
// Queue = [1]
//
// --------------------------------
//
// push(2)
//
// stack1 = [1,2]
// stack2 = []
//
// Queue = [1,2]
//
// --------------------------------
//
// peek()
//
// stack2 is empty.
//
// Transfer stack1 → stack2:
//
// stack1 = []
// stack2 = [2,1]
//
// Top of stack2 = 1
//
// peek() → 1
//
// --------------------------------
//
// pop()
//
// stack2 = [2,1]
//
// Pop 1:
//
// pop() → 1
//
// stack2 = [2]
//
// Queue = [2]
//
// --------------------------------
//
// empty()
//
// stack1 = []
// stack2 = [2]
//
// Both are NOT empty.
//
// empty() → false

import java.util.*;

class MyQueue {

    Stack<Integer> stack1;
    Stack<Integer> stack2;

    public MyQueue() {
        stack1 = new Stack<>();
        stack2 = new Stack<>();
    }

    public void push(int x) {
        stack1.push(x);
    }

    public int pop() {

        if (stack2.isEmpty()) {
            while (!stack1.isEmpty()) {
                stack2.push(stack1.pop());
            }
        }

        return stack2.pop();
    }

    public int peek() {

        if (stack2.isEmpty()) {
            while (!stack1.isEmpty()) {
                stack2.push(stack1.pop());
            }
        }

        return stack2.peek();
    }

    public boolean empty() {
        return stack1.isEmpty() && stack2.isEmpty();
    }
}


// --------- 🎯 Interview Explanation -----
// I implemented a FIFO queue using two stacks.
//
// stack1 stores newly inserted elements.
//
// stack2 is used to access the front element.
//
// When stack2 is empty, I transfer all elements
// from stack1 to stack2.
//
// This reverses their order, so the oldest element
// comes to the top of stack2.
//
// Therefore, pop() and peek() can work like a queue.
//
// Each element is transferred from stack1 to stack2
// at most once.
//
// Time Complexity:
//
// push()  → O(1)
// pop()   → Amortized O(1)
// peek()  → Amortized O(1)
// empty() → O(1)
//
// Space Complexity: O(n)

//------- ⭐ Key Trick -----
// stack1:
//
// [1, 2, 3]
//          ↑
//         top
//
// Transfer to stack2:
//
// [3, 2, 1]
//          ↑
//         top
//
// Now 1 comes out first.
//
// Stack LIFO
//     ↓
// Reverse using second stack
//     ↓
// Queue FIFO