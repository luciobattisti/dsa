# https://coderbyte.com/results/alusci:Questions%20Marks:Python3

def QuestionsMarks(strParam):
    # Find first number
    p = 0
    while p < len(strParam):
        if strParam[p].isdigit():
            break
        else:
            p += 1

    if p == len(strParam):
        return False

    left_num = int(strParam[p])

    qmarks = 0
    num_matches = 0
    first_num = True
    for c in strParam[p + 1:]:
        if c == "?":
            qmarks += 1

        if c.isdigit():
            right_num = int(c)
            if left_num + right_num == 10:
                if qmarks == 3:
                    num_matches += 1
                else:
                    return False

            left_num = right_num
            qmarks = 0

    return num_matches >= 1


# keep this function call here
print(QuestionsMarks(input()))