import logging
from typing import List
from decimal import Decimal
from combination.input_with_duplicate_decimal import sum_combinations, filter_redundant_combinations_set
from utility.validation_decimal import validate_result

logging.basicConfig(format="%(asctime)s %(levelname)s %(filename)s:%(funcName)s():%(lineno)i: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S", level=logging.DEBUG)

logger = logging.getLogger(__name__)

def test(input_list: List[Decimal], target_list: List[Decimal], tolerance: Decimal) -> None:
    """
    Given input and target, find all combinations, filter out redundant combinations, 
    validate results, and print out the result.
    
    :param input_list: input list of Decimals
    :param target_list: target list of Decimals
    :param tolerance: Decimal tolerance level for approximate matches

    :returns: None
    """
    logger.info("=====finding combinations=====")
    all_combinations: List[List[Decimal]] = sum_combinations(input_list, target_list, tolerance=tolerance)
    print(all_combinations)

    logger.info("=====filtering out redundant combinations=====")
    viable_results: List[List[List[Decimal]]] = filter_redundant_combinations_set(input_list, target_list, all_combinations, tolerance=tolerance)

    logger.info("=====validating result=====")
    counter: int = 0
    for result in viable_results:
        if validate_result(result=result, input_list=input_list, output_list=target_list, tolerance=tolerance):
            logger.info(f"=====result {counter} is valid=====")
            print(result)
            counter += 1
    logger.info("=====done=====")


if __name__ == "__main__":
    # Define a tolerance level
    tolerance = Decimal("0.01")

    # Test cases with Decimal input and target values
    input_unique_positive = [Decimal(x) for x in [1, 2, 3, 4, 5]]
    target_unique_positive = [Decimal(x) for x in [7, 8]]
    logger.info("=====1. testing for unique positive input and unique positive target=====")
    test(input_unique_positive, target_unique_positive, tolerance)

    input_unique_negative = [Decimal(x) for x in [-1, -2, -3, -4, -5]]
    target_unique_negative = [Decimal(x) for x in [-7, -8]]
    logger.info("=====2. testing for unique negative input and unique negative target=====")
    test(input_unique_negative, target_unique_negative, tolerance)

    input_unique_mixed = [Decimal(x) for x in [-1, 2, -3, 4, -5]]
    target_unique_mixed = [Decimal(x) for x in [-7, 4]]
    logger.info("=====3. testing for unique mixed input and unique mixed target=====")
    test(input_unique_mixed, target_unique_mixed, tolerance)

    input_duplicate_positive = [Decimal(x) for x in [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 4]]
    target_duplicate_positive = [Decimal(x) for x in [7, 8, 9, 10]]
    logger.info("=====4. testing for duplicate positive input and duplicate positive target=====")
    test(input_duplicate_positive, target_duplicate_positive, tolerance)

    input_duplicate_negative = [Decimal(x) for x in [-1, -2, -3, -4, -5, -1, -2, -3, -4, -5, -4]]
    target_duplicate_negative = [Decimal(x) for x in [-7, -8, -9, -10]]
    logger.info("=====5. testing for duplicate negative input and duplicate negative target=====")
    test(input_duplicate_negative, target_duplicate_negative, tolerance)

    input_duplicate_mixed = [Decimal(x) for x in [-1, 2, -3, 4, -5, -1, 2, -3, 4, -5]]
    target_duplicate_mixed = [Decimal(x) for x in [-7, 4, -8, 5]]
    logger.info("=====6. testing for duplicate mixed input and duplicate mixed target=====")
    test(input_duplicate_mixed, target_duplicate_mixed, tolerance)

    input_duplicate_mixed_for_zero = [Decimal(x) for x in [-1, 2, -3, 4, -5, -1, 2, -3, 4, -5]]
    target_duplicate_mixed_for_zero = [Decimal(x) for x in [-7, 4, -8, 1, 0, 4]]
    logger.info("=====7. testing for duplicate mixed input and duplicate mixed target with zero=====")
    test(input_duplicate_mixed_for_zero, target_duplicate_mixed_for_zero, tolerance)

    input_duplicate_mixed_for_zero_2 = [Decimal(x) for x in [-1, 2, -3, 4, -5, -1, 2, -3, 4, -5]]
    target_duplicate_mixed_for_zero_2 = [Decimal(x) for x in [0, -1, 3, -8]]
    logger.info("=====8. testing for duplicate mixed input and duplicate mixed target with zero=====")
    test(input_duplicate_mixed_for_zero_2, target_duplicate_mixed_for_zero_2, tolerance)

    input_duplicate_mixed_for_zero_3 = [Decimal(x) for x in [1, 2, 2, 3, 4, 5, 2, 2, 7, 8, -8, 8]]
    target_duplicate_mixed_for_zero_3 = [Decimal(x) for x in [8, 9, 4, 15, 0]]
    logger.info("=====9. testing for duplicate mixed input and duplicate mixed target with zero=====")
    test(input_duplicate_mixed_for_zero_3, target_duplicate_mixed_for_zero_3, tolerance)

    # Define a tolerance level for approximate matches
    tolerance = Decimal("0.01")

    # Original test cases with integer inputs converted to Decimal, as provided before
    input_unique_positive = [Decimal(x) for x in [1, 2, 3, 4, 5]]
    target_unique_positive = [Decimal(x) for x in [7, 8]]
    logger.info("=====1. testing for unique positive input and unique positive target=====")
    test(input_unique_positive, target_unique_positive, tolerance)

    # New test cases with decimal inputs
    input_decimal_simple = [Decimal("1.5"), Decimal("2.5"), Decimal("3.0"), Decimal("4.0")]
    target_decimal_simple = [Decimal("5.5"), Decimal("5.5")]
    logger.info("=====10. testing for simple decimal input and decimal target=====")
    test(input_decimal_simple, target_decimal_simple, tolerance)

    input_decimal_with_precision = [Decimal("1.111"), Decimal("2.222"), Decimal("3.333"), Decimal("4.444")]
    target_decimal_with_precision = [Decimal("5.555"), Decimal("5.555")]
    logger.info("=====11. testing for decimal input with higher precision and decimal target=====")
    test(input_decimal_with_precision, target_decimal_with_precision, tolerance)

    input_mixed_decimal = [Decimal("1.5"), Decimal("2.25"), Decimal("-3.75"), Decimal("4.5"), Decimal("-5.5")]
    target_mixed_decimal = [Decimal("0.0"), Decimal("4.75")]
    logger.info("=====12. testing for mixed decimal input with positive and negative numbers and decimal target=====")
    test(input_mixed_decimal, target_mixed_decimal, tolerance)

    input_duplicate_decimal = [Decimal("1.5"), Decimal("1.5"), Decimal("2.5"), Decimal("3.5"), Decimal("4.0")]
    target_duplicate_decimal = [Decimal("3.0"), Decimal("5.0"), Decimal("4.0")]
    logger.info("=====13. testing for duplicate decimal input and decimal target=====")
    test(input_duplicate_decimal, target_duplicate_decimal, tolerance)

    input_decimal_for_zero = [Decimal("2.5"), Decimal("-2.5"), Decimal("3.5"), Decimal("-3.5"), Decimal("5.5")]
    target_decimal_for_zero = [Decimal("5.5"), Decimal("0.0")]
    logger.info("=====14. testing for decimal input with zero-sum possibility and decimal target=====")
    test(input_decimal_for_zero, target_decimal_for_zero, tolerance)

    input_high_precision_decimal = [Decimal("1.234"), Decimal("2.345"), Decimal("3.456"), Decimal("4.567"), Decimal("5.678")]
    target_high_precision_decimal = [Decimal("6.789"), Decimal("10.111")]
    logger.info("=====15. testing for high precision decimal input and decimal target=====")
    test(input_high_precision_decimal, target_high_precision_decimal, tolerance)

    input_decimal_with_rounding = [Decimal("1.005"), Decimal("2.005"), Decimal("3.015"), Decimal("4.025")]
    target_decimal_with_rounding = [Decimal("6.01"), Decimal("4.03")]
    logger.info("=====16. testing for decimal input where rounding may impact result and decimal target=====")
    test(input_decimal_with_rounding, target_decimal_with_rounding, tolerance)
    