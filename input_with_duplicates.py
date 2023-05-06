from typing import List
from utility.csv import read_csv, export_to_csv
from utility.validation import validate
import logging

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
    # logging.debug(f"candidates: {candidates}, target: {target}, start: {start}, path: {path}, res: {result}")
    if target == 0:
        result.append(path)
        return
    if target < 0:
        return
    for i in range(start, len(candidates)):
        find_combinations(candidates, target - candidates[i], i + 1, path + [candidates[i]], result)

def sum_combinations(x: List[int], y: List[int]) -> List[List[int]]:
    """
    find all combinations of x that sum to y

    :param x: list of candidates, which may contain duplicates
    :param y: list of targets

    :return: list of combinations
    """
    logging.debug(f"x: {x}, y: {y}")
    x.sort()
    results = []
    for target in y:
        res = []
        find_combinations(x, target, 0, [], res)
        results.extend(res)
    return results

def unique_combinations(x: List[int], combinations: List[List[int]]) -> List[List[int]]:
    used_numbers = set()
    unique_combinations = []

    for combination in combinations:
        if not any(num in used_numbers for num in combination):
            unique_combinations.append(combination)
            used_numbers.update(combination)

    return unique_combinations

# Example usage
# x = [1, 2, 2, 3, 4, 5]
# y = [8, 9]
# combinations = sum_combinations(x, y)
# filtered_combinations = unique_combinations(x, combinations)
# print(filtered_combinations)

if __name__ == "__main__":
    x = read_csv('input.csv')
    y = read_csv('target.csv')
    if validate(x, y):
        results = sum_combinations(x, y)
        results = unique_combinations(results)
        export_to_csv(results, 'results.csv')
        print(f"The result is: \n {results}")