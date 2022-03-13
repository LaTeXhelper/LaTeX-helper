# coding=utf-8
# author: Jianwei Zhu
# usage: 读取LaTeX-templates\\下所有的.tex模板名称，并在终端显示，类似于`pip list`
from utils.fileio import *
import os
import json
import pandas as pd
import platform

document_type_list = []
tex_name_list = []
tex_dir_list = []
description_list = []
pdf_list = []

def dfs_showdir(path: str = os.path.join(os.environ['HOME'], '.latexhelper', 'LaTeX-templates'),
                depth: int = 0,
                pdf_father_path: str = os.path.join(os.environ['HOME'], '.latexhelper', 'pdf')):
    # choose split symbol according to the operating system
    if platform.system() == 'Windows':
        split_symbol = '\\'
    else:
        split_symbol = '/'

    # load description dict
    description_path = os.path.join(os.environ['HOME'], '.latexhelper','description.json')
    with open(description_path) as f:
        description_dict = json.load(f)
    
    # recursively get all the information
    for item in os.listdir(path):
        newitem = os.path.join(path, item)
        if os.path.splitext(newitem)[1] == '.tex':
            tex_name_list.append(item)
            document_type_list.append(newitem.split(split_symbol)[-3])
            tex_dir_list.append(newitem.split(split_symbol)[-2])
            if (os.path.exists(os.path.join(pdf_father_path,f'{os.path.splitext(item)[0]}.pdf'))):
                pdf_list.append(os.path.join(pdf_father_path,f'{os.path.splitext(item)[0]}.pdf'))
            else:
                pdf_list.append('None')
            description_list.append(description_dict[item])
        if os.path.isdir(newitem):
            dfs_showdir(newitem, depth + 1)

# show all the info in pandas-Dataframe style
def create_pd_format():
    data = {
        'document type':document_type_list,
        'content type': tex_dir_list,
        'template name': tex_name_list,
        'description':description_list,
        'pdf': pdf_list
    }
    df = pd.DataFrame(data)
    print(df)


def tex_list(path: str = os.path.join(os.environ['HOME'], '.latexhelper','LaTeX-templates'),
             depth: int = 0,
             pdf_father_path: str = os.path.join(os.environ['HOME'],'.latexhelper', 'pdf')):
    dfs_showdir(path,depth,pdf_father_path)
    create_pd_format()

tex_list()