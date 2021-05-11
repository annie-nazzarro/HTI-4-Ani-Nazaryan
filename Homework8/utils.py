#!/usr/bin/env python3
from sys import argv


def odd_digit_range(start, stop):
    for n in range(start, stop):
        for d in str(n):
            if int(d) % 2 == 0:
                break
            else:
                yield n


if __name__ == '__main__':
    if len(argv) != 3:
        raise ValueError("You should provide start and stop")

    start_arg = int(argv[1])
    stop_arg = int(argv[2])

    for i in odd_digit_range(start_arg, stop_arg):
        print(i, end=" ")

    print()
        