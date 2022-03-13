# latexhelper

A simple tool for writing latex in vscode.
## build

We suggest [Anaconda](https://www.anaconda.com/) to setup all the running environment.

### preparation before setup

In order to avoid unknown problems, we suggest using `python3.8` to run this project.

```bash
$ conda create -n latex python=3.8 # the environment name is not important, you can choose other name, or you can just install in base
## you can change your conda source for faster speed:
# conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
# conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
# conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
# conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
# conda config --set show_channel_urls yes
$ conda install pip
## you can change your pip source for faster speed:
# pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

### setup the project

```bash
# install scripts
$ git clone git@github.com:git@github.com:LaTeXhelper/LaTeX-helper.git
$ cd LaTeX-helper
$ conda activate latex # same as your previous name
$ pip install -r requirements.txt
$ python setup.py install
# install templates
$ git clone git@github.com:LaTeXhelper/LaTeX-templates.git ~/.latexhelper
```

Then, you can use `latexhelper`，`generate_pdf.sh`，`generate_ppt.sh` command after `conda activate latex`(or some other name you set before).