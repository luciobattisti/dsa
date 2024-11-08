# Implementation of quick sort algorithm

def swap(a: list, p: int, l: int, r: int) -> int:

    while l != r:
        if a[l] > a[p] and  a[r] < a[p]:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1
        elif a[l] > a[p] and a[r] >= a[p]:
            r -= 1
        elif a[l] <= a[p] and a[r] < a[p]:
            l += 1
        else:
            l += 1
            r -= 1

    a[p], a[l] = a[l], a[p]

    return l


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
