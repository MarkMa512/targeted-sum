import logging
from typing import List, Dict
from collections import Counter

logger = logging.getLogger(__name__)

def validate_input_target(input:list, target:list)-> bool:
    """
    validate input and target

    :param input: list of integers
    :param target: list of targets
    :return: True if input and target are valid, False otherwise
    """
    logging.info('---validating input and target---')
    if len(input) == 0: # if input is empty, return False
        logger.error('---input is empty!---')
        return False
    if len(target) == 0: # if target is empty, return False
        logger.error('---target is empty!---')
        return False
    sum_of_input = sum(input) # sum of input
    sum_of_target = sum(target) # sum of target
    if sum_of_input != sum_of_target:
        logger.error('---sum of input and target are not equal!---')
        logger.error('---sum of input: %s, sum of target: %s---', sum_of_input, sum_of_target)
        return False
    logger.info('---input and target are valid---')
    return True # return True

def validate_unique_input(input:list)-> bool:
    """
    validate input by checking if it contains duplicates

    :param input: list of integers
    :return: True if input is valid with no duplicates, False otherwise
    """
    logger.info('---checking if input contains duplicates---')
    # convert input to tuple to address unhashable type error
    input_tuple = tuple(input)
    if len(input) != len(set(input_tuple)):
        logger.info('---input contains duplicates! use module for duplicates---')
        return False

    logger.info('---all elements in input are unique---')
    return True # return True

def validate_result(result: List[List[int]], x: List[int],y:List[int] )-> bool:
    """
    validate result by checking if it: 

    :param result: list of combinations
    :return: True if result is valid with no duplicates, False otherwise
    """
    logger.info('---checking the length of result---')
    logger.info(f"---length of result: {len(result)}, length of target: {len(y)}---")
    if len(result) != len(y):
        logger.error('+++length of result is not equal to length of target!+++')
        return False
    logger.info(f"===length of result is equal to length of target!===")
    
    logger.info('---checking if the result has the same count of numbers as per x---')
    x_element_count: Dict[int, int] = Counter(x)
    result_element_count: Dict[int, int] = Counter()

    for combination in result:
        combination_count: Dict[int, int] = Counter(combination)
        logger.info('---checking if combination has counts of elements less than or equal to the counts of the same elements in x---')
        for key in combination_count:
            # check for individual combination, if the count of an element in a combination is greater than the count of the same element in x, return False
            logger.info(f'---count of {key} in combination: {combination_count[key]}, count of {key} in x: {x_element_count[key]}---')
            if combination_count[key] > x_element_count[key]:
                logger.error('+++result is invalid, count of %s in result is greater than count of %s in input in a combination+++', key, key)
                return False
            result_element_count[key] += combination_count[key]
    
    # check for the whole result, if the count of an element in result is not equal to the count of the same element in x, return False
    for key in x_element_count:
        logger.info(f'---count of {key} in x: {x_element_count[key]}, count of {key} in result: {result_element_count[key]}---')
        if result_element_count[key] != x_element_count[key]:
            logger.error('+++result is invalid, count of %s in result is not equal to count of %s in input+++', key, key)
            return False

    logger.info('===result is valid===')
    return True