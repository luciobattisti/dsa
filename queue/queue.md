A **queue** is a linear data structure that follows the **First In, First Out (FIFO)** principle, meaning the first element added to the queue is the first one to be removed. It is similar to a real-world queue, like a line of people waiting for service.

---

### Key Characteristics:
1. **FIFO**: The first element added is the first one to be removed.
2. **Two Endpoints**: 
   - Elements are added at one end (called the **rear** or **back**).
   - Elements are removed from the other end (called the **front**).

---

### Main Methods:
1. **`enqueue(item)`**:
   - Adds an item to the rear of the queue.
   - Increases the size of the queue by one.

2. **`dequeue()`**:
   - Removes and returns the item from the front of the queue.
   - Decreases the size of the queue by one.
   - Raises an error (or returns a special value) if the queue is empty.

3. **`peek()`** (or **`front()`**):
   - Returns the item at the front of the queue without removing it.
   - Does not modify the size of the queue.

4. **`is_empty()`**:
   - Checks if the queue is empty.
   - Returns `True` if the queue has no elements, otherwise `False`.

5. **`size()`**:
   - Returns the number of elements currently in the queue.

---

### Variations:
- **Double-Ended Queue (Deque)**:
   - Supports insertion and deletion from both ends (front and rear).

- **Priority Queue**:
   - Elements are dequeued based on priority rather than arrival order.

---

### Example Use Cases:
- **Scheduling**: Task scheduling in operating systems or managing print jobs.
- **Breadth-First Search (BFS)**: Used to keep track of nodes during graph traversal.
- **Resource Management**: Handling requests in shared resources like printers or CPU processes.
- **Data Buffering**: Temporary storage for streaming data (e.g., in networking or audio/video processing).

Queues are commonly implemented using arrays, linked lists, or collections like Python's `collections.deque` for efficient operations.