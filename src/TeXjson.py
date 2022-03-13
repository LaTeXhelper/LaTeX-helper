import json
import re
import platform

from utils.fileio import *


def tex_json(
    dir_path: str = os.path.join(os.environ['HOME'], '.latexhelper'),
    windows_json_path: str = os.environ['HOME'] + '\\AppData\\Roaming\\Code\\User\\snippets\\latex.json',
    linux_json_path: str = '.'):

    # get all the files
    file_dict = get_tex_list_recursive(dir_path)

    # select the json path according to the platform
    if platform.system() == 'Windows':
        json_path = windows_json_path
    else:
        json_path = linux_json_path
        print('The json file will be generated in current path. You should copy it in ~\\AppData\\Roaming\\Code\\User\\snippets\\latex.json')

    # init settings
    description_path = os.path.join(os.environ['HOME'],'.latexhelper','description.json')
    tex_dict = {}
    describe_dict = {}

    # generate a dictionary for every single tex file
    for file, file_path in file_dict.items():
        with open(file_path,encoding='utf-8') as f:
            text_data = f.read()
            description = re.match(r"%\s*description\s*:\s*(.*)\s*", text_data)
            if (description == None):
                describe_dict[file] = 'None'
            else:
                description = description.group(1)
                describe_dict[file] = description
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


# if __name__ == '__main__':
#     tex_json(
#         os.path.join(os.environ['HOME'],'.latexhelper'),
#         )
