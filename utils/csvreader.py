import csv
import typeguard
from typing import Tuple

def get_csv_list(csv_text: str, delimiter: str = ',') -> Tuple:
    assert typeguard.check_argument_types()
    csv_list = []
    max_elem_length = 0
    row_num = 0
    column_list = []
    with open(csv_text) as f:
        reader = csv.reader(f, delimiter=delimiter)
        for row in reader:
            column_num = 0
            for elem in row:
                csv_list.append(elem)
                column_num += 1
                if max_elem_length < len(elem):
                    max_elem_length = len(elem)
            row_num += 1
            column_list.append(column_num)
    return csv_list, row_num, column_list, max_elem_length + 1