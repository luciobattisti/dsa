def recurse(a: list, l: int, r: int, k: int) -> bool:

    length = r - l + 1

    # Base case
    if length <= 1:
        if a[l] == k:
            return True
        else:
            return False

    # Calculate m
    m = (l+r) // 2

    if a[m] == k:
        return True

    # Recurse
    if k < a[m]:
        return recurse(a, l, m-1, k)
    else:
        return recurse(a, m+1, r, k)


def binary_search(k: int, a: list) -> bool:

    # Edge case
    if len(a) == 1:
        if a[0] == k:
            return True
        else:
            return False

    # Standard case
    l = 0
    r = len(a) - 1

    return recurse(a, l, r, k)


if __name__ == "__main__":

    a = [1, 3, 5, 6, 8, 10, 12]

    print(binary_search(5, a))
    print(binary_search(10, a))
    print(binary_search(-1, a))

    a = [1, 3]
    print(binary_search(1, a))
    print(binary_search(0, a))