from typing import List, Dict
from utility.csv import read_csv, export_to_csv
from utility.validation import validate_input, validate_result
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
    
    # if target == 0:
    #     result.append(path)
    #     return
    # if target < 0:
    #     return
    # for i in range(start, len(candidates)):
    #     find_combinations(candidates, target - candidates[i], i + 1, path + [candidates[i]], result)

    if target == 0:
        result.append(path)
        return
    if target < 0:
        return
    for i in range(start, len(candidates)):
        if i > start and candidates[i] == candidates[i - 1]:
            continue
        find_combinations(candidates, target - candidates[i], i + 1, path + [candidates[i]], result)

def sum_combinations(x: List[int], y: List[int]) -> List[List[int]]:
    """
    find all combinations of x that sum to y

    :param x: list of candidates, which may contain duplicates
    :param y: list of targets

    :return: list of combinations
    """
    logger.info('---finding combinations---')
    x.sort()
    results = []
    for target in y:
        res = []
        find_combinations(x, target, 0, [], res)
        results.extend(res)
    return results

def count_occurrences(int_list: List[int]) -> Dict[int, int]:
    """
    count the occurrences of each element in a list

    :param int_list: list of integers

    :return: dictionary of occurrences
    """
    return Counter(int_list)

def is_valid_combination(x_count: Dict[int, int], combination: List[int]) -> bool:
    """
    determine if a combination is valid by checking if the occurrences of each element in the combination is less than or equal to the occurrences of the same element in x

    :param x_count: dictionary of occurrences of each element in x
    :param combination: list of integers

    :return: boolean, True if the combination is valid, False otherwise
    """
    combination_count: Dict[int, int] = count_occurrences(combination) # count the occurrences of each element in the combination, key is the element, value is the occurrences
    for key in combination_count: # check if the occurrences of each element in the combination is less than or equal to the occurrences of the same element in x
        if combination_count[key] > x_count[key]: # if the occurrences of an element in the combination is greater than the occurrences of the same element in x, return False
            return False
    return True

def unique_combinations(x: List[int], combinations: List[List[int]]) -> List[List[int]]:
    """
    filter out duplicate combinations

    :param x: list of candidates, which may contain duplicates
    :param combinations: list of combinations

    :return: list of unique combinations
    """
    logger.info('---filtering out duplicate combinations---')
    x_count = count_occurrences(x)
    unique_combinations = []

    for combination in combinations:
        if is_valid_combination(x_count, combination):
            x_count_comb = count_occurrences(combination)
            x_count.subtract(x_count_comb)
            unique_combinations.append(combination)

    return unique_combinations

# Example usage
# x = [1, 2, 2, 3, 4, 5]
# y = [8, 9]
# combinations = sum_combinations(x, y)
# filtered_combinations = unique_combinations(x, combinations)
# print(filtered_combinations)

if __name__ == "__main__":
    x = read_csv('input_duplicate.csv')
    y = read_csv('target_duplicate.csv')
    if validate_input(x, y):
        results = sum_combinations(x, y)
        # results = unique_combinations(x, results)
        # if validate_result(results, x, y):
        #     export_to_csv(results, 'results_duplicate.csv')
        #     print(f"The result is: \n {results}")
        # else:
        #     print('No Valid Combination Found')

        print(f"The result is: \n {results}")