# 命令行界面

Jupyter Book 提供了一个命令行界面，可以方便地构建图书和运行一些常用函数。这个页面包含了关于 CLI（command-line interface）可以做什么的信息。

本页面是 CLI 的完整参考。对于新手想开始与木星书 CLI，我们建议从 [](../start/overview.md) 开始。

:::{note}

您也可以在命令行中使用 ``jb`` 来简写 ``jupyter-book``。
例如：`jupyter-book build mybook/` 等价于 ``jb build mybook/``。

:::

**请参阅下面的完整命令行参考资料**

```{eval-rst}
.. click:: jupyter_book.cli.main:main
   :prog: jupyter-book
   :nested: full
```
