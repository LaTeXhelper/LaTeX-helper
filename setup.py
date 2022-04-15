from importlib_metadata import entry_points
from setuptools import setup, find_packages
import os
import platform

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname),encoding='utf-8').read()

setup(
    name="latexhelper",
    version="1.0",
    author="Yujin Wang, Zhi Wang, Jianwei Zhu",
    author_email="1329438302@qq.com",
    description="A command line tool for writing LaTeX.",
    packages=find_packages(),
    license='MIT',
    long_description=read('README.md'),
    entry_points={'console_scripts': ['latexhelper = bin.latex_helper:main']},
    scripts=(['generate_pdf.ps1','generate_ppt.ps1'] if (platform.system()== 'Windows') else ['generate_pdf.sh','generate_ppt.sh']),
    classifiers=["Development Status :: 3 - Alpha", "Environment :: Console"],
)