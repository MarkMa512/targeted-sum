import logging
from typing import List
from combination.duplicate_int import sum_combinations, filter_redundant_combinations_set
from utility.validation import validate_input_target, validate_result

logging.basicConfig(format="%(asctime)s %(levelname)s %(filename)s:%(funcName)s():%(lineno)i: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S", level=logging.DEBUG)

logger = logging.getLogger(__name__)

def test(input_list: List[int], target_list: List[int])->None:
    """
    Given input and target, validate input and target, find all combinations, filter out redundant combinations, validate result, and print out the result.
    
    :param input_list: input list of integers
    :param target_list: target list of integers

    :returns:None
    """
    logger.info("---validating input and target---")
    if not validate_input_target(input_list, target_list):
        return
    
    logger.info("---finding combinations---")
    all_combinations: List[List[int]] = sum_combinations(input_list, target_list)
    logger.info("---filtering out redundant combinations---")
    viable_results: List[List[List[int]]] = filter_redundant_combinations_set(input_list, target_list, all_combinations)
    logger.info("---validating result---")
    counter: int = 0
    for result in viable_results:
        if validate_result(result=result, input_list=input_list, output_list=target_list):
            logger.info(f"---result {counter} is valid---")
            print(result)
            counter += 1
    logger.info("---done---")


if __name__ == "__main__":
    test()