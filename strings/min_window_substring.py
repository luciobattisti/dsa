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
    min_window = ""

    for i in range(len(strn)):
        for j in range(i, len(strn)):
            curr_str = strn[i:j + 1]
            curr_chars = Counter(strn[i:j + 1])
            if is_substr(required_chars, curr_chars):
                if not min_window:
                    min_window = curr_str
                elif len(min_window) > len(curr_str):
                    min_window = curr_str

    return min_window


# keep this function call here
print(MinWindowSubstring(input()))




