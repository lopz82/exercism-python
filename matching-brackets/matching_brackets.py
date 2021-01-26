from itertools import zip_longest

BRACKETS = {"}": "{", "]": "[", ")": "("}


def is_paired(input_string):
    stack = []
    for char in input_string:
        if char in BRACKETS.values():
            stack.append(char)
        elif char in BRACKETS.keys():
            if not stack or BRACKETS[char] != stack.pop():
                return False
    else:
        return not stack
