# coding=utf-8
# author: Jianwei Zhu
# usage: 读取LaTeX-templates\\下所有的.tex模板名称，并在终端显示，类似于`pip list`
# 饼: 在LaTeX-templates\\picture.tex中，开头记录了一段关于该模板信息的注释，如果文件中有这样的注释，也可以将其读入并输出，产生这样的效果：
# picture                    nullptr  2022-02-06  A template for pictures(using captionof)
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
    if platform.system() == 'Windows':
        split_symbol = '\\'
    else:
        split_symbol = '/'
    description_path = os.path.join(os.environ['HOME'], '.latexhelper','description.json')
    with open(description_path) as f:
        description_dict = json.load(f)
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


if __name__ == '__main__':
    dfs_showdir()
    create_pd_format()
