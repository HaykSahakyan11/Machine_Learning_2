# 1160. Find Words That Can Be Formed by Characters

from collections import Counter


def countCharacters(words, chars):
    len_good_str = 0
    chars_counter = Counter(chars)
    for word in words:
        good_str = True
        word_counter = Counter(list(word))
        for key in word_counter.keys():
            if key not in chars_counter:
                good_str = False
                break
            else:
                if chars_counter[key] < word_counter[key]:
                    good_str = False
                    break
        if good_str:
            len_good_str += len(word)

    return len_good_str


words = ["hello", "world", "leetcode"]  # ["cat", "bt", "hat", "tree"]
chars = "welldonehoneyr"  # "atach"
print(countCharacters(words=words, chars=chars))
