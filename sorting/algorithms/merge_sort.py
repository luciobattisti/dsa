# Implementation of merge sort algorithm

def merge(a: list, b: list) -> list:

    i = 0
    j = 0
    c = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    while i < len(a):
        c.append(a[i])
        i += 1

    while j < len(b):
        c.append(b[j])
        j += 1

    return c


def merge_sort(a: list) -> list:

    # Base case
    if len(a) == 1:
        return a

    # Recursive case
    m = len(a) // 2
    l = merge_sort(a[0:m])
    r = merge_sort(a[m:len(a)])

    return merge(l, r)


a = [2, 3, 5, 4, 1, 7, 10, 9]
print(f"Before: {a}")
sorted_a = merge_sort(a)
print(f"After: {sorted_a}")
