import logging

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