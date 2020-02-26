#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "bcotton52"

import sys

opened = ['[', '(', '{', '<', '(*']
closed = [']', ')', '}', '>', '*)']

def is_nested(line):
    stack =  []
    unbalanced = False
    location = 0
    while line:
        item = line[0]
        if line[:2] == '(*' or line[:2] == '*)':
            item = line[:2]
        location += 1
        if item in closed:
           index = closed.index(item)
           match = opened[index]
           if stack.pop() != match:
               unbalanced = True
               break
        if item in opened:
            stack.append(item)

        line = line[len(item):]
    if stack or unbalanced:
        return 'NO, ' + str(location)
    return 'YES'


def main(args):
    """Open the input file and call `is_nested()` for each line"""
    with open('input.txt', 'r') as file:
        with open('output.txt', 'w') as new_file:
            for line in file:
                results = is_nested(line)
                print(results)
                new_file.write(results + '\n')


if __name__ == '__main__':
    main(sys.argv[1:])
