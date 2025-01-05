Merge sort is a divide-and-conquer algorithm used for sorting that splits a list into smaller parts, sorts those parts, and then merges them back together in order. Here's a detailed explanation of how it works:

### How Merge Sort Works
1. **Divide**: The algorithm starts by dividing the list into two roughly equal halves. This division continues recursively until each sublist has only one element (since a single element is already considered sorted).

2. **Conquer**: Once the list is divided into the smallest units, the algorithm starts merging these sublists. During the merging process, the sublists are combined in a way that maintains order. This is done by comparing elements from each sublist and placing the smaller element into the merged list.

3. **Merge**: The merging process continues until all sublists are combined back into a single sorted list. Since the merging ensures that elements are placed in the correct order, the final result is a completely sorted list.

### Key Characteristics
- **Time Complexity**: Merge sort has a time complexity of O(n log n), making it more efficient than algorithms like bubble sort or selection sort for large lists.
- **Space Complexity**: Merge sort requires additional space proportional to the size of the input list, giving it a space complexity of O(n). This is because it uses temporary arrays to store the divided sublists.
- **Stability**: Merge sort is a stable sort, meaning that equal elements maintain their relative order from the original list.
- **Efficiency**: It performs well on large datasets and is preferred when stability and predictable performance are important.

### Example Walkthrough
Consider sorting the list ([6, 3, 8, 5, 2, 7, 4, 1]):

1. **Divide**: 
   - Split into: \([6, 3, 8, 5]\) and \([2, 7, 4, 1]\)
   - Further split: \([6, 3]\), \([8, 5]\), \([2, 7]\), \([4, 1]\)
   - Continue splitting: \([6]\), \([3]\), \([8]\), \([5]\), \([2]\), \([7]\), \([4]\), \([1]\)

2. **Merge**: 
   - Merge \([6]\) and \([3]\) into \([3, 6]\)
   - Merge \([8]\) and \([5]\) into \([5, 8]\)
   - Merge \([2]\) and \([7]\) into \([2, 7]\)
   - Merge \([4]\) and \([1]\) into \([1, 4]\)
   - Merge \([3, 6]\) and \([5, 8]\) into \([3, 5, 6, 8]\)
   - Merge \([2, 7]\) and \([1, 4]\) into \([1, 2, 4, 7]\)
   - Finally, merge \([3, 5, 6, 8]\) and \([1, 2, 4, 7]\) into \([1, 2, 3, 4, 5, 6, 7, 8]\)

The list is now sorted! Merge sort’s efficiency and consistent *O(n log n)* performance make it a powerful choice for many sorting tasks.