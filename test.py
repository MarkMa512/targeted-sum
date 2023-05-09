import logging
from typing import List
from combination.duplicate_int import sum_combinations, filter_redundant_combinations_set
from utility.validation import validate_input_target, validate_result, validate_viable_result_sets

logging.basicConfig(format="%(asctime)s %(levelname)s %(filename)s:%(funcName)s():%(lineno)i: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S", level=logging.DEBUG)

logger = logging.getLogger(__name__)

def test(input_list: List[int], target_list: List[int])->None:
    """
    Given input and target, validate input and target, find all combinations, filter out redundant combinations, validate result, and print out the result.
    
    :param input_list: input list of integers
    :param target_list: target list of integers

    :returns: None
    """
    logger.info("=====validating input and target=====")
    if not validate_input_target(input_list, target_list):
        return
    
    logger.info("=====finding combinations=====")
    all_combinations: List[List[int]] = sum_combinations(input_list, target_list)
    print(all_combinations)
    logger.info("=====filtering out redundant combinations=====")
    viable_results: List[List[List[int]]] = filter_redundant_combinations_set(input_list, target_list, all_combinations)
    logger.info("=====validating result=====")
    if not validate_viable_result_sets(viable_results):
        return
    counter: int = 0
    for result in viable_results:
        if validate_result(result=result, input_list=input_list, output_list=target_list):
            logger.info(f"=====result {counter} is valid=====")
            print(result)
            counter += 1
    logger.info("=====done=====")


if __name__ == "__main__":
    # input_unique_positive: List[int] = [1, 2, 3, 4, 5] # 1+2+3+4+5=15
    # target_unique_positive: List[int] = [7, 8] # 7+8=15

    # logger.info("=====1. testing for unique positive input and unique positive target=====")
    # test(input_unique_positive, target_unique_positive)

    # input_unique_negative: List[int] = [-1, -2, -3, -4, -5] # -1-2-3-4-5=-15
    # target_unique_negative: List[int] = [-7, -8] # -7-8=-15
    # logger.info("=====2. testing for unique negative input and unique negative target=====")
    # test(input_unique_negative, target_unique_negative)

    # input_unique_mixed: List[int] = [-1, 2, -3, 4, -5] # -1+2-3+4-5=-3
    # target_unique_mixed: List[int] = [-7, 4] # -7+4=-3
    # logger.info("=====3. testing for unique mixed input and unique mixed target=====")
    # test(input_unique_mixed, target_unique_mixed)

    # input_duplicate_positive: List[int] = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 4] # 1+2+3+4+5+1+2+3+4+5+4=34
    # target_duplicate_positive: List[int] = [7, 8, 9, 10] # 7+8+9+10=34
    # logger.info("=====4. testing for duplicate positive input and duplicate positive target=====")
    # test(input_duplicate_positive, target_duplicate_positive)

    # input_duplicate_negative: List[int] = [-1, -2, -3, -4, -5, -1, -2, -3, -4, -5, -4] # -1-2-3-4-5-1-2-3-4-5=-30
    # target_duplicate_negative: List[int] = [-7, -8, -9, -10] # -7-8-9-10=-34
    # logger.info("=====5. testing for duplicate negative input and duplicate negative target=====")
    # test(input_duplicate_negative, target_duplicate_negative)

    # input_duplicate_mixed: List[int] = [-1, 2, -3, 4, -5, -1, 2, -3, 4, -5] # -1+2-3+4-5-1+2-3+4-5=-6
    # target_duplicate_mixed: List[int] = [-7, 4, -8, 5] # -7+4-8+5=-6
    # logger.info("=====6. testing for duplicate mixed input and duplicate mixed target=====")
    # test(input_duplicate_mixed, target_duplicate_mixed)

    input_duplicate_mixed_for_zero: List[int] = [-1, 2, -3, 4, -5, -1, 2, -3, 4, -5] # -1+2-3+4-5-1+2-3+4-5=-6
    target_duplicate_mixed_for_zero: List[int] = [-7, 4, -8, 1, 0, 4] # -7+4-8+1+0+4=-6
    logger.info("=====7. testing for duplicate mixed input and duplicate mixed target with zero=====")
    test(input_duplicate_mixed_for_zero, target_duplicate_mixed_for_zero)

    input_duplicate_mixed_for_zero_2: List[int] = [-1, 2, -3, 4, -5, -1, 2, -3, 4, -5] # -1+2-3+4-5-1+2-3+4-5=-6
    target_duplicate_mixed_for_zero_2: List[int] = [0, -1, 3, -8] # 0 + -1 + 3 + -8 = -6 
                                                    # 0 = -1 +2 - 1, 
                                                    # -1 = 2 - 3, 
                                                    # 3 = 4 - 5 + 4, 
                                                    # -8 = -3 - 5

    logger.info("=====8. testing for duplicate mixed input and duplicate mixed target with zero=====")
    test(input_duplicate_mixed_for_zero, target_duplicate_mixed_for_zero)

    input_duplicate_mixed_for_zero_3 = [1, 2, 2, 3, 4, 5, 2, 2, 7, 8, -8, 8] # 1+2+2+3+4+5+2+2+7+8-8+8=54
    target_duplicate_mixed_for_zero_3 = [8, 9, 4, 15, 0] # 8+9+4+15+0=54
                                        # 8 = 1 + 2 + 2 + 3
                                        # 9 = 4 + 5
                                        # 4 = 2 + 2
                                        # 15 = 7 + 8
                                        # 0 = -8 + 8
                                        
    logger.info("=====9. testing for duplicate mixed input and duplicate mixed target with zero=====")
    test(input_duplicate_mixed_for_zero_3, target_duplicate_mixed_for_zero_3)
