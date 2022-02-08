## 2022-2-6 develop 1
王治：bin/latex_helper.py
朱健维：src/TeXinit.py,list.py
王与进：src/TeXtable.py

由于是第一次开发，所以就不设置ddl了，大家先想想怎么写，有问题随时讨论。

## 2022-2-8
第二轮开发计划：
1. 在执行`latexhelper init xx.tex`时，可以生成一个`config.yaml`文件。在第一次生成时，该文件的内容均为默认值，用户也可以根据自己的喜好修改。当用户缺省某些命令行参数时，可以直接根据`config.yaml`的设置读取命令行参数设置值。
2. 直接读取`.txt`或`.csv`中的数据，将其转换为tex表格写入文件中。
...（初步想法，仅供参考）