# MyST Markdown 概述

除了 [Jupyter Notebook Markdown](../file-types/notebooks.ipynb)，Jupyter Book 还支持 Markdown 的一种特殊样式，称为**MyST（或标记结构化文本）**。它旨在简化创建以 Markdown 标记编写的可发布计算文档的过程。它是 [CommonMark Markdown](https://commonmark.org/) 的超集，并从奇妙的 [RMarkdown language from RStudio](https://rmarkdown.rstudio.com/) 中汲取了很多灵感。

```{margin}
对于那些熟悉 Sphinx 的人来说，MyST Markdown 基本上是 CommonMark + Markdown 扩展 + Sphinx 的角色和指令
```

无论您是在 Jupyter 笔记本（`.ipynb`）中还是在常规 Markdown 文件（`.md`）中编写书籍的内容，都将使用**MyST Markdown**风格书写。Jupyter Book 将知道如何解析它们两者。

此页面包含有关 MyST Markdown 及其与 Jupyter Book 的关系的一些信息。您可以在 [Myst Parser 文档](myst-parser:example_syntax) 中找到有关 Markdown 风格的更多信息。

:::{admonition} 是否要直接使用 RMarkdown？
:class: tip
查阅 [](../file-types/jupytext.md)
:::


## 指令与角色

角色和指令是 Jupyter Book 中两个功能最强大的工具。它们有点像*函数*，但是是以标记语言编写的。指令（directive）与角色（role）的目标相似，但是**角色写在一行中**而**指令跨越很多行**。它们都接受不同种类的输入，它们对这些输入的处理方式取决于所使用的特定角色或指令。

(content:myst/directives)=
### 指令

指令可自定义书的外观，感觉和行为。它们有点像*函数*，并且以不同的方式出现各种名称。本节介绍如何构造和使用它们。

最简单的，您可以这样使用指令：

````md
```{指令}
这里是指令内容
```
````

仅在名称为 `指令` 的指令已经存在（不存在）的情况下才有效。有许多与 Jupyter Book 相关的预定义指令。例如，要插入注释框，可以使用以下指令：

````
```{note}
Here is a note
```
````

结果是：

```{note}
Here is a note
```

被插入到您的已建书中。


有关使用指令的更多信息，请参见 [MyST 文档](myst-parser:syntax/directives)。

(directive-arguments)=
#### 指令中的更多参数和元数据

许多指令允许您使用额外的信息来控制它们的行为。除了指令名称和指令内容外，指令还允许其他两个配置点：

**指令参数**：紧跟在 `{directivename}` 之后的单词列表。

这是指令参数的示例用法：

````md
```{directivename} arg1 arg2
My directive content.
```
````

**指令关键字**：位于 `{directivename}` 下方的标志或键/值对的集合。

有两种写指令关键字的方法，要么是 `:key: val` 对，要么是 `---` 括起来的 `key: val` 对。它们都以相同的方式工作：

以下是使用 `:key: val` 语法的指令关键字的示例：

````md
```{directivename}
:key1: metadata1
:key2: metadata2
My directive content.
```
````

以下是使用封闭式 `---` 语法的指令关键字的示例：

````md
```{directivename}
---
metadata1: metadata2
metadata3: metadata4
---
My directive content.
```
````

:::{tip}
记住，用 `:key:` 或 `---` 指定指令关键字没有什么区别。如果您要指定许多关键字，或者某些值跨越多行，建议您使用 `---`。使用 `:key: val` 语法作为一个或两个关键字的简写。
:::

有关如何使用它的示例，请参见以下各节。

(content:myst/roles)=
### 角色

角色与指令非常相似，但它们的复杂性和编写性较低

```md
Some content {rolename}`and here is my role's content!`
```

同样，仅当 `rolename` 是有效的角色名称时，角色才起作用。例如，`doc` 角色可用于引用书中的另一页。您可以通过相对路径直接引用另一个页面。例如，语法 `` {doc}`../README` `` 将产生 {doc}`../README`。

```{warning}
目前要求角色在您的源文件中位于“同一行”上。如果它跨越多行，将无法正确解析。可以跟踪 [此议题](https://github.com/executablebooks/MyST-Parser/issues/269) 跨多个角色的支持角色的进展情况。
```

有关使用角色的更多信息，请参阅 [MyST 文档](myst-parser:syntax/roles)。

## 有哪些角色和指令可用？

当前没有角色/指令的单个列表用作参考，但是本节尝试提供尽可能多的信息。对于那些熟悉 Sphinx 生态系统的人，**您可以使用 Sphinx 中可用的任何指令/角色**。这是因为 Jupyter Book 使用 Sphinx 来构建您的书，而 MyST Markdown 支持 Sphinx 支持的所有语法（将其视为 reStructuredText 的 Markdown 版本）。

:::{caution}
如果您在网（和下面的链接）上搜索有关角色和指令的信息，则通常在编写文档时会考虑到 reStructuredText。MyST Markdown 与 reStructuredText 不同，但是所有功能都应该相同。查阅 [MyST Sphinx 解析器文档](myst-parser:intro/get-started) 获取有关 MyST 和 rST 之间差异的更多信息。
:::

有关可供您使用的指令列表，请检查三个地方：

1. [Sphinx 指令页面](sphinx:usage/restructuredtext/directives) 包含一个指令列表，默认情况下在 Sphinx 中可用。
2. [reStructuredText 指令页面](https://docutils.sourceforge.io/docs/ref/rst/directives.html) 在 Python "docutils" 模块中具有指令列表。
3. 本文档还有一些特定于 Jupyter Book 的其他指令。

:::{admonition} 如果它存在于 rST 中但不存在于 MyST 怎么办？
:class: tip
在某些特殊情况下，MyST 可能与某个角色或指令不兼容。在这种情况下，可以使用特殊的 `eval-rst` 指令直接解析 reStructuredText：

````md
```{eval-rst}
.. note::

   A note written in reStructuredText.
```
````

产生

```{eval-rst}
.. note::

   A note written in reStructuredText.
```
:::

:::{seealso}
关于 [指令如何解析内容](myst-parser:syntax/directives/parsing) 的 MyST-Parser 文档，及其用于 [将 rST 文件包含到Markdown文件中](myst-parser:howto/include-rst) 的用法，以及 [在 Markdown 文件中使用 `sphinx.ext.autodoc`](myst-parser:howto/autodoc)。
:::

(markdown/nesting)=
## 在 Markdown 中嵌套内容块

如果您想在 Markdown 中将内容块彼此嵌套（例如，将 `{note}` 放在 `{margin}` 中），则可以通过添加额外的反引号（`` ` ``）到最外面的块。这也适用于文字代码块。

例如，以下语法：

`````md
````
```
```
````
`````

生成

````md
```
```
````

因此，如果您希望将指令彼此嵌套在一起，则可以采用相同的方法。例如，以下语法：

`````md
````{margin}
```{note}
Here's my note!
```
````
`````

生成：

````{margin}
```{note}
Here's my note!
```
````

## 其他 MyST Markdown 语法

除了角色和指令外，MyST Markdown 还支持许多其他类型的语法。MyST支持 CommonMark Markdown 的所有语法（Jupyter 笔记本使用的 Markdown 类型），以及用于科学出版的扩展语法。

[MyST-Parser](myst-parser:intro/get-started) 是 Jupyter Book 用来允许您在 MyST 中写书内容的工具。它也是有关 MyST 语法的良好信息来源。以下是一些可以用作参考的链接：

* [CommonMark 块语法](myst-parser:commonmark-block-tokens)
* [MyST 中的扩展 MyST 块语法](myst-parser:extended-block-tokens)
* [CommonMark 内联语法](myst-parser:commonmark-span-tokens)
* [MyST 中的扩展 MyST 内联语法](myst-parser:extended-span-tokens)

:::{seealso}
有关启用扩展 MyST 语法的信息，请参见 [](content-blocks:myst-extensions).
此外，请参阅本文档中有关此扩展语法的其他示例（以及如何启用每个扩展语法）。
:::

## 可以使用 MyST Markdown 创建什么？

请参阅 [](./content-blocks.md)，以获取在 Jupyter Book 中有关如何使用 MyST Markdown 进行操作的介绍。此外，该站点的其他页面还介绍了有关如何在 MyST 中使用指令的更多用例。

## 编写 MyST Markdown 的工具

整个社区的工具中都对 MyST Markdown 提供了一些支持。在这里，我们包括一些杰出的。

### Jupyter 接口

尽管 MyST Markdown 尚未在传统的 Jupyter 界面中呈现，但其大多数语法应“优美地降级”，这意味着您仍然可以在 Jupyter 中使用 MyST，然后使用 Jupyter Book 来构建您的书。

### Jupytext 和文本同步

要使用 Jupyter 笔记本和 Markdown 文件，建议使用 [jupytext](https://jupytext.readthedocs.io/en/latest)，这是一种用于在 `.ipynb` 和文本文件之间进行双向转换的开源工具。Jupytext [支持 MyST Markdown 格式](https://jupytext.readthedocs.io/en/latest/formats.html#myst-markdown).

:::{note}
为了与 `myst-parser` 完全兼容，必须使用 `jupytext>=1.6.0`。

也可参阅 [](file-types:custom:jupytext)。
:::

### VS Code

如果使用 VS Code 编辑 Markdown 文件，则 [VS Code MyST Markdown 扩展](https://marketplace.visualstudio.com/items?itemName=ExecutableBookProject.myst-highlight) 提供语法高亮显示和其他功能。
