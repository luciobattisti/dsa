# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/description

class BruteForceSolution:
    def numOfSubarrays(self, arr: List[int]) -> int:

        """
        [1,3,5]

        1, 4, 9, (4-1), (9-1),
        """

        # General case

        odd_sums = 0
        # for i in range(0, len(arr)):
        #    for j in range(i, len(arr)):
        #        res = sum(arr[i:j+1])
        #        if res % 2 != 0:
        #            odd_sums += 1

        # return odd_sums % (10**9 + 7)

        # Calculate all sums starting from 0
        odd_sums = 0
        sums = []
        for i in range(0, len(arr)):
            res = sum(arr[0:i + 1])
            sums.append(res)
            if res % 2 != 0:
                odd_sums += 1

        # print(sums)

        for j in range(1, len(arr)):
            for k in range(j, len(arr)):
                sums[k] = sums[k] - arr[j - 1]
                if sums[k] % 2 != 0:
                    odd_sums += 1

            # print(sums[j:])

        return odd_sums % (10 ** 9 + 7)


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:

        prefix = 0
        odd = 0
        even = 1
        res = 0
        mod = (10 ** 9 + 7)

        for num in arr:
            prefix = (prefix + num) % 2

            if prefix == 0:
                res = (res + odd) % mod
                even += 1
            else:
                res = (res + even) % mod
                odd += 1

        return res




