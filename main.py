import logging
from typing import List
from combination.duplicate_int import sum_combinations, filter_redundant_combinations
from utility.csv import read_csv, export_to_csv
from utility.validation import validate_input_target, validate_result

logging.basicConfig(format="%(asctime)s %(levelname)s %(filename)s:%(funcName)s():%(lineno)i: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S", level=logging.DEBUG)

logger = logging.getLogger(__name__)

def main()->None:
    logger.info("---reading input file---")
    input_list = read_csv('input.csv')
    target_list = read_csv('target.csv')

    logger.info("---validating input and target---")
    if not validate_input_target(input_list, target_list):
        return
    
    logger.info("---all elements in input are unique---")
    logger.info("---finding combinations---")
    result: List[List[int]] = sum_combinations(input_list, target_list)
    viable_results: List[List[List[int]]] = filter_redundant_combinations(input_list, target_list, result)
    logger.info("---validating result---")
    counter: int = 0
    for result in viable_results:
        if validate_result(input_list, target_list, result):
            logger.info(f"---result {counter} is valid---")
            export_to_csv(result, f"result_{counter}.csv")
            counter += 1
    logger.info("---done---")


if __name__ == "__main__":
    main()