import logging
import csv
from typing import List

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_csv(csv_name: str) -> List[int]:
    """
    read a csv and return list of integers

    :param csv_name: name of file
    :return: list of integers
    """
    logging.info(f'---reading {csv_name}---')
    with open(csv_name, newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        return [int(row[0]) for row in csv_reader] # each row is a list of one element, so we return the first element
    
def export_to_csv(combinations:List[List[int]], file_name:str)-> None:
    """
    export combinations to csv file

    :param combinations: list of combinations
    :param file_name: name of file
    """
    logging.info(f'---exporting to {file_name}---')
    with open(file_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for combination in combinations:
            csv_writer.writerow(combination)