# Implementation of quick sort algorithm

def partition(a: list, p: int, l: int, r: int) -> int:

    # Move  pivot at the end of the list
    a[p], a[r] = a[r], a[p]

    # Set store index to left index
    s = l

    # Perform comparisons
    while l < r:
        if a[l] < a[r]:
            a[l], a[s] = a[s], a[l]
            s += 1
        l += 1

    # Move pivot back to its position
    a[s], a[r] = a[r], a[s]

    return s


def quick_sort_helper(a: list, l: int, r: int):

    # Base case
    if l >= r:
        return

    # Recursive case
    p = l + (r - l) // 2

    p = partition(a, p, l, r)

    quick_sort_helper(a, l, p-1)
    quick_sort_helper(a, p+1, r)

    return


def quick_sort(a: list):

    l = 0
    r = len(a) -1

    quick_sort_helper(a, l, r)


a = [8, 3, 1, 7, 0, 10, 2]
print(f"Before: {a}")
quick_sort(a)
print(f"After: {a}")

a = [8, 3, 1]
print(f"Before: {a}")
quick_sort(a)
print(f"After: {a}")

a = [8, 3]
print(f"Before: {a}")
quick_sort(a)
print(f"After: {a}")
