from itertools import combinations
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

# if 0 is provided in the target list, it has to be dealt with separately
def find_zero_sum_combination(candidates: List[int]) -> List[int]:
    """
    from the given candidate list, found out the elements that sums up to 0

    :param candidate: list of candidates, which may contain duplicates, zero, or negative numbers
    
    :return: list of elements that sums up to 0
    """
    logger.info('---finding combinations that sum up to 0---')
    for i in range(1, len(candidates) + 1):
        for combination in combinations(candidates, i):
            if sum(combination) == 0:
                zero_sum_result: List[int] = list(combination)
                logger.info(f'---found {len(zero_sum_result)} combinations that sum up to 0---')
                logger.info(f'---combinations that sum up to 0: {zero_sum_result}---')
                return zero_sum_result
    return []
    

def sum_combinations(input_list: List[int], target_list: List[int]) -> List[List[int]]:
    """
    find all combinations of input_list that sum to target_list

    :param input_list: list of candidates, which may contain duplicates
    :param target_list: list of targets

    :return: list of combinations
    """
    logger.info('---finding combinations---')

    # create a copy of input_list and target_list so that the original list is not modified
    input_list_copy = input_list.copy()
    target_list_copy = target_list.copy()

    input_list_copy.sort()
    result: List[List[int]] = []

    # check if 0 is present in target_list
    zero_count = target_list.count(0)
    # while there is >0 zero in target_list, find combinations that sum up to 0
    while zero_count > 0: 
        # find the combination that sums up to 0
        zero_sum_combination: List[int] = find_zero_sum_combination(input_list)
        # if there is a combination that sums up to 0, 
        if zero_sum_combination:
            # append to result and 
            result.append(zero_sum_combination)
            # remove the elements in the combination from input_list_copy. This is because the original list is not modified
            # so that it can be used later to valid combinations
            input_list_copy = [elem for elem in input_list_copy if elem not in zero_sum_combination] 
            zero_count -= 1 # reduce zero_count by 1
        else: # if there is no combination that sums up to 0, break
            break
    
    # Update the target_list to remove the 0s
    target_list_copy = [elem for elem in target_list_copy if elem != 0]

    for target in target_list_copy:
        res: List[List[int]] = []
        find_combinations(input_list_copy, target, 0, [], res)
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

    # # Check for a 0-sum combination while constructing the combinations
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
