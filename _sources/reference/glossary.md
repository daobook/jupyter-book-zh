# 术语表

整个 Jupyter Book 中使用的常用术语的术语表。

```{glossary}
[CommonMark](https://commonmark.org/)
    Markdown 的标准语法可在许多社区和项目中使用。它是 Jupyter Notebook 的 Markdown 基本风格，也是 {term}`MyST Markdown <MyST>` 和 Jupyter Book 的基本风格。

[ExecutableBookProject](https://executablebooks.org/en/latest/)
    该项目支持和开发 Jupyter Book 使用的许多核心工具。

[MyST Markdown](https://myst-parser.readthedocs.io/en/latest/using/syntax.html)
[MyST](https://myst-parser.readthedocs.io/en/latest/using/syntax.html)
    专为 {term}`Sphinx` 项目使用而设计的 Markdown 风格。它是 {term}`CommonMark Markdown <CommonMark>` 和一些额外的语法片段的组合，以支持 Sphinx 的功能，因此您可以用纯 Markdown 编写 Sphinx 文档。它是 Jupyter Book 使用的核心技术之一。

[MyST-Parser](https://myst-parser.readthedocs.io/en/latest/)
    {term}`Sphinx` 的解析器，它可以读取以 MyST Markdown 编写的内容。{term}`MyST-NB` 也使用它来解析 Jupyter 笔记本内部的 MyST Markdown。

[MyST-NB](https://myst-nb.readthedocs.io/en/latest/)
    {term}`Sphinx` 的扩展，它使用 {term}`MyST-Parser <MyST>` 将 Jupyter 笔记本直接解析为 Sphinx。这还允许用户在用 Sphinx 解析的笔记本中编写 MyST Markdown。它是 Jupyter Book 使用的核心技术之一。

[Sphinx](https://www.sphinx-doc.org/en/master/)
    用 Python 编写的文档引擎。Sphinx 支持许多科学和学术出版所必需的功能。它是 Jupyter Book 使用的核心技术之一。

[Binder](https://mybinder.org)
    一种免费的公共服务，用于运行可复用的交互式计算环境。
    Binder 是 Jupyter 社区成员运行的 100% 开源的基础结构。Binder 项目背后的基础技术是 {term}`BinderHub`。

[BinderHub](https://binderhub.readthedocs.io/en/latest/)
    BinderHub 是 mybinder.org 的基础技术，是一种在 Kubernetes 上运行的开源工具，并利用 {term}`JupyterHub` 来提供用户可在 GitHub 上托管的实时可复用的交互式计算环境。

[Google Colab](https://colab.research.google.com/)
    A Jupyter Notebook service from Google that provides access to free computing resources,
    including GPUs and TPUs.

[JupyterHub](https://jupyterhub.readthedocs.io/en/stable/)
    JupyterHub 是 Jupyter 社区的核心开源工具，它允许您部署向多个用户提供远程数据科学环境的应用程序。它可以部署在云中，也可以部署在您自己的硬件上。

[Jupyter-Cache](https://github.com/executablebooks/jupyter-cache)
    一个开源工具，用于执行和缓存 Jupyter Notebook 内容的输出。输出缓存在一个隐藏的文件夹中，因此不需要直接将其包含在源文件中。

[Sphinx Book Theme](https://github.com/executablebooks/sphinx-book-theme)
    [PyData Sphinx 主题](https://pydata-sphinx-theme.readthedocs.io/en/latest/) 的自定义版本，它定义了 Jupyter Book 的外观。
```
