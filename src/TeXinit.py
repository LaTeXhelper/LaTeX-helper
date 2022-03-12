# coding=utf-8
# author: Jianwei Zhu
# usage: 根据文件名称生成文件
# 饼: 鲁棒性：如果用户输入的文件名带后缀如何处理？不带后缀如何处理？如果不输入文件名如何处理？
import platform
import os
import typeguard

TEMPLATE_STRING = r'''
% description:
% requirements:

% Add your templates below:

'''

def tex_init(tex_file_name: str,
             windows_editor: str = 'notepad',
             linux_editor: str = 'notepad.exe')->None:
    assert typeguard.check_argument_types()
    if (tex_file_name[-4:] != '.tex'):
        tex_file_name += '.tex'
    with open(tex_file_name, 'w') as f:
        f.write(TEMPLATE_STRING)
    print('Add your templates according to the format in the empty file:')
    if (platform.system() == 'Windows'):
        os.system(f'{windows_editor} {tex_file_name}')
    elif (platform.system() == 'Linux'):
        os.system(f'{linux_editor} {tex_file_name}')
    print(f'template saved: {tex_file_name}')


if __name__ == '__main__':
    tex_init('xxxx.tex')
