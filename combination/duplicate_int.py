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
    find all combinations of x that sum to y

    :param x: list of candidates, which may contain duplicates
    :param y: list of targets

    :return: list of combinations
    """
    logger.info('---finding combinations---')
    input_list.sort()
    results = []
    for target in target_list:
        res = []
        find_combinations(input_list, target, 0, [], res)
        results.extend(res)
    return results

def count_occurrences(int_list: List[int]) -> Dict[int, int]:
    """
    count the occurrences of each element in a list

    :param int_list: list of integers

    :return: dictionary of occurrences, key is the integer, value is the number of occurrences
    """
    return Counter(int_list)

def all_subsets(result: List[List[int]]) -> Iterator[Tuple[List[int]]]:
    """
    find all subsets of a list

    :param s: list of list of integers

    :return: iterator of all subsets
    """
    logger.info('---finding all subsets---')
    iterator = chain.from_iterable(combinations(result, r) for r in range(len(result)+1))
    return iterator

def filter_redundant_combinations(input_list: List[int], target_list: List[int], result: List[List[int]]) -> List[List[int]]:
    """
    filter out redundant combinations

    :param input_list: list of input that is used to generate combinations, it may contain duplicates
    :param target_list: list of targets
    :param results: list of combinations generated from input_list

    :return: overall valid combinations that: 
        1) do not contain count of any number in the overall combination that is greater than count of that number in x, 
        2) while contains all numbers in x
    """
    logger.info('---filtering redundant combinations---')
    # count the occurrences of each element
    input_list_counts = count_occurrences(input_list) 
    # count the occurrences of each element in y
    target_list_counts = count_occurrences(target_list) 

     # iterate through all the subsets of combinations
    for subset in all_subsets(result):
        combined_subset = [item for sublist in subset for item in sublist] # flatten the subset
        subset_counts = count_occurrences(combined_subset) # count the occurrences of each element in the subset
        
        # Check if all the elements in x have appeared in the overall combinations for the same number of times they are present in x
        is_valid_x = all(subset_counts[element] == count for element, count in input_list_counts.items())

        # Check if all the elements in y as the target have been accounted for
        is_valid_y = all(sum([1 for c in subset if sum(c) == target]) >= count for target, count in target_list_counts.items())
        
        # If both conditions are met, return the subset
        if is_valid_x and is_valid_y:
            return list(subset)
    
    # If no valid subset is found, return an empty list
    return []