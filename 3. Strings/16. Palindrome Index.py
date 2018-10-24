#!/bin/python3

import os


# Complete the palindromeIndex function below.


def palindromeIndex(s):
    if is_palindrome(s):
        return -1

    for i in range(len(s) // 2):
        if s[i] != s[0 - i - 1]:
            if is_palindrome(s[:i] + s[i + 1:]):
                return i
            elif is_palindrome(s[:0 - i - 1] + s[0 - i:]):
                return len(s) - i - 1
    else:
        if is_palindrome(s[:-1]):
            return len(s) - 1

    return -1


def is_palindrome(s):
    return s == s[::-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
