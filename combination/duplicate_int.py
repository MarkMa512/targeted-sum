from typing import List, Dict, Tuple, Iterator
import logging
from collections import Counter
from itertools import chain, combinations

logger = logging.getLogger(__name__)

def find_combinations(candidates: List[int], target: int, start: int, path: List[int], result: List[List[int]]) -> None:
    """
    find all combinations of candidates that sum to target

    :param candidates: list of candidates
    :param target: target sum
    :param start: start index
    :param path: current path
    :param res: result list

    :return: None
    """
    if target == 0:
        result.append(path)
        return
    if target < 0:
        return
    for i in range(start, len(candidates)):
        if i > start and candidates[i] == candidates[i - 1]:
            continue
        find_combinations(candidates, target - candidates[i], i + 1, path + [candidates[i]], result)


def sum_combinations(input_list: List[int], target_list: List[int]) -> List[List[int]]:
    """
    find all combinations of input_list that sum to target_list

    :param input_list: list of candidates, which may contain duplicates
    :param target_list: list of targets

    :return: list of combinations
    """
    logger.info('---finding combinations---')
    input_list.sort()
    result: List[List[int]] = []
    for target in target_list:
        res: List[List[int]] = []
        find_combinations(input_list, target, 0, [], res)
        result.extend(res)
    return result


def count_occurrences(int_list: List[int]) -> Dict[int, int]:
    """
    count the occurrences of each element in a list

    :param int_list: list of integers

    :return: dictionary of occurrences, key is the integer, value is the number of occurrences
    """
    return Counter(int_list)


def backtrack(
    x_counts: Dict[int, int],
    y_counts: Dict[int, int],
    combinations: List[List[int]],
    current: List[List[int]],
    index: int,
    x_remaining: Dict[int, int],
    y_remaining: Dict[int, int],
) -> List[List[List[int]]]:
    if index == len(combinations):
        if all(x_remaining[k] == 0 for k in x_remaining) and all(y_remaining[k] == 0 for k in y_remaining):
            return [current.copy()]
        return []

    results = []


    # Try adding the current combination to the solution
    comb_sum = sum(combinations[index])
    if y_remaining[comb_sum] > 0 and all(x_remaining[k] >= 0 for k in x_remaining):
        for elem in combinations[index]:
            x_remaining[elem] -= 1
        y_remaining[comb_sum] -= 1

        current.append(combinations[index])
        results.extend(backtrack(x_counts, y_counts, combinations, current, index + 1, x_remaining, y_remaining))
        current.pop()

        for elem in combinations[index]:
            x_remaining[elem] += 1
        y_remaining[comb_sum] += 1

    # Try skipping the current combination
    results.extend(backtrack(x_counts, y_counts, combinations, current, index + 1, x_remaining, y_remaining))

    return results


def filter_redundant_combinations_set(x: List[int], y: List[int], combinations: List[List[int]]) -> List[List[List[int]]]:
    x_counts = count_occurrences(x)
    y_counts = count_occurrences(y)

    x_remaining = x_counts.copy()
    y_remaining = y_counts.copy()

    results = backtrack(x_counts, y_counts, combinations, [], 0, x_remaining, y_remaining)

    return results
