#!/usr/bin/env python3
import sys
from typing import List

DICE = [4, 6, 8, 10, 12, 20]


def knapsack(capacity: int, values: List[int]) -> List[List[int]]:
    if len(values) == 0:
        raise Exception('error')
    if len(values) == 1:
        if capacity % values[0] == 0:
            return [[capacity // values[0]]]
        else:
            return []

    solutions = []  # type: List[List[int]]
    value, rest = values[0], values[1:]
    for i in range(0, capacity // value + 1):
        for subsolution in knapsack(capacity - i * value, rest):
            solution = [i]
            solution.extend(subsolution)
            solutions.append(solution)

    return solutions


def print_solution(solution: List[int], dice: List[int], low: int) -> None:
    rolls = []
    for i, value in enumerate(solution):
        if value > 1:
            rolls.append('{}d{}'.format(value, dice[i]))
        elif value == 1:
            rolls.append('d{}'.format(dice[i]))

    joined_rolls = '+'.join(rolls)
    modifier = low - sum(solution)
    if modifier > 0:
        print(joined_rolls + '+{}'.format(modifier))
    elif modifier == 0:
        print(joined_rolls)
    else:
        print(joined_rolls + '-{}'.format(abs(modifier)))


def range_to_roll(low: int, high: int) -> None:
    dice = list(reversed(sorted(DICE)))
    values = [die - 1 for die in dice]
    solutions = knapsack(high - low, values)
    for solution in solutions:
        print_solution(solution, dice, low)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise Exception("USAGE: range_to_roll.py LOW HIGH")
    range_to_roll(int(sys.argv[1]), int(sys.argv[2]))
