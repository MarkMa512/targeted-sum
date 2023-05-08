"""
Retired module for finding unique combinations of integers that sum to a target as it is a subset of duplicate_int.py
"""

from typing import List
import logging

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
    if target == 0: # if target is 0
        result.append(path) # add path to result
        return # return
    if target < 0: # if target is negative
        return # return
    for i in range(start, len(candidates)): # iterate over candidates
        if i > start and candidates[i] == candidates[i - 1]: # if current candidate is the same as the previous candidate
            continue # skip current candidate
        find_combinations(candidates, target - candidates[i], i + 1, path + [candidates[i]], result) # find combinations for current candidate

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

def filter_redundant_combinations(combinations: List[List[int]]) -> List[List[int]]:
    """
    filter out combinations that contain duplicate numbers which have already been used

    :param combinations: list of combinations
    :return: list of unique combinations
    """
    logger.info('---filtering out redundant combinations')
    
    used_numbers = set() # set of used numbers
    unique_combinations = [] # list of unique combinations

    for combination in combinations: # iterate over combinations
        if not any(num in used_numbers for num in combination): # if no number in combination has been used
            unique_combinations.append(combination) # add combination to unique combinations
            used_numbers.update(combination) # add combination to used numbers 
            # we can do this because we know that all the numbers in the input list are unique
    return unique_combinations
