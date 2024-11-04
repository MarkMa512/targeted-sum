from decimal import Decimal
from itertools import combinations
from typing import List, Dict
import logging
from collections import Counter

logger = logging.getLogger(__name__)

def find_combinations(candidates: List[Decimal], target: Decimal, start: int, path: List[Decimal], result: List[List[Decimal]], tolerance: Decimal = Decimal("0.1")) -> None:
    """
    Find all combinations of candidates that approximate the target within a tolerance level.

    :param candidates: list of candidates
    :param target: target sum
    :param start: start index
    :param path: current path
    :param result: result list

    :return: None
    """
    if abs(target) <= tolerance:  # Allows combinations close to target
        result.append(path)
        return
    
    for i in range(start, len(candidates)):
        if i > start and candidates[i] == candidates[i - 1]:
            continue
        find_combinations(candidates, target - candidates[i], i + 1, path + [candidates[i]], result)

def find_zero_sum_combination(candidates: List[Decimal], tolerance: Decimal = Decimal("0.1")) -> List[Decimal]:
    """
    Find combinations that sum up approximately to zero within a tolerance level.

    :param candidates: list of candidates, which may contain duplicates, zero, or negative numbers
    
    :return: list of elements that sum up to approximately zero
    """
    logger.info('---finding combinations that sum up to 0---')
    for i in range(1, len(candidates) + 1):
        for combination in combinations(candidates, i):
            if abs(sum(combination)) <= tolerance:
                zero_sum_result: List[Decimal] = list(combination)
                logger.info(f'---found {len(zero_sum_result)} combinations that sum up to 0---')
                logger.info(f'---combinations that sum up to 0: {zero_sum_result}---')
                return zero_sum_result
    return []

def sum_combinations(input_list: List[Decimal], target_list: List[Decimal], tolerance: Decimal = Decimal("0.1")) -> List[List[Decimal]]:
    """
    Find all combinations of input_list that approximate the values in target_list within a tolerance.

    :param input_list: list of candidates, which may contain duplicates
    :param target_list: list of targets
    :param tolerance: tolerance level for comparing sums to target values

    :return: list of combinations
    """
    logger.info('---finding combinations---')

    input_list_copy = input_list.copy()
    target_list_copy = target_list.copy()
    input_list_copy.sort()
    result: List[List[Decimal]] = []

    zero_count = target_list.count(Decimal("0"))
    while zero_count > 0: 
        zero_sum_combination: List[Decimal] = find_zero_sum_combination(input_list,tolerance)
        if zero_sum_combination:
            result.append(zero_sum_combination)
            input_list_copy = [elem for elem in input_list_copy if elem not in zero_sum_combination] 
            zero_count -= 1
        else:
            break
    
    target_list_copy = [elem for elem in target_list_copy if elem != Decimal("0")]

    # Use tolerance when finding combinations
    for target in target_list_copy:
        res: List[List[Decimal]] = []
        find_combinations(input_list_copy, target, 0, [], res,tolerance)
        result.extend(res)
    return result

def count_occurrences(int_list: List[Decimal]) -> Dict[Decimal, int]:
    """
    Count the occurrences of each element in a list.

    :param int_list: list of numbers

    :return: dictionary of occurrences
    """
    return Counter(int_list)

def backtrack(
    input_count: Dict[Decimal, int],
    target_count: Dict[Decimal, int],
    combinations: List[List[Decimal]],
    current: List[List[Decimal]],
    index: int,
    input_remaining: Dict[Decimal, int],
    output_remaining: Dict[Decimal, int],
    tolerance: Decimal = Decimal("0.1")
) -> List[List[List[Decimal]]]:
    """
    Backtracking algorithm to find viable combinations that approximate target list values within a tolerance.

    :param input_count: dictionary of occurrences of each element in input_list
    :param target_count: dictionary of occurrences of each element in target_list
    :param combinations: list of combinations of elements in input_list that sum to elements in target_list
    :param current: current combination
    :param index: current index
    :param input_remaining: remaining occurrences of each element in input_list
    :param output_remaining: remaining occurrences of each element in target_list

    :return: list of viable combinations
    """
    if index == len(combinations):
        if all(input_remaining[k] == 0 for k in input_remaining) and all(output_remaining[k] == 0 for k in output_remaining):
            return [current.copy()]
        return []

    results = []
    comb_sum = sum(combinations[index])

    # Use tolerance when checking if comb_sum approximates a target
    for target in output_remaining:
        if abs(comb_sum - target) <= tolerance and output_remaining[target] > 0:
            # Temporarily update occurrences for backtracking
            for elem in combinations[index]:
                input_remaining[elem] -= 1
            output_remaining[target] -= 1
            
            current.append(combinations[index])
            results.extend(backtrack(input_count, target_count, combinations, current, index + 1, input_remaining, output_remaining))
            current.pop()

            # Revert occurrences after backtracking
            for elem in combinations[index]:
                input_remaining[elem] += 1
            output_remaining[target] += 1

    results.extend(backtrack(input_count, target_count, combinations, current, index + 1, input_remaining, output_remaining))

    return results

def filter_redundant_combinations_set(input_list: List[Decimal], target_list: List[Decimal], combinations: List[List[Decimal]],tolerance: Decimal = Decimal("0.1")) -> List[List[List[Decimal]]]:
    """
    Filter out redundant combinations to retain only viable ones.

    :param input_list: list of candidates, which may contain duplicates, zero, or negative numbers
    :param target_list: list of targets

    :return: list of viable combinations
    """
    x_counts: Dict[Decimal, int] = count_occurrences(input_list)
    y_counts: Dict[Decimal, int] = count_occurrences(target_list)

    x_remaining: Dict[Decimal, int] = x_counts.copy()
    y_remaining: Dict[Decimal, int] = y_counts.copy()

    results: List[List[List[Decimal]]] = backtrack(x_counts, y_counts, combinations, [], 0, x_remaining, y_remaining,tolerance)
    return results