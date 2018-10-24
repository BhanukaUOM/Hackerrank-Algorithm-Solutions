#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    min_length = 6
    requirements = {
        "numbers": "0123456789",
        "lower_case": "abcdefghijklmnopqrstuvwxyz",
        "upper_case": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "special_characters": "!@#$%^&*()-+"
    }

    add_diff_char_count = 0

    for i, k in requirements.items():
        if not has_char(password, k):
            add_diff_char_count += 1

    return max(min_length - n, add_diff_char_count)


def has_char(string, chars_str):
    return any(c in chars_str for c in string)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
