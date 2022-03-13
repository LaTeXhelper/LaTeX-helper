# coding=utf-8
# author: Zhi Wang
# usage: 命令行程序，运行时根据用户的输入，调用src/中的函数，以实现相关功能
#        这里用户接口和函数运行逻辑是分离的
import argparse
import src.TeXinit
import src.TeXlist
import src.TeXtable


def main():
    parser = argparse.ArgumentParser(description='A tool for editing LaTeX')
    parser.add_argument('-i',
                        '--init',
                        default=None,
                        metavar='FILENAME',
                        help='generate a TeX file with your scheduled name')
    parser.add_argument('-d',
                        '--init_default',
                        action='store_true',
                        help='generate a TeX file with the default name')
    parser.add_argument('-l',
                        '--list',
                        action='store_true',
                        help='show your TeX templates')
    parser.add_argument('-t',
                        '--table',
                        nargs=2,
                        type=int,
                        metavar=('ROW', 'COLUMN'),
                        default=[0, 0],
                        help='create a table in your TeX work')
    parser.add_argument(
        '-c',
        '--readcsv',
        default=None,
        metavar='CSVNAME',
        help='transform a csv file into a table in your TeX work')
    args = parser.parse_args()
    if (args.init != None):
        src.TeXinit.tex_init(args.init)
    if (args.init_default == True):
        src.TeXinit.tex_add()
    if (args.list == True):
        src.TeXlist.tex_list()
    if (args.table != [0, 0]):
        pass
    if (args.readcsv != None):
        pass


if __name__ == '__main__':
    main()
