# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        while n > 0:
            quotient = n // 3
            residual = n % 3

            if residual > 1:
                return False

            n = quotient

        return True
