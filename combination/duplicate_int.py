from typing import List, Dict
import logging
from collections import Counter

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

    if target == 0: # if target is 0, append path to result
        result.append(path)
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
    input_count: Dict[int, int],
    target_count: Dict[int, int],
    combinations: List[List[int]],
    current: List[List[int]],
    index: int,
    input_remaining: Dict[int, int],
    output_remaining: Dict[int, int],
) -> List[List[List[int]]]:
    """
    backtracking algorithm to find all combinations of input_list and target_list that sum to target list

    :param input_count: dictionary of occurrences of each element in input_list
    :param target_count: dictionary of occurrences of each element in target_list
    :param combinations: list of combinations of elements in input_list that sum to elements in target_list
    :param current: current combination
    :param index: current index
    :param input_remaining: remaining occurrences of each element in input_list
    :param output_remaining: remaining occurrences of each element in target_list

    :return: list of combinations of viable combinations
    """
    if index == len(combinations):
        if all(input_remaining[k] == 0 for k in input_remaining) and all(output_remaining[k] == 0 for k in output_remaining):
            return [current.copy()]
        return []

    results = []

    # Try adding the current combination to the solution
    comb_sum = sum(combinations[index])
    if output_remaining[comb_sum] > 0 and all(input_remaining[k] >= 0 for k in input_remaining):
        for elem in combinations[index]:
            input_remaining[elem] -= 1
        output_remaining[comb_sum] -= 1

        current.append(combinations[index])
        results.extend(backtrack(input_count, target_count, combinations, current, index + 1, input_remaining, output_remaining))
        current.pop()

        for elem in combinations[index]:
            input_remaining[elem] += 1
        output_remaining[comb_sum] += 1

    # Try skipping the current combination
    results.extend(backtrack(input_count, target_count, combinations, current, index + 1, input_remaining, output_remaining))

    # Check for a 0-sum combination while constructing the combinations
    # if comb_sum == 0 and output_remaining[0] > 0:
    #     output_remaining[0] -= 1
    #     results.extend(backtrack(input_count, target_count, combinations, current, index + 1, input_remaining, output_remaining))
    #     output_remaining[0] += 1

    return results


def filter_redundant_combinations_set(input_list: List[int], target_list: List[int], combinations: List[List[int]]) -> List[List[List[int]]]:
    """
    filter out redundant combinations 

    :param input_list: list of candidates, which may contain duplicates, zero, or negative numbers
    :param target_list: list of targets which may contain duplicates, zero, or negative numbers and to be summed to

    :return: list of viable combinations
    """
    x_counts: Dict[int, int] = count_occurrences(input_list)
    y_counts: Dict[int, int] = count_occurrences(target_list)

    x_remaining: Dict[int, int] = x_counts.copy()
    y_remaining: Dict[int, int] = y_counts.copy()

    results: List[List[List[int]]]= backtrack(x_counts, y_counts, combinations, [], 0, x_remaining, y_remaining)

    return results
