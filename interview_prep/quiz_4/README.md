Got it! Here’s a **LeetCode-style 30-minute DSA challenge** for you. 🚀  

---

### **📌 Problem: Longest Substring Without Repeating Characters**  
**Difficulty:** Medium  
**Time Limit:** 30 minutes  

### **📝 Description**
Given a string `s`, find the **length of the longest substring** without repeating characters.  

---

### **📌 Example 1**
```python
Input: s = "abcabcbb"
Output: 3
Explanation: The longest substring without repeating characters is "abc", with a length of 3.
```

### **📌 Example 2**
```python
Input: s = "bbbbb"
Output: 1
Explanation: The longest substring without repeating characters is "b", with a length of 1.
```

### **📌 Example 3**
```python
Input: s = "pwwkew"
Output: 3
Explanation: The longest substring without repeating characters is "wke", with a length of 3.
```

---

### **📌 Constraints**
- `0 <= s.length <= 5 * 10⁴`
- `s` consists of English letters, digits, symbols, and spaces.

---

### **📌 Your Task**
1. Implement the function:
   ```python
   def length_of_longest_substring(s: str) -> int:
   ```
2. Optimize for **O(n) time complexity** using **Sliding Window** or **HashSet**.
3. Your function should return an integer representing the length of the longest substring **without repeating characters**.

---

### **⏳ Time: 30 minutes**