Dynamic Programming (DP) is a technique used in computer science and mathematics to solve problems that can be broken down into overlapping subproblems. It's particularly useful for optimization problems where you need to find the best solution among many possible solutions.

### Core Concepts of Dynamic Programming

1. **Optimal Substructure**:
   - A problem has an optimal substructure if its solution can be constructed efficiently from solutions of its subproblems.
   - Example: The shortest path problem in a graph.

2. **Overlapping Subproblems**:
   - The problem can be divided into smaller subproblems that are solved multiple times.
   - Example: Fibonacci sequence.

3. **Memoization (Top-Down)**:
   - Store the results of expensive function calls and reuse them when the same inputs occur again.
   - Example: Recursive implementation with a cache.

4. **Tabulation (Bottom-Up)**:
   - Solve the problem iteratively and store results in a table. This avoids recursion overhead.
   - Example: Iterative implementation with arrays.

---

### Steps to Solve a Problem Using DP

1. **Define the State**:
   - Decide what each subproblem represents. Define a state variable to represent the solution for the subproblem.
   - Example: *dp[i]* could represent the minimum cost to reach the \( i^{th} \) step in a staircase problem.

2. **State Transition Relation**:
   - Determine how to compute the solution for the current state using previous states.
   - Example: *dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])*  in a staircase problem.

3. **Base Case**:
   - Define the simplest subproblem(s) with known solutions.
   - Example: *dp[0] = 0* for the staircase problem if no steps are required.

4. **Compute the Final Solution**:
   - Use the state transition relation iteratively or recursively to compute the solution for the original problem.

---

### Examples

#### 1. Fibonacci Sequence

Compute the *n^th* Fibonacci number.

##### Recursive with Memoization:
```python
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

print(fibonacci(10))  # Output: 55
```

##### Iterative with Tabulation:
```python
def fibonacci(n):
    if n <= 1:
        return n
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n]

print(fibonacci(10))  # Output: 55
```

---

#### 2. 0/1 Knapsack Problem

Given weights and values of \( n \) items, determine the maximum value you can obtain with a weight capacity \( W \).

##### Tabulation Approach:
```python
def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

weights = [1, 2, 3]
values = [60, 100, 120]
capacity = 5
print(knapsack(weights, values, capacity))  # Output: 220
```

---

#### 3. Longest Common Subsequence (LCS)

Find the longest subsequence present in both strings.

##### Tabulation Approach:
```python
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

print(lcs("abcde", "ace"))  # Output: 3
```

---

#### 4. Minimum Path Sum (Grid Problem)

Find the minimum path sum from the top-left to the bottom-right corner of a grid.

##### Tabulation Approach:
```python
def min_path_sum(grid):
    rows, cols = len(grid), len(grid[0])
    dp = [[0] * cols for _ in range(rows)]

    dp[0][0] = grid[0][0]
    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    for j in range(1, cols):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

    return dp[rows - 1][cols - 1]

grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print(min_path_sum(grid))  # Output: 7
```

---

### Key Points to Remember
- DP is powerful for problems involving combinations, sequences, or optimization.
- Identify overlapping subproblems and optimal substructure.
- Choose memoization (recursive) or tabulation (iterative) based on the problem.
- Analyze time and space complexity to optimize the solution further.