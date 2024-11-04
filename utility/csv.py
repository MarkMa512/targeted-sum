import logging
import csv
from typing import List, Union
from decimal import Decimal

logger = logging.getLogger(__name__)

def read_csv(csv_name: str) -> List[Union[int, Decimal]]:
    """
    Read a CSV and return a list of integers or decimals based on the content.

    :param csv_name: name of file
    :return: list of integers or decimals
    """
    logger.info(f'---reading {csv_name}---')
    values = []
    with open(csv_name, newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            value = row[0].strip()  # Get the value and strip any whitespace
            try:
                if '.' in value:  # If there's a decimal point, use Decimal
                    values.append(Decimal(value))
                else:  # Otherwise, try to convert to int
                    values.append(int(value))
            except ValueError:
                logger.error(f"+++invalid data '{value}' in {csv_name}+++")
                continue
    return values

def export_to_csv(combinations: List[List[Union[int, Decimal]]], file_name: str) -> None:
    """
    Export combinations to CSV file.

    :param combinations: list of combinations
    :param file_name: name of file
    """
    logger.info(f'---exporting to {file_name}---')
    with open(file_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for combination in combinations:
            csv_writer.writerow([str(item) for item in combination])  # Convert each item to string