# https://leetcode.com/problems/word-subsets/description/

def get_letter_counts(word: str) -> dict:
    output = {}
    for c in word:
        if c in output:
            output[c] += 1
        else:
            output[c] = 1

    return output


def get_max_letter_counts(words: list) -> dict:
    output = {}
    for w in words:

        counts = get_letter_counts(w)

        for k in counts:
            if k not in output:
                output[k] = counts[k]
            else:
                output[k] = max(output[k], counts[k])

    return output


def check_match(substr: dict, word: dict) -> bool:
    for k in substr.keys():
        if k not in word or word[k] < substr[k]:
            return False

    return True


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        """
        For each word in words1
            create hashmap with letter counts
            for example
                "amazon"
                a: 2
                m: 1
                z: 1
                o: 1
                n: 1

            for each world in b
            create hashmap of concatendated strings
            for example
                ["c", "cc", "b"]
                c: 3
                b: 1

        Then compare each key in b with all words hashmaps in a
        For example
            c: 3
            b: 1

            with "cccbb"
                c: 3
                b: 2

            if b[k] <= wa[k] for all k, we have a match
            and we return the word
        """

        # Calculate hashmaps for each word in words1
        words1_letter_counts = []
        for w in words1:
            words1_letter_counts.append(
                get_letter_counts(w)
            )

        # Calculate hashmaps for all words in words2
        words2_letter_counts = get_max_letter_counts(words2)

        # Find matches in words1
        matches = []
        for i, w1 in enumerate(words1):

            if check_match(
                    words2_letter_counts,
                    words1_letter_counts[i]
            ):
                matches.append(w1)

        return matches
