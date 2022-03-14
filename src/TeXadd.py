from utils.fileio import *
from typing import List
import os

def tex_add(name: str,
            template_path: str = os.path.join( os.path.expanduser('~'), '.latexhelper'),
            src_path: str = '.'):
    assert typeguard.check_argument_types()
    template_tex_list = get_tex_list(template_path)
    if template_tex_list.count(name):
        with open(template_path + name + 'tex', 'r') as f:
            tex_strings = f.read()
            write_to_tex(tex_strings, src_path)
    else:
        raise FileNotFoundError(f"No template: {name}.tex.")
