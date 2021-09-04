# Jupyter Book 中文

[![GitHub issues](https://img.shields.io/github/issues/xinetzone/jupyter-book)](https://github.com/xinetzone/jupyter-book/issues) [![GitHub forks](https://img.shields.io/github/forks/xinetzone/jupyter-book)](https://github.com/xinetzone/jupyter-book/network) [![GitHub stars](https://img.shields.io/github/stars/xinetzone/jupyter-book)](https://github.com/xinetzone/jupyter-book/stargazers) [![GitHub license](https://img.shields.io/github/license/xinetzone/jupyter-book)](https://github.com/xinetzone/jupyter-book/blob/main/LICENSE)  ![repo size](https://img.shields.io/github/repo-size/xinetzone/jupyter-book.svg) [![contributors](https://img.shields.io/github/contributors/xinetzone/jupyter-book.svg)](https://github.com/xinetzone/jupyter-book/graphs/contributors) [![watcher](https://img.shields.io/github/watchers/xinetzone/jupyter-book.svg)](https://github.com/xinetzone/jupyter-book/watchers) ![](https://github.com/xinetzone/jupyter-book/actions/workflows/docs.yml/badge.svg)

```{div} w3-pale-green w3-card w3-padding w3-round-xlarge w3-margin-top
Jupyter Book 可以直接运行代码，且持续化集成和部署到 GitHub Pages。

本项目是 [executablebooks/jupyter-book](https://github.com/executablebooks/jupyter-book) 的中文版本。欢迎提出翻译建议！
```

````{admonition} 导航
:class: tip, dropdown; w3-pale-blue w3-card-4 w3-padding w3-round-xlarge w3-margin-top

```{tableofcontents}
```
````

(intro)=
## Jupyter <img src="images/logo-square.svg" width=40 /> 速览

```{only} html
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.2561065.svg)](https://doi.org/10.5281/zenodo.2561065)
```

Jupyter Book 是一个开源项目，用于从计算材料中构建漂亮且具有出版质量的书籍和文档。

以下是 Jupyter Book 的一些特点：

:::{panels}
:container: +full-width text-center
:column: col-lg-6 px-2 py-2
:card:
:header: w3-light-blue
**[可发布内容](file-types:markdown)** ✍
^^^
使用 Jupyter Markdown, MyST Markdown，以及更多[发布功能](content/myst) 的 [reStructuredText](file-types:rst)，[Jupyter Notebooks](file-types:notebooks)，或 [任何 Jupytext 格式](file-types:custom)。

包括对富文本语法的支持，如[引用和交叉引用](content/citations)、[数学和等式](content/math)，以及[图](content/figures)。
---
:header: w3-light-gray
**[执行、缓存和插入可计算性内容](content/execute)** 🚀
^^^
执行笔记本单元格，然后[格式化并将最新输出插入](content:code-outputs)到您的书中。[缓存输出以节省稍后重建的时间](execute/cache)。甚至[保存笔记本输出并插入到其他页面](content:code-outputs:glue)。
---
:header: w3-pale-blue
**[向内容和输出添加交互性](interactive/launchbuttons)** ✨
^^^
创建交互式内容块，如 [](content:tabs)、[](content:dropdowns)。[切换单元格可见性](interactive/hiding)，并包含与 Jupyter 笔记本[交互的单元格输出](interactive/interactive)。使用 Binder 或 Colab [启动互动会话](interactive/launchbuttons)，[让你的代码在 Thebe 上可执行](launch:thebe)，或[与像 Hypothes.is 这样的评论服务连接](interactive:comments)。
---
:header: w3-pale-yellow
**[构建多种格式的书籍和文章](start/build)** 🎁
^^^
构建[多页的书籍](structure:book)或[单页文章](structure:article)，并从中生成多种输出，如 [HTML 网站](start/build) 或 [PDF 输出](advanced/pdf)。Jupyter Book 使用 [Sphinx 文档引擎](https://sphinx-doc.org)，支持[多种输出类型](https://www.sphinx-doc.org/en/master/usage/builders/index.html)。
:::

本文档分为几个主要部分。

- **教程**是 Jupyter Book 的一步步的介绍性指南。
- **主题指南**更深入地涵盖了特定领域，并被组织为离散的“如何”部分。
- **参考**章节详细描述了 Jupyter Book 的 API/语法 等细节。

这个网站就是 Jupyter Book 建立的！探索左边的章节来了解更多！

:::{admonition} 了解更多并参与其中
:class: tip full-width

💡 [打开议题](https://github.com/executablebooks/jupyter-book/issues/new/choose)
: 通过 GitHub issue 跟踪增强请求、bug 报告和待办事项。

💬 [加入讨论](https://github.com/executablebooks/meta/discussions)
: 在[社区论坛](https://github.com/executablebooks/meta/discussions)上进行社区讨论，讨论想法，分享一般性问题和反馈。

👍 [为新功能投票](ebp:feature-note)
: 社区通过在我们的存储库中添加👍对问题的反应来提供反馈。您可以在 [Executable Books 问题排行榜](ebp:feature-note) 中找到一个最重要的问题列表。

🙌 [对 Jupyter Book 有所贡献](contribute/intro.md)
: 通过遵循我们的贡献指南，找到需要解决的问题。查看 {ref}`功能投票排行榜 <ebp:feature-note>` 以获得灵感。

🙌 [加入社区](contribute/intro.md)
: Jupyter Book 是由[可执行书籍社区](https://executablebooks.org)开发的。我们欢迎任何人加入我们改进 Jupyter Book 并帮助彼此学习和创建他们的书。想要加入，请查看我们的[贡献指南](contribute/intro.md)。
:::

## 找到正确的文档资源

这里有一些建议可以帮助你开始。

:::{panels}
:container: +full-width
:column: col-lg-4 px-2 py-2
---
:header: bg-jb-one
**快速入门**
^^^

**[](start/your-first-book.md)**：一个循序渐进的入门教程。

**[](create-a-template-book)**：从一本简单的模板书开始。

---
:header: bg-jb-two

**了解更多**
^^^
**[](structure:index)**：学习如何结构化和组织内容。

**[](content/index.md)**：学习如何写丰富的叙事内容。

**[](content/executable/index.md)**：编写计算性内容。
---
:header: bg-jb-three

**灵感**
^^^
[**The Jupyter Book Gallery**](http://gallery.jupyterbook.org)：包含大量由 Jupyter Book 创建书籍的社区画廊。

[**The QuantEcon Python Lectures**](https://python.quantecon.org/intro.html)：一个由自定义 Jupyter Book 主题构建的完整的数学教科书。
:::

## 致谢

Jupyter Book 由一个[开放的贡献者社区](https://github.com/executablebooks/jupyter-book/graphs/contributors)支持，其中很多人来自[可执行书籍社区](https://executablebooks.org)和 [Jupyter 社区](https://jupyter.org/community)。

:::{image} https://pbs.twimg.com/profile_images/1226944724365447169/MzFpwY5P_400x400.png
:class: float-left mr-2 rounded
:width: 100px
:::

非常感谢 Sloan 基金会[为可执行图书项目提供支持](https://sloan.org/grant-detail/9231)。
