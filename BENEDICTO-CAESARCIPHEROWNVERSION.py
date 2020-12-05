# @Author: Jory
# IAS
# MY Own Version

import string
import collections


def jory(rotate_string, number_to_rotate_by):
    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_uppercase)

    upper.rotate(number_to_rotate_by)
    lower.rotate(number_to_rotate_by)

    upper = ''.join(list(upper))
    lower = ''.join(list(upper))

    # print(upper, lower)
    # jory('', 0)
    return rotate_string.translate(str.maketrans(string.ascii_uppercase, upper)) \
        .translate(str.maketrans(string.ascii_lowercase, lower))


# print(jory("JORY CAESAR CIPHER VERSION", 0)
our_string = "JORY'S CAESAR CIPHER OWN VERSION"
for i in range(len(string.ascii_uppercase)):
    print(i, "|", jory(our_string, i))
