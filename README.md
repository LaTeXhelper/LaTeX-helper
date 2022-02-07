# LaTeX-helper

## 概况

一个便于书写$\LaTeX$文本的小工具。基于Python语言编写。

## 目录结构

```markdown
bin/ # 命令行程序入口
src/ # 存放核心运行逻辑的Python文件
test/ # 存放测试文件
utils/ # 存放一些常用功能封装成的接口，便于调用
LaTeX-templates/ # git submodule, 用于存放模板文件
info/ # 存放可能对项目开发有帮助的一些文档
picture/ # 存放.md文件中用到的图片
development.md # 开发日志
README.md # 项目介绍
usage.md # 教程
requirements.txt # 存放需要安装的Python第三方库及其版本要求
```

## 配置

```bash
$ pip install -r requirements.txt # 安装需要的第三方库
$ git submodule update --init --recursive # 拉取子模块
```

如子模块需要更新，则需要执行以下指令：

```bash
$ cd LaTeX-templates
$ git pull  
```


## 可能需要用到的工具/库

* Python相关

  * `argparse` Python用于编写命令行程序的一个库

  * `re` Python处理正则表达式的一个库。因为这个项目需要大量处理文本的方法，所以我感觉大概率会用到这个库。在线测试正则表达式可以用[https://regex101.com/](https://regex101.com/)

  * Python文件读写的相关机制

* LaTeX相关

  * 如何通过命令行操作LaTeX相关指令，编译生成pdf文件

  * pandoc的使用  

  * 如何使用LaTeX做PPT---beamer  

...

## 开发方法

* 将 LaTeX-helper 仓库 fork 到个人 GitHub 仓库中
* 创建自己的分支，例如可以将开发分支命名为mydev
* 进行开发
* 将 LaTeX-helper 仓库 dev 分支的最新进度 pull 到自己的仓库中
* 向 LaTeX-helper 的 dev 分支提出 pull request

## 运行环境

windows，Linux(Ubuntu)；Python3.x+

## Tips

* 注重代码的规范性，多写注释，多格式化代码。

* 注重代码的可维护性，尽量解耦，让项目看起来更像一个工程而不是一个脚本，但也不必太拘泥于代码的结构，有什么好的想法先大胆写，之后有精力再重构。

* 随时交流！

