import logging
from typing import List
from decimal import Decimal
from combination.input_with_duplicate_decimal import sum_combinations, filter_redundant_combinations_set
from utility.csv import read_csv, export_to_csv
from utility.validation_decimal import validate_result

logging.basicConfig(format="%(asctime)s %(levelname)s %(filename)s:%(funcName)s():%(lineno)i: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S", level=logging.DEBUG)

logger = logging.getLogger(__name__)

def main() -> None:
    """
    Read input and target from CSV files, find all combinations that approximate the target values, 
    filter out redundant combinations, validate results, and export valid results to CSV files.

    Returns: None
    """

    # Read the input file
    logger.info("---reading input file---")
    try: 
        # Convert each item in input list to Decimal
        input_list: List[Decimal] = [Decimal(x) for x in read_csv('input.csv')]
    except FileNotFoundError: 
        logger.error("+++input file not found+++")
        return
    
    # Read the target file
    logger.info("---reading target file---")
    try: 
        # Convert each item in target list to Decimal
        target_list: List[Decimal] = [Decimal(x) for x in read_csv('target.csv')]
    except FileNotFoundError:
        logger.error("+++target file not found+++")
        return

    # Define tolerance
    tolerance = Decimal("0.01")

    # Find combinations with the specified tolerance
    logger.info("---finding combinations---")
    all_combinations: List[List[Decimal]] = sum_combinations(input_list, target_list, tolerance=tolerance)
    logger.info("---filtering out redundant combinations---")

    # Filter off the redundant combination sets with tolerance
    viable_results: List[List[List[Decimal]]] = filter_redundant_combinations_set(input_list, target_list, all_combinations, tolerance=tolerance)

    # Validate and export results
    logger.info("---validating result---")
    counter: int = 0
    for result in viable_results:
        if validate_result(result=result, input_list=input_list, output_list=target_list, tolerance=tolerance):
            logger.info(f"---result {counter} is valid---")
            print(f"combination {counter} for {target_list}: {result}")
            export_to_csv(result, f"result_{counter}.csv")
            counter += 1
    logger.info("---done---")


if __name__ == "__main__":
    main()