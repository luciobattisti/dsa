# https://coderbyte.com/editor/Min%20Window%20Substring:Python3

from collections import Counter


def is_substr(required: dict, curr: dict) -> bool:
    for k, v in required.items():
        if k not in curr:
            return False
        elif curr[k] < v:
            return False

    return True


def MinWindowSubstring(strArr):
    # Code goes here
    strn = strArr[0]
    strk = strArr[1]

    required_chars = Counter(strk)

    p1 = 0
    p2 = 0

    # Find largest substr
    min_window = ""
    while p1 < len(strn):
        curr_str = strn[p2:p1 + 1]
        curr_chars = Counter(curr_str)

        if is_substr(required_chars, curr_chars):
            curr_min_window = curr_str

            # Reduce substr length
            while p2 < len(strn):
                curr_str = strn[p2:p1 + 1]
                curr_chars = Counter(curr_str)

                if not is_substr(required_chars, curr_chars):
                    break
                else:
                    curr_min_window = curr_str
                    p2 += 1

            if not min_window:
                min_window = curr_min_window
            elif len(min_window) > len(curr_min_window):
                min_window = curr_min_window
        else:
            p1 += 1

    return min_window


# keep this function call here
print(MinWindowSubstring(input()))