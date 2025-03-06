# https://coderbyte.com/editor/Min%20Window%20Substring:Python3

"""
"aaabaaddae", "aad"
p1 = 0
p2 = 0

Simple Explanation:
1. Move p1 to the left until we find a match (a string containing all charachters)
2. Then try to move p2 towards p1 until the match still holds
3. Memorize the string and then move p1 to the right
4. Repeat the process until p1 reaches the end of the string
"""

from collections import Counter


def MinWindowSubstring(strArr):
    # Code goes here
    strn = strArr[0]
    strk = strArr[1]

    required_chars = Counter(strk)
    required_matches = sum([required_chars[k] for k in required_chars.keys()])

    p1 = 0
    p2 = 0
    matched_count = 0
    matched_chars = {}

    # Find largest substr
    min_window = ""
    while p1 < len(strn):
        c = strn[p1]
        if c in required_chars:
            if c not in matched_chars:
                matched_chars[c] = 1
                matched_count += 1
            else:
                if matched_chars[c] < required_chars[c]:
                    matched_count += 1
                matched_chars[c] += 1

        if matched_count == required_matches:
            if not min_window:
                min_window = strn[p2:p1 + 1]
            while p2 < p1:
                c = strn[p2]
                if c not in required_chars:
                    p2 += 1
                elif matched_chars[c] > required_chars[c]:
                    matched_chars[c] -= 1
                    p2 += 1
                else:
                    break

            if len(min_window) > len(strn[p2:p1 + 1]):
                min_window = strn[p2:p1 + 1]

        p1 += 1

    return min_window


# keep this function call here
print(MinWindowSubstring(input()))