# Bubble Sort

Bubble sort is a straightforward sorting algorithm that works by repeatedly "bubbling" the largest (or smallest) elements to their correct positions. Imagine you're sorting a list of numbers from smallest to largest. Here's a step-by-step rundown of how bubble sort accomplishes this:

1. **Start at the Beginning**: Begin with the first element in the list and compare it to the next element.
  
2. **Swap if Needed**: If the first element is greater than the second, swap their positions. If it's not, leave them as they are.

3. **Move to the Next Pair**: Now, move one position forward and compare the second element to the third. Again, swap if the second is greater than the third. Continue this way until you've reached the end of the list. By the end of this pass, the largest number will have moved (or "bubbled") to the end of the list.

4. **Repeat the Process**: Go back to the start of the list and repeat the same process, excluding the last element (since it’s now in the correct position). Each pass through the list will place the next largest element in its correct position.

5. **Stop Condition**: Continue repeating these passes until you complete a pass without making any swaps. At this point, the list is sorted.

Bubble sort is simple to implement and understand but isn’t very efficient for large lists, as it has a time complexity of **O(n^2)**. It’s best used for small or nearly sorted datasets, where its simplicity can be advantageous.