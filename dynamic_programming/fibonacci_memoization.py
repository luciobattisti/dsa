def fibonacci(n: int, memo: dict={}) -> int:

    # Base case
    if n <= 1:
        return n

    # General case
    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)

    return memo[n]


print(fibonacci(10))
