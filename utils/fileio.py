# coding=utf-8
# author: Yujin Wang
# usage: 通用函数，将生成的模板内容写入对应的tex文件

import os
from typing import Dict, List
import typeguard


# 获取当前文件夹下所有的.tex文件（深度为1）
def get_tex_list(path: str, postfix : str = '.tex') -> List:
    assert typeguard.check_argument_types()
    datanames = os.listdir(path)
    tex_list = []
    for dataname in datanames:
        if os.path.splitext(dataname)[1] == postfix:
            tex_list.append(dataname)
    assert typeguard.check_return_type(tex_list)
    return tex_list

# 获取当前文件夹下所有的.tex文件（递归）。返回的字典中key为文件名，value为文件路径
def get_tex_list_recursive(path: str, postfix : str = '.tex', ignore_file_list : List[str] = ['.git']) -> Dict:
    assert typeguard.check_argument_types()
    tex_dict = {}
    for parent,dirnames,filenames in os.walk(path):
        dirnames[:] = [d for d in dirnames if d not in ignore_file_list]
        filenames[:] = [f for f in filenames if f.endswith(postfix)]
        for filename in filenames:
            tex_dict[filename] = os.path.join(parent,filename)
    assert typeguard.check_return_type(tex_dict)
    return tex_dict

# 写入对应的.tex文件
# params: tex_strings LaTeX字符串
# params: path 文件夹路径
def write_to_tex(tex_strings: str, path : str = '.'):
    assert typeguard.check_argument_types()
    tex_files = get_tex_list(path)
    if (len(tex_files) == 0):
        print(
            "[Warning]: No .tex files found in this directory. Create one first."
        )
        return
    elif (len(tex_files) > 1):
        print(
            "[Warning]: There are more than one .tex files. The tex string will write to the file according to the config.yaml"
        )
        # TODO: handling the situation according to the config.yaml
    else:
        tex_file = tex_files[0]
        print(f"Write to {tex_file}")
        with open(tex_file,'a+') as f:
            f.write(tex_strings)
