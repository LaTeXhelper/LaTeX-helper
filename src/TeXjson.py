# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @usage: generate the vscode json file for code completion, using all the templates in the folder before

import json
import re
import platform

from utils.fileio import *


def tex_json(
    dir_path: str = os.path.join( os.path.expanduser('~'), '.latexhelper'),
    windows_json_path: str =  os.path.expanduser('~') + '\\AppData\\Roaming\\Code\\User\\snippets\\latex.json',
    linux_json_path: str = './latex.json'):

    # get all the files
    file_dict = get_tex_list_recursive(dir_path)

    # select the json path according to the platform
    if platform.system() == 'Windows':
        json_path = windows_json_path
    else:
        json_path = linux_json_path
        if json_path == './latex.json':
            print('[Warning]: The json file will be generated in current path. You should copy it in ~\\AppData\\Roaming\\Code\\User\\snippets\\latex.json')

    # init settings
    description_path = os.path.join(os.path.expanduser('~'), '.latexhelper', 'description.json')
    requirements_pdf_path = os.path.join(os.path.expanduser('~'), '.latexhelper', 'requirements_pdf.txt')
    requirements_ppt_path = os.path.join(os.path.expanduser('~'), '.latexhelper', 'requirements_ppt.txt')

    tex_dict = {}
    describe_dict = {}
    requirements_pdf_list = []
    requirements_ppt_list = []

    # generate a dictionary for every single tex file
    for file, file_path in file_dict.items():
        with open(file_path,encoding='utf-8') as f:
            text_data = f.read()

            # get the description
            description = re.search(r"%\s*description\s*:\s*(.*)", text_data)
            if (description == None):
                describe_dict[file] = 'None'
            else:
                description = description.group(1)
                describe_dict[file] = description

            # get the requirements
            requirements = re.search(r"requirement\s*:\s*(.*)", text_data)
            if (requirements == None):
                requirements = 'None'
            else:
                requirements = requirements.group(1)
                requirements = requirements.split()
                if 'article' in file_path:
                    requirements_pdf_list += requirements
                else:
                    requirements_ppt_list += requirements

            single_tex_dict = {
                'prefix': os.path.splitext(file)[0],
                'body': text_data,
                'description': description
            }
            fragment = os.path.splitext(file)[0].replace('_', ' ')
            tex_dict[fragment] = single_tex_dict

    # generate json for vscode auto code generating
    json_str = json.dumps(tex_dict)
    with open(json_path, 'w') as f:
        f.write(json_str)

    # generate description json for showing list
    describe_str = json.dumps(describe_dict)
    with open(description_path, 'w') as f:
        f.write(describe_str)

    # collect all the packages
    requirements_ppt_list = list(set(requirements_ppt_list))
    requirements_pdf_list = list(set(requirements_pdf_list))
    with open(requirements_pdf_path, 'w') as f:
        for package in requirements_pdf_list:
            if 'usepackage' in package:
                f.write(package + '\n')
            else: 
                f.write('\\usepackage{' + package + '}\n')

    with open(requirements_ppt_path, 'w') as f:
        for package in requirements_ppt_list:
            if 'usepackage' in package:
                f.write(package + '\n')
            else: 
                f.write('\\usepackage{' + package + '}\n')

    print('[Info]: The json file has been generated in ' + json_path)