# 如何部署Python项目

## 项目构成

Python项目的部署基于`setup.py`。一般来说，一个需要部署的Python项目应该具有一定的目录规范，以本项目为例：
```python
.
├── bin
│   ├── __init__.py # 每一个需要进行打包的文件夹中都必须放置一个`__init__.py`，否则setup.py将无法识别
│   └── latex_helper.py # 命令行程序的入口
├── generate_pdf.sh # 项目的附属脚本 
├── generate_ppt.sh
├── README.md
├── setup.py # 注意setup.py一定要放在项目的根目录下
├── src
│   ├── __init__.py
│   ├── TeXadd.py
│   ├── TeXinit.py
│   ├── TeXlist.py
│   └── TeXtable.py
├── test
│   ├── __init__.py
│   ├── test_csv.py
│   ├── test_table.py
│   └── test_write.py
└── utils
    ├── csvreader.py
    ├── fileio.py
    └── __init__.py
```

## `setup.py`的编写

```python
from importlib_metadata import entry_points
from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="latexhelper", # 项目名称
    version="1.0", # 版本号
    author="Yujin Wang, Zhi Wang, Jianwei Zhu", # 作者
    author_email="1329438302@qq.com", # 邮箱
    description="A command line tool for writing LaTeX.", # 项目的简要描述
    packages=find_packages(),
    license='MIT', # 使用MIT License
    long_description=read('README.md'), # 详细说明，此处采用直接读取README.md的方法

    entry_points={
        'console_scripts': [
            'latexhelper = bin.latex_helper:main'
        ]
    }, # 命令行程序的入口

    scripts=['generate_pdf.sh','generate_ppt.sh'], # 所需要添加的附加脚本
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console"
    ], # 一些分类，如开发进展、程序分类等
)

```

编写完毕后，即可分平台安装。

### Linux

```bash
$ python3 setup.py build # 在当前文件夹下构建项目
$ sudo python3 setup.py install # 将该项目安装至本机，以供在命令行中直接调用。通常需要root权限
```

第二句指令将生成大量内容，我们重点关注这三句话：
```python
Installing generate_pdf.sh script to /usr/local/bin # 将项目的附属脚本安装到`/usr/local/bin`，以便用户在命令行中直接调用
Installing generate_ppt.sh script to /usr/local/bin 
Installing latexhelper script to /usr/local/bin # 此后，在命令行中直接输入`latexhelper`，就相当于调用`bin/latex_helper`中的main函数
```
这样我们就完成了项目在Linux平台上的部署。