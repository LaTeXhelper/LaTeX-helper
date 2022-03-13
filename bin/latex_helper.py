# coding=utf-8
# author: Jianwei Zhu
# usage: 命令行程序，运行时根据用户的输入，调用src/中的函数，以实现相关功能
#        这里用户接口和函数运行逻辑是分离的

import argparse
import src.TeXinit
import src.TeXlist
import src.TeXtable
import src.TeXjson
import platform
import os


def main():
    if platform.system() == 'Windows':
        os.environ['HOME'] = os.environ['USERPROFILE']
    parser = argparse.ArgumentParser(description='A tool for editing LaTeX')
    parser.add_argument('-i',
                        '--init',
                        default=None,
                        metavar='FILENAME',
                        help='generate a TeX template with your scheduled name')
    parser.add_argument('-l',
                        '--list',
                        action='store_true',
                        help='show your TeX templates')
    parser.add_argument('-t',
                        '--table',
                        nargs=3,
                        metavar=('ROW', 'COLUMN', 'STYLE'),
                        default=[0, 0, 1],
                        help='create a table in your TeX work')
    parser.add_argument('-c',
                        '--csvreader',
                        nargs=2,
                        default=[None, 1],
                        metavar=('CSVNAME', 'STYLE'),
                        help='transform a csv file into a table in your TeX work')
    parser.add_argument('-j',
                        '--json',
                        action='store_true',
                        help='generate a .json file for the auto-completion in VSCode')
    args = parser.parse_args()
    helpflag = 1
    if (args.init != None):
        src.TeXinit.tex_init(args.init)
        helpflag = 0
    if (args.list == True):
        src.TeXlist.tex_list()
        helpflag = 0
    if (args.table != [0, 0, 1]):
        src.TeXtable.tex_table(row=int(args.table[0]),
                               column=int(args.table[1]),
                               style=int(args.table[2]) if args.table[2] not in src.TeXtable.STYLE_DICT.keys() else args.table[2])
        
        helpflag = 0
    if (args.csvreader != [None, 1]):
        src.TeXtable.tex_table(csv_text=args.csvreader[0],
                               style=int(args.csvreader[1]) if args.csvreader[1] not in src.TeXtable.STYLE_DICT.keys() else args.csvreader[1])
        helpflag = 0
    if(args.json == True):
        src.TeXjson.tex_json()
        helpflag = 0
    if (helpflag):
        parser.parse_args(['-h'])

if __name__ == '__main__':
    main()