# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @usage: generate a latex file fluently from a markdown file (using pandoc outside)

import os
import re
import typeguard


def markdown2latex(markdown_file: str,
                   tex_interpreter: str = 'xelatex',
                   using_utf8: bool = True,
                   using_section_number: bool = True,
                   building_pdf: bool = True) -> None:

    assert typeguard.check_argument_types()
    retval = os.system("pandoc -v")
    if (retval != 0):
        raise FileNotFoundError("[Error]: You should download pandoc first. See more about pandoc: https://pandoc.org/")
    tex_file = os.path.splitext(markdown_file)[0] + '.tex'

    # convert the markdown file to latex file
    os.system(f"pandoc {markdown_file} -f markdown -t latex -s -o {tex_file}")

    # delete some harmful sentences
    with open(tex_file, encoding='utf-8') as f:
        output = f.read()
        if (using_utf8):
            output = re.sub(r"\\documentclass\[\s?\]{article}",
                            r"\\documentclass[UTF8]{ctexart}", output)
        if (using_section_number):
            output = re.sub(r"\\setcounter{secnumdepth}.*",
                            r"% enable num label", output)
    
    # generate new tex file
    with open(tex_file, 'w',encoding='utf-8') as f:
        f.write(output)
    if (building_pdf):
        os.system(f'{tex_interpreter} -file-line-error -halt-on-error -interaction=nonstopmode {tex_file}')
        if(os.path.exists(os.path.splitext(markdown_file)[0] + '.pdf')):
            print('[Info]: PDF file generated successfully.')
        else:
            print('[Error]: PDF file generated failed.')
    
