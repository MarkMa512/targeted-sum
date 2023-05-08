import logging
from combination_finder import unique_input, duplicate_input
from utility.csv import read_csv, export_to_csv
from utility.validation import validate_input, validate_unique_input, validate_result

logging.basicConfig(format="%(asctime)s %(levelname)s %(filename)s:%(funcName)s():%(lineno)i: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S", level=logging.DEBUG)

logger = logging.getLogger(__name__)

def main():
    logger.info("reading input file")
    input_list = read_csv('input.csv')
    target_list = read_csv('target.csv')
