# coding=utf-8
# author: Yujin Wang
# usage: 根据用户的需求生成表格

from typing import Union
from utils.csvreader import get_csv_list
from utils.fileio import write_to_tex
import typeguard

BEGIN_COMMAND = r"\begin{tabular}"
END_COMMAND = r"\end{tabular}"
H_LINE = r"\hline" + "\n"
POSITION_TIPS = r"% You can change c(which means center) to l(which means left) or r(which means right) according to your need."
STYLE_DICT = {
    "no_lines": 1,
    "full_lines": 2,
    "three_lines": 3,
    "bold_three_lines": 4
}
TOP_RULE = r'\toprule' + '\n'
MID_RULE = r'\midrule' + '\n'
BOTTOM_RULE = r'\bottomrule' + '\n'


def tex_table(row: int = None, column: int = None, style: Union[int, str] = 1, csv_text: str = None) -> None:
    # exception handling
    assert typeguard.check_argument_types()
    if (row != None and row <= 0):
        raise ValueError(f"Row should be positive, got {row}.")
    if (row != None and column <= 0):
        raise ValueError(f"Column should be positive, got {column}.")
    if (csv_text == None):
        if (row == None):
            raise ValueError(f"No csv file, but row is not decided.")
        if (column == None):
            raise ValueError(f"No csv file, but column is not decided.")
    if (style not in STYLE_DICT.keys() and style not in STYLE_DICT.values()):
        raise ValueError(
            f"Type \"{style}\" is not supported, the styles now supported: {STYLE_DICT}"
        )
    if (isinstance(style, int)):
        _style = style
    else:
        _style = STYLE_DICT.get(style)

    # using csv or not
    if(csv_text != None):
        csv_list, row_num, column_list, max_elem_length = get_csv_list(csv_text)
        row = row_num
        column = max(column_list)
    else:
        max_elem_length = 2

    # generating strings
    table_string = ''

    table_position_string = r'{'
    for i in range(column):
        if (_style == 2):
            table_position_string += '|'
        table_position_string += 'c'
    if(_style == 2):
        table_position_string += r'|'
    table_position_string += r'}'

    if(csv_text != None):
        table_row_string_list = []
        idx = 0
        for i in range(row):
            table_row_string = ''
            for j in range(column):
                if (j < column_list[i]):
                    table_row_string += csv_list[idx]
                    table_row_string += ' ' * (max_elem_length - len(csv_list[idx]))
                    idx += 1
                else:
                    table_row_string += ' ' * max_elem_length
                table_row_string += '& '
            table_row_string = table_row_string[0:-2]
            table_row_string += r'\\'
            table_row_string_list.append(table_row_string)
    else:
        table_row_string = ' '*max_elem_length
        for i in range(column - 1):
            tmp = ' '*max_elem_length
            table_row_string += ('&' + tmp)
    table_row_string += r'\\'

    table_string += POSITION_TIPS
    table_string += '\n'
    if (_style == 4):
        table_string += r"% warning: add \usepackage{booktabs} at top."
        table_string += '\n'
    table_string += BEGIN_COMMAND
    table_string += table_position_string
    table_string += '\n'

    for i in range(row):
        if (_style == 2):
            table_string += H_LINE
        if (i == 0):
            if (_style == 3):
                table_string += H_LINE
            elif (_style == 4):
                table_string += TOP_RULE
        elif (i == 1):
            if (_style == 3):
                table_string += H_LINE
            elif (_style == 4):
                table_string += MID_RULE
        if(csv_text != None):
            table_string += table_row_string_list[i]
        else:
            table_string += table_row_string
        table_string += '\n'

    if (_style == 2 or _style == 3):
        table_string += H_LINE
    elif (_style == 4):
        table_string += BOTTOM_RULE
    table_string += END_COMMAND
    table_string += '\n'

    write_to_tex(table_string, '.')
