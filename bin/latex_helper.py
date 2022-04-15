# coding=utf-8
# author: Jianwei Zhu
# usage: Command line interface for LaTeX-templates


import src.TeXinit
import src.TeXlist
import src.TeXtable
import src.TeXjson
import src.TeXmarkdown

import argparse
import yaml
from dataclasses import dataclass
import os

@dataclass
class Config:
    table_style: int = 1
    windows_editor: str = 'notepad'
    linux_editor: str = 'vim'
    windows_json_path: str = '~\\AppData\\Roaming\\Code\\User\\snippets\\latex.json'
    linux_json_path: str = './latex.json'


def main():
    config_path = os.path.join(os.path.expanduser('~'), '.latexhelper', 'config.yaml')
    
    cfg = Config()

    if(os.path.exists(config_path)):
        with open(config_path, 'r') as f:
            config_dict = yaml.load(f)
            cfg.update(config_dict)

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
    parser.add_argument('-m',
                        '--md',
                        nargs=1,
                        default=[None],
                        metavar=('MARKDOWNNAME'),
                        help='convert a markdown file into a TeX file which can be compiled by LaTeX beautifully')
    
    args = parser.parse_args()
    helpflag = 1
    if (args.init != None):
        src.TeXinit.tex_init(args.init, cfg.windows_editor, cfg.linux_editor)
        helpflag = 0
    if (args.list == True):
        src.TeXlist.tex_list()
        helpflag = 0
    if (args.table != [0, 0, 1]):
        src.TeXtable.tex_table(row=int(args.table[0]),
                               column=int(args.table[1]),
                               style=int(cfg.table_style) if args.table[2] not in src.TeXtable.STYLE_DICT.keys() else args.table[2])
        helpflag = 0
    if (args.csvreader != [None, 1]):
        src.TeXtable.tex_table(csv_text=args.csvreader[0],
                               style=int(cfg.table_style) if args.csvreader[1] not in src.TeXtable.STYLE_DICT.keys() else args.csvreader[1])
        helpflag = 0
    if(args.json == True):
        src.TeXjson.tex_json(windows_json_path=cfg.windows_json_path, linux_json_path=cfg.linux_json_path)
        helpflag = 0
    if(args.md != [None]):
        print(args.md[0])
        src.TeXmarkdown.markdown2latex(markdown_file=args.md[0])
        helpflag = 0
    if (helpflag):
        parser.parse_args(['-h'])

if __name__ == '__main__':
    main()