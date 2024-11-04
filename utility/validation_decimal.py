from typing import List, Dict
from collections import Counter
from decimal import Decimal
import logging

logger = logging.getLogger(__name__)

def validate_result(result: List[List[Decimal]], input_list: List[Decimal], output_list: List[Decimal], tolerance: Decimal = Decimal("0")) -> bool:
    """
    Validate result by checking if it: 

    :param result: list of combinations of x that sum to y
    :param input_list: original input list of candidates
    :param output_list: list of target values
    :param tolerance: Decimal tolerance level for approximation (default is 0 for exact match)
    
    :return: True if result is valid by ensuring that: 
        1) The length of result is equal to the length of target
        2) The count of each element in result is equal to the count of the same element in input_list
        3) There is no empty combination in result
        4) Each combination’s sum approximates the target within a tolerance level
    False otherwise
    """
    logger.info('---validating result---')
    
    if len(result) == 0:
        logger.error('+++result is empty, no valid combination found!+++')
        return False
    if len(result) != len(output_list):
        logger.error('+++length of result does not equal to length of target!+++')
        return False
    logger.info(f"===length of result is equal to length of target!===")
    
    # Count occurrences of elements in input_list and result
    x_element_count: Dict[Decimal, int] = Counter(input_list)
    result_element_count: Dict[Decimal, int] = Counter()
    
    # Check each combination
    for i, combination in enumerate(result):
        combination_sum = sum(combination)
        target = output_list[i]
        
        # Check if the combination sum is within the tolerance range of the target
        if abs(combination_sum - target) > tolerance:
            logger.error(f"+++sum of combination {i} ({combination_sum}) is not within tolerance of target {target}+++")
            return False
        
        combination_count: Dict[Decimal, int] = Counter(combination)
        
        # Check for empty combinations
        if len(combination) == 0:
            logger.error('+++result contains empty combination!+++')
            return False
        
        # Ensure each element count in combination does not exceed its count in input_list
        for key in combination_count:
            if combination_count[key] > x_element_count[key]:
                logger.error('+++result is invalid, count of %s in result is greater than count of %s in input in a combination+++', key, key)
                return False
            result_element_count[key] += combination_count[key]
    
    # Final check to ensure overall counts match input_list counts
    for key in x_element_count:
        if result_element_count[key] != x_element_count[key]:
            logger.error('+++result is invalid, count of %s in result is not equal to count of %s in input+++', key, key)
            return False

    logger.info('===result is valid===')
    return True