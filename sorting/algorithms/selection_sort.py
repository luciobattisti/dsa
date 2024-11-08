# Implementation of selection sort algorithm

def find_smallest(a: list, j: int) -> int:
    v = a[j]
    k = j

    for i in range(j, len(a)):
        if a[i] < a[k]:
            k = i

    return k


def selection_sort(a: list):
    p1 = 0

    while p1 < len(a)-1:
        p2 = find_smallest(a, p1)
        a[p1], a[p2] = a[p2], a[p1]

        p1 += 1


a = [4, 5, 2, 3, 1]
print(f"Before: {a}")
selection_sort(a)
print(f"After: {a}")

