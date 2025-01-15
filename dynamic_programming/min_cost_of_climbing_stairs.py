# https://leetcode.com/problems/min-cost-climbing-stairs/

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # Base case
        if len(cost) == 2:
            return min(cost[0], cost[1])

        # General case
        n = len(cost)

        # Calculate costs
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        return min(dp[n-1], dp[n-2])


def calculate_min(i: int, cost: List[int], dp: List[int]) -> int:
    if i == 0:
        dp[0] = cost[0]
        calculate_min(i + 1, cost, dp)
    elif i == 1:
        dp[1] = cost[1]
        calculate_min(i + 1, cost, dp)
    elif i < len(cost):
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        calculate_min(i + 1, cost, dp)
    else:
        return


class SolutionRecursive:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Edge case
        if len(cost) == 2:
            return min(cost[0], cost[1])

        # General case
        n = len(cost)

        dp = [0] * n
        calculate_min(0, cost, dp)

        return min(dp[n - 1], dp[n - 2])


