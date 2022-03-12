from src.TeXtable import tex_table

if __name__ == '__main__':
    # right
    print(tex_table(style = 1,csv_text='./test/test.csv'))
    print(tex_table(style = 2,csv_text='./test/test.csv'))
    print(tex_table(style = 3,csv_text='./test/test.csv'))
    print(tex_table(style = 4,csv_text='./test/test.csv'))