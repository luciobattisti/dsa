# Implementation of Bubble Sort algorithm

def bubble_sort(a: list):
    p1 = 0
    p2 = len(a) - 1
    n_swaps = 0

    while p1 < p2:
        for i in range(p1, p2):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                n_swaps += 1

        if n_swaps == 0:
            print("no_swaps")
            return

        p2 -= 1
        n_swaps = 0


a = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

print(f"Before: {a}")
bubble_sort(a)
print(f"After: {a}")

a = [1, 2, 3, 4, 5]

print(f"Before: {a}")
bubble_sort(a)
print(f"After: {a}")
