"""
A password string, pwd, consists of binary characters (0s and 1s).
A cyber security expert is trying to determine the minimum number of changes required to make the password secure.
To do so, it must be divided into substrings of non-overlapping, even-length substrings.
Each substring can only contain 1s or 0s, not a mix. This helps to ensure that the password is strong and
less vulnerable to hacking attacks.

Find the minimum number of characters that must be flipped in the password string,
i.e., changed from 0 to 1 or 1 to 0, to allow the string to be divided as described.

A substring is a contiguous sequence of characters in a string.
"""


def getMinFlips(pwd: str) -> int:

    flips = 0

    for i in range(0, len(pwd), 2):
        substr = pwd[i:i+2]

        count_0 = substr.count("0")
        count_1 = substr.count("1")

        flips += min(count_0, count_1)

    return flips


if __name__ == "__main__":
    input_str = "100110"
    print(input_str, getMinFlips(input_str), 3)

    input_str = "101011"
    print(input_str, getMinFlips(input_str), 2)