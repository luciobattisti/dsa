### **Core Idea**
Binary search divides the search space in half at each step. By comparing the target value to the middle element of the current range, it determines which half of the range to search next. This process continues until the target value is found or the search space is empty.

---

### **Steps of Binary Search**

1. **Initial Setup**:
   - Start with two pointers: 
     - `low`: Points to the first element of the array.
     - `high`: Points to the last element of the array.

2. **Find the Middle Element**:
   - Compute the middle index as:  
     `middle = (low + high) / 2` 
   - Compare the element at the middle index with the target value.

3. **Narrow Down the Search Space**:
   - If the middle element equals the target, the search is complete.
   - If the middle element is greater than the target, adjust the `high` pointer to focus on the left half of the array (values smaller than the middle).
   - If the middle element is less than the target, adjust the `low` pointer to focus on the right half of the array (values larger than the middle).

4. **Repeat**:
   - Continue the process of halving the search space until:
     - The target is found, or
     - The `low` pointer surpasses the `high` pointer, indicating the target is not in the array.

---

### **Key Characteristics**
- **Efficiency**: Binary search has a time complexity of O(log n), making it much faster than a linear search O(n) for large arrays.
- **Requirement**: The array must be sorted beforehand for binary search to work.
- **Iterative or Recursive**: The process can be implemented using either iteration or recursion.

---

### **Example Walkthrough**
Let’s search for the number `6` in the sorted array `[1, 3, 5, 6, 8, 10, 12]`.

1. **Initial Step**:
   - `low = 0` (pointing to `1`), `high = 6` (pointing to `12`).
   - Middle index: *middle = (0 + 6) / 2 = 3*
   - Middle element: `6`.
   - Since the middle element equals the target, the search ends successfully.

2. **If Target Was Not at Middle**:
   - If searching for `8`, after comparing with `6`, the new range becomes `[8, 10, 12]` (adjust `low` to 4).
   - Continue the process until the target is found or the search range is exhausted.

---

Binary search is highly intuitive once you practice dividing and narrowing search ranges!