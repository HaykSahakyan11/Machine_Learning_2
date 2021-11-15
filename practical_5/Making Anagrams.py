# Making Anagrams

from collections import Counter


def makeAnagram(a, b):
    a_dict = Counter(a)
    b_dict = Counter(b)

    intersection = set(a_dict).intersection(set(b_dict))
    output = 0
    for key in intersection:
        output += min(a_dict[key], b_dict[key])
    return len(a) + len(b) - 2 * output


if __name__ == '__main__':
    # a = 'cde'
    # b = 'abc'
    a = input()
    b = input()
    print(makeAnagram(a, b))
