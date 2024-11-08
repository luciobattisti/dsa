# Implementation of quick sort algorithm

def swap(a: list, p: int, l: int, r: int) -> int:

    # Swap pivot at the end of the list
    a[p], a[r] = a[r], a[p]

    # Set store index to left index
    s = l

    # Perform comparisons
    while l < r:
        if a[l] < a[r]:
            a[l], a[s] = a[s], a[l]
            s += 1
        l += 1

    # Swap pivot in its position
    a[s], a[r] = a[r], a[s]

    return s


def quick_sort(a: list, l: int, r: int):
    # Calculate len
    L = r - l + 1

    # Define base case
    if L <=1:
        return

    # Define recursive case
    p = l + (r - l) // 2

    p = swap(a, p, l, r)

    quick_sort(a, l, p-1)
    quick_sort(a, p+1, r)

    return


a = [8, 3, 1, 7, 0, 10, 2]
print(f"Before: {a}")
quick_sort(a, 0, len(a)-1)
print(f"After: {a}")

a = [8, 3, 1]
print(f"Before: {a}")
quick_sort(a, 0, len(a)-1)
print(f"After: {a}")

a = [8, 3]
print(f"Before: {a}")
quick_sort(a, 0, len(a)-1)
print(f"After: {a}")
