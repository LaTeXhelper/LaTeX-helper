import json
import re

from utils.fileio import *

def tex_json(dir_path: str, json_path: str = None):
    # get all the files
    file_dict = get_tex_list_recursive(dir_path)

    # init settings
    description_path = os.path.join(os.environ['HOME'],'.latexhelper','description.json')
    tex_dict = {}
    describe_dict = {}

    # generate a dictionary for every single tex file
    for file, file_path in file_dict.items():
        with open(file_path) as f:
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


if __name__ == '__main__':
    tex_json(
        os.path.join(os.environ['HOME'],'.latexhelper'),
        "C:/Users/86181/AppData/Roaming/Code/User/snippets/latex.json")
