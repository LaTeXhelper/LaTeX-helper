# coding=utf-8
# author: Yujin Wang
# usage: 根据用户的需求生成表格

from typing import Union
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


def tex_table(row: int, column: int, style: Union[int, str] = 1) -> str:
    # exception handling
    assert typeguard.check_argument_types()
    if (row <= 0):
        raise ValueError(f"Row should be positive, got {row}.")
    if (column <= 0):
        raise ValueError(f"Column should be positive, got {column}.")
    if (style not in STYLE_DICT.keys() and style not in STYLE_DICT.values()):
        raise ValueError(
            f"Type \"{style}\" is not supported, the styles now supported: {STYLE_DICT}"
        )
    if (isinstance(style, int)):
        _style = style
    else:
        _style = STYLE_DICT.get(style)

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

    table_row_string = '  '
    for i in range(column - 1):
        table_row_string += '&  '
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

        table_string += table_row_string
        table_string += '\n'

    if (_style == 2 or _style == 3):
        table_string += H_LINE
    elif (_style == 4):
        table_string += BOTTOM_RULE
    table_string + '\n'

    assert typeguard.check_return_type(table_string)
    return table_string
