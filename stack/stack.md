A **stack** is a linear data structure that follows the **Last In, First Out (LIFO)** principle, meaning the last element added to the stack is the first one to be removed. It is similar to a stack of plates, where you can only add or remove plates from the top.

### Key Characteristics:
1. **LIFO**: Last element added is the first to be removed.
2. **Restricted Access**: Elements can only be added (pushed) or removed (popped) from the top of the stack.
3. **Single Endpoint**: Operations occur at one end (the "top" of the stack).

---

### Main Methods:
1. **`push(item)`**:
   - Adds an item to the top of the stack.
   - Increases the size of the stack by one.
   
2. **`pop()`**:
   - Removes and returns the item from the top of the stack.
   - Decreases the size of the stack by one.
   - Raises an error (or returns a special value) if the stack is empty.

3. **`peek()`** (or **`top()`**):
   - Returns the item at the top of the stack without removing it.
   - Does not modify the size of the stack.

4. **`is_empty()`**:
   - Checks if the stack is empty.
   - Returns `True` if the stack has no elements, otherwise `False`.

5. **`size()`**:
   - Returns the number of elements currently in the stack.

---

### Example Use Cases:
- **Backtracking**: Undo operations in applications like text editors or navigating browser history.
- **Expression Evaluation**: Used in parsing or evaluating mathematical expressions (e.g., infix to postfix conversion).
- **Depth-First Search (DFS)**: To keep track of nodes in graph traversal. 
- **Call Stack**: Used in function calls to maintain the order of execution in programming. 

Stacks can be implemented using arrays, lists, or linked lists depending on the required performance and memory constraints.