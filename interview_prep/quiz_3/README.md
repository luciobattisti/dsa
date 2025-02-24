## **📌 Code Challenge: Implement a Least Recently Used (LRU) Cache**
### **Objective**  
Design a **Least Recently Used (LRU) Cache** data structure that follows these rules:  
✅ Stores **key-value pairs**.  
✅ When the cache reaches its **capacity**, it removes the **least recently used item** before adding a new one.  
✅ Supports **O(1) operations** for `get(key)` and `put(key, value)`.  

---

### **📌 Requirements**
1️⃣ **Implement an `LRUCache` class** with:
   - `get(key)`: Retrieve the value associated with `key`. **Returns -1 if not found**.
   - `put(key, value)`: Insert or update a key-value pair. If the cache reaches capacity, **remove the least recently used item**.
   
2️⃣ The class should use **O(1) time complexity** for both operations using **OrderedDict** or a combination of a **HashMap + Doubly Linked List**.  

3️⃣ **Capacity constraint**: The cache should store only a fixed number of items.

---

### **📌 Example Usage**
```python
cache = LRUCache(2)  # Capacity = 2

cache.put(1, "A")
cache.put(2, "B")
print(cache.get(1))   # Output: "A"

cache.put(3, "C")     # Removes key 2 (Least Recently Used)
print(cache.get(2))   # Output: -1 (Not found)

cache.put(4, "D")     # Removes key 1
print(cache.get(1))   # Output: -1
print(cache.get(3))   # Output: "C"
print(cache.get(4))   # Output: "D"
```

---

### **⏳ Time: 30 minutes**