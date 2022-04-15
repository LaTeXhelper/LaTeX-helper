# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @usage: create a latex template and save it in the template directory for further use

import platform
import os
import typeguard
import json

TEMPLATE_STRING = r'''
% description:
% requirements:
% write a brief description of your template
% If your template needs special packages, please add them in the requirements.

% Add your templates below:

'''

def tex_init(tex_file_name:str,
             windows_editor: str = 'notepad',
             linux_editor: str = 'vim',
             template_dir: str = os.path.join( os.path.expanduser('~'), '.latexhelper', 'LaTeX-templates')) -> None:
    assert typeguard.check_argument_types()
    if (tex_file_name[-4:] != '.tex'):
        tex_file_name += '.tex'

    # select editor according platform
    if (platform.system() == 'Windows'):
        editor = windows_editor
    elif (platform.system() == 'Linux'):
        editor = linux_editor

    # TODO: add legal check
    # choose type. The file will be saved at document_type/content_type
    document_type = input('[info]: Please input your document type:')
    content_type = input('[info]: Please input your content type:')

    # generate path for the file
    if not os.path.exists(os.path.join(template_dir, document_type)):
        print('[Warning]: The document type does not exist. Please check your input.')
        key = input('continue? (Y/n)')
        if (key == 'Y' or key == 'y'):
            os.makedir(os.path.join(template_dir, document_type))
        else:
            return
    if not (os.path.exists(os.path.join(template_dir, document_type, content_type))):
        print('[Warning]: The content type does not exist. Please check your input.')
        key = input('continue? (Y/n)')
        if (key == 'Y' or key == 'y'):
            os.makedirs(os.path.join(template_dir, document_type, content_type))
        else:
            return
    print('[Info]: Add your templates according to the format in the empty file:')
    tex_file_full_path = os.path.join(template_dir,document_type,content_type,tex_file_name)

    # edit your template in editor
    if not (os.path.exists(tex_file_full_path)):
        with open(tex_file_full_path, 'w') as f:
            f.write(TEMPLATE_STRING)
    retval = os.system(f'{editor} {tex_file_full_path}')
    if (retval !=0):
        raise FileNotFoundError(f'Can\'t find {editor}. Consider use another editor!')
    print(f'[Info]: template saved in: {tex_file_full_path}')

    # update gererate.json for search
    description_path = os.path.join( os.path.expanduser('~'), '.latexhelper','description.json')
    with open(description_path) as f:
        description_dict = json.load(f)
    print(tex_file_name)
    description_dict[tex_file_name] = 'None'

    # generate json for vscode auto code generating
    json_str = json.dumps(description_dict)
    with open(description_path, 'w') as f:
        f.write(json_str)
