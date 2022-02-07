from src.TeXtable import tex_table

if __name__ == '__main__':
    # right
    print(tex_table(3, 3, 1))
    print(tex_table(5, 2, 2))
    print(tex_table(4, 4, 3))
    print(tex_table(4, 3, 4))
    print(tex_table(6, 7, "bold_three_lines"))

    # wrong
    print(tex_table(3, 4, 5))
    print(tex_table(2, -1))
