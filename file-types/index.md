(file-types:index)=
# 内容源文件的类型

Jupyter Book 为您的书的内容支持多种源文件。
这些部分涵盖了 Jupyter Book 中的主要内容类型，以及如何控制它们的行为。
有关每种类型的信息，请参阅左边的章节列表。

## 章节目录

```{tableofcontents}
```

## 允许的内容类型

总的来说，以下是 Jupyter Book 支持的内容类型(以及到本书中它们部分的链接)：

[Markdown files](./markdown.md)
: 这些都是用 CommonMark 或 MyST Markdown 编写的文本文件。

[Jupyter notebooks](./notebooks.md)
: 又名 `.ipynb` 文件。这些文件可以包含 MyST Markdown 的 Markdown 单元格。
: Jupyter 笔记本可以利用任何实现了 [Jupyter 消息协议](http://jupyter-client.readthedocs.io/en/latest/messaging.html) 的程序内核来执行代码。
  可用的内核有 [Python](http://ipython.org/notebook.html), [Julia](https://github.com/JuliaLang/IJulia.jl), [Ruby](https://github.com/minad/iruby), [Haskell](https://github.com/gibiansky/IHaskell) 和 [更多其它语言](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels)。

[MyST Markdown notebooks](./myst-notebooks.md)
: 这些是 Markdown 文件(以 `.md` 结尾)，将被转换为笔记本并执行。

[reStructuredText](./restructuredtext.md).
: 这些是 Sphinx 文档引擎(被 Jupyter Book 使用)所使用的文本文件。推荐使用 MyST Markdown。

[Custom notebook formats](file-types:custom)
: 任何其他文件类型都可以在执行前通过指定一个定制的 Python 函数自动转换，例如那些由 Jupytext 转换工具提供的函数。

(rules-all-content-types)=
## 所有内容类型的规则

有一些事情对所有内容类型都适用。以下是一个简短的列表：

* **文件必须有一个 title**。一般来说，这意味着它们必须以一行 `#` 开头
* **只使用一个顶级 header**。因为每个页面必须有一个明确的 title，所以它也必须只有一个顶级 header。您不能在多个 headers 文件中使用单个 `#` 标记。
* **Headers 应该线性增加**。如果您位于带有一个 `#` 的部分中，那么下一个嵌套的部分应该以 `##` 开始。避免直接从 `#` 跳到`###`。

## 文本文件和 `.ipynb` 文件之间的双向转换

关于如何使用的 Jupyter Book 相互转换文本文件和 `.ipynb` 文件，请参阅 [](file-types:custom:jupytext)。
