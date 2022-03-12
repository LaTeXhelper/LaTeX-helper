from utils.fileio import *
from utils.fileio import get_tex_list, write_to_tex
from src.TeXtable import *
if __name__ == '__main__':
    print(get_tex_list('.'))
    tablestring = tex_table(5, 5, 1)
    write_to_tex(tablestring, '.')
