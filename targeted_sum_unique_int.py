from typing import List
import csv
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_csv(csv_name: str) -> List[int]:
    """
    read a csv and return list of integers

    :param csv_name: name of file
    :return: list of integers
    """
    logging.info(f'---reading {csv_name}---')
    with open(csv_name, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        return [int(row[0]) for row in csv_reader] # each row is a list of one element, so we return the first element
    
def validate(input:list, target:list)-> bool:
    """
    validate input and target

    :param input: list of integers
    :param target: list of targets
    :return: True if input and target are valid, False otherwise
    """
    if len(input) == 0: # if input is empty, return False
        logging.error('---input is empty!---')
        return False
    if len(target) == 0: # if target is empty, return False
        logging.error('---target is empty!---')
        return False
    sum_of_input = sum(input) # sum of input
    sum_of_target = sum(target) # sum of target
    if sum_of_input != sum_of_target:
        logging.error('---sum of input and target are not equal!---')
        return False
    return True # return True

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
    logging.info('---finding combinations---')
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
    logging.info('---filtering out duplicate numbers---')

    used_numbers = set()
    unique_combinations = []

    for combination in combinations:
        if not any(num in used_numbers for num in combination):
            unique_combinations.append(combination)
            used_numbers.update(combination)

    return unique_combinations

def export_to_csv(combinations:List[List[int]], file_name:str)-> None:
    """
    export combinations to csv file

    @param combinations: list of combinations
    @param file_name: name of file
    """
    logging.info(f'---exporting to {file_name}---')
    with open(file_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for combination in combinations:
            csv_writer.writerow(combination)

if __name__ == "__main__":
    x = read_csv('input.csv')
    y = read_csv('target.csv')
    if validate(x, y):
        results = sum_combinations(x, y)
        results = unique_combinations(results)
        export_to_csv(results, 'results.csv')
        print(f"The result is: \n {results}")