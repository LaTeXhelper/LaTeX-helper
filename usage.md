# 使用指南

设计可能还有不足之处，之后可能会随时更改！

* 查看帮助

```bash
$ latexhelper -h
# or
$ latexhelper --help
```

* 初始化文档

```bash
$ latexhelper init # 固定创建一个叫a.tex的文件，并在文件中写入常用的宏包
  
$ latexhelper init xxx.tex # 创建xxx.tex文件，并在文件中写入常用的宏包
```

* 写入模板

```bash
$ latexhelper list # 查看所有可用的模板
$ latexhelper <template_name> # 在文件夹下的.tex文件中写入模板
```

* 写入表格(因为表格是可变的，所以单独拿出来作为一个命令)

```bash
$ latexhelper table 5 7 
# 也可以加入更多的设置，指定表格样式等
```

* 载入模板

```bash
$ latexhelper add template.tex # 比如你觉得有一段latex写法很好，你可以将其保存下来，下次就可以直接用latexhelper template来生成代码
```

...