import logging
from typing import List
from combination.duplicate_int import sum_combinations, filter_redundant_combinations_set
from utility.csv import read_csv, export_to_csv
from utility.validation import validate_input_target, validate_result, validate_viable_result_sets

logging.basicConfig(format="%(asctime)s %(levelname)s %(filename)s:%(funcName)s():%(lineno)i: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S", level=logging.DEBUG)

logger = logging.getLogger(__name__)

def main()->None:
    """
    Read input and target from csv files, validate input and target, find all combinations, filter out redundant combinations, validate result, and export to csv.

    Returns:None
    """
    logger.info("---reading input file---")
    try: 
        input_list: List[int] = read_csv('input.csv')
    except FileNotFoundError: 
        logger.error("+++input file not found+++")
        return
    
    logger.info("---reading target file---")
    try: 
        target_list: List [int] = read_csv('target.csv')
    except FileNotFoundError:
        logger.error("+++target file not found+++")
        return

    logger.info("---validating input and target---")
    if not validate_input_target(input_list, target_list):
        return
    
    logger.info("---finding combinations---")
    all_combinations: List[List[int]] = sum_combinations(input_list, target_list)
    logger.info("---filtering out redundant combinations---")
    viable_results: List[List[List[int]]] = filter_redundant_combinations_set(input_list, target_list, all_combinations)
    if not validate_viable_result_sets(viable_results):
        return
    logger.info("---validating result---")
    counter: int = 0
    for result in viable_results:
        if validate_result(result=result, input_list=input_list, output_list=target_list):
            logger.info(f"---result {counter} is valid---")
            print(f"combination {counter} for {target_list}: {result}")
            export_to_csv(result, f"result_{counter}.csv")
            counter += 1
    logger.info("---done---")


if __name__ == "__main__":
    main()