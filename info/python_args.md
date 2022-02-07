# Python命令行参数与Python模块运行

当运行`test/test_table.py`时，有以下几种运行方法：

```bash
# 在LaTeX-Helper/目录下
$ python -m test.test_table # OK
$ python test/test_table.py # not OK
# 在test/目录下
$ python -m test_table # not OK
$ python test_table.py # not OK
```

其中有一定的原因：

## `__init__.py`
具体可见[https://zhuanlan.zhihu.com/p/115350758](https://zhuanlan.zhihu.com/p/115350758)。简单来说，当python检测到一个目录下存在__init__.py文件时，python就会把它当成一个模块(module)。这个文件可以是空文件，也可以添加相关内容。

## `-m`

```bash
$ python run.py # 直接运行
$ python -m run.py # 把模块当作脚本启动
```
这两种运行方法有什么具体区别？详见[https://www.cnblogs.com/xueweihan/p/5118222.html](https://www.cnblogs.com/xueweihan/p/5118222.html)。简单来说，直接启动是把`run.py`文件所在的目录放到了`sys.path`属性中。
模块启动是把你输入命令的目录（也就是当前路径），放到了`sys.path`属性中。`run.py`会从`sys.path`中读取其它模块。

所以回过头看，第2个和第4个指令只会将`test/`目录放在`sys.path`中，自然识别不到外部的`src/`，而第3个指令由于在`test/`目录下运行，自然也不会识别到外部的`src/`模块。