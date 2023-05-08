from typing import List
import logging
from utility.validation import validate_input, validate_unique, validate_result
from utility.csv import read_csv, export_to_csv

logger = logging.getLogger(__name__)


def find_combinations(candidates:List[int], target: int, start: int, path: List[int], result: List[List[int]]) -> None:
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

def sum_combinations(x: List[int], y: List[int]) -> List[List[int]]:
    """
    find all combinations of x that sum to y

    :param x: list of candidates
    :param y: list of targets

    :return: list of combinations
    """
    logger.info('---finding combinations---')
    x.sort() # sort x
    results = [] # result list
    for target in y: # iterate over targets
        res = [] # result list for current target
        find_combinations(x, target, 0, [], res) # find combinations for current target
        results.extend(res) # add combinations to result
    return results # return result

def unique_combinations(combinations: List[List[int]]) -> List[List[int]]:
    """
    filter out combinations that contain duplicate numbers

    :param combinations: list of combinations
    :return: list of unique combinations
    """
    logger.info('---filtering out duplicate numbers---')

    used_numbers = set()
    unique_combinations = []

    for combination in combinations:
        if not any(num in used_numbers for num in combination):
            unique_combinations.append(combination)
            used_numbers.update(combination)

    return unique_combinations

if __name__ == "__main__":
    x = read_csv('input.csv')
    y = read_csv('target.csv')
    if validate_input(x, y) and validate_unique(x):
        results = sum_combinations(x, y)
        results = unique_combinations(results)
        if validate_result(results, x, y):
            export_to_csv(results, 'results.csv')
            print(f"The result is: \n {results}")
        else:
            logger.error('No valid result found')