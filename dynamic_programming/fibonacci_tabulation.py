def fibonacci(n: int):

    dp = [0, 1]

    for i in range(2, n):
        tmp = dp[0] + dp[1]
        dp[0] = dp[1]
        dp[1] = tmp

    return dp[0] + dp[1]


print(fibonacci(10))