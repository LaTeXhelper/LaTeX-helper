# LaTeX命令行小工具

LaTeX是一种高度模板化的语言——我们不需要深入了解其原理，只需要记住一些常用模板就可以了，仿照这个命令行程序，我们只需要记住一些常用模板，然后在命令行里敲一下，latex代码就有了。

比如这个程序可以有以下操作：

```bash
$ latexhelper init xxx.tex # 创建一个.tex文件，并在文件中写入常用的宏包
$ latexhelper picture # 在当前文件夹下的.tex文件中，写入一段插入图片的代码
$ latexhelper table 5 7 # 在当前文件夹下的.tex文件中，写入一段插入表格(5行7列)的代码
$ latexhelper add template.tex # 比如你觉得有一段latex写法很好，你可以将其保存下来，下次就可以直接用latexhelper template来生成代码
$ latexhelper pull # 拉取别人写的优秀模板(可以用git实现)
$ latexhelper push # 将自己的模板提交到github上
$ latexhelper show # 查看现在可用的latex模板
...
```

基础是命令行程序，但也可以魔改成GUI，甚至是vscode插件。

