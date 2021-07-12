---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(file-types:myst-notebooks)=
# 完全用 Markdown 书写笔记本

在 Markdown 中存储 Jupyter 笔记本是可能的。这允许你完全使用 MyST Markdown 定义一个笔记本结构。关于 MyST Markdown 的更多信息，请参见 {doc}`../content/myst`。

使用 Markdown 的笔记本可以在 Jupyter Book 中读取、执行和缓存(参见 {doc}`../content/execute` 来获取关于如何缓存页面的信息)。
这允许你以文本格式存储你所有的笔记本内容，这对于版本控制软件来说是更好的，同时仍然拥有一个 Jupyter 笔记本的所有功能。

:::{note}
MyST 笔记本使用 [MyST-NB to convert between ipynb and text files][myst-nb:index]。
有关更多信息，请参阅文档。
:::

要查看 MyST 笔记本的示例，您可以查看[本文档的许多页面](https://github.com/executablebooks/jupyter-book/tree/master/docs)。
例如，查看 {download}`../interactive/hiding.md` 和 {download}`../content/layout.md`。

## 用 Jupytext 创建一个 MyST 笔记本

创建 MyST 笔记本最简单的方法是使用 [Jupytext](https://jupytext.readthedocs.io)，这是一个允许双向转换 `.ipynb` 和各种文本文件的工具。

你可以用下面的命令将 `.ipynb` 文件转换为 MyST 笔记本：

```bash
jupytext mynotebook.ipynb --to myst
```

`mynotebook.md` 文件的结果将被创建。
这可以作为你书中的一页。

:::{important}
为了与 `myst-parser` 完全兼容，必须使用 `jupytext>=1.6.0`。
:::

Jupytext 也可以**与您的 Markdown 自动同步 `.ipynb` 文件**。
要做到这一点，请使用 Jupyter 接口，如 Jupyter Lab 或经典的笔记本接口，并遵循[配对笔记本的 Jupytext 说明](https://jupytext.readthedocs.io/en/latest/paired-notebooks.html)。

```{margin} Markdown 优先
如果 `.ipynb` 和 `.md` 文件都存在于你的书的文件夹中，则 `.md` 文件将优先使用！
```

### 将 Markdown 文件转换为 MyST Markdown

Jupyter Book 有一个小的 CLI，为操作和创建与 Jupytext 同步的 MyST Markdown 文件提供通用功能。将 Jupytext 语法添加到 Markdown 文件中(这将告诉 Jupytext 它是一个 MyST Markdown 文件)，运行以下命令:

```bash
jupyter-book myst init mymarkdownfile.md --kernel kernelname
```

如果您没有指定 `--kernel`，那么如果只有一个可用的*默认的内核* 将被使用。如果有多个可用内核，则必须手动指定一个。


## MyST 笔记本的结构

让我们看一下 Jupytext 创建的结构，您也可以使用它从头创建 MyST 笔记本。首先，让我们看看一个简单的 MyST 笔记本:

````md
---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# My simple notebook

Some **intro Markdown**!

```{code-cell} ipython3
:tags: [mytag]

print("A python cell")
```

## A section

And some more Markdown...
````

这里有三个主要部分需要注意：

### Frontmatter YAML

MyST 笔记本需要特殊的前端格式的 YAML 来告诉 Jupytext 他们可以被转换成 `.ipynb` 文件。frontmatter YAML 块：

```yaml
---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
```

告诉 Jupytext 此文件是 `myst` 格式的，并且它的代码应该在 Python 3 内核下运行。

```{margin}
记住，Jupyter 总是为每个笔记本定义一个而且只有一个内核。
```

### 代码单元格

MyST 笔记本中的代码块是用下面的 MyST 指令定义的：

````md
```{code-cell}
your-code
```
````

您可以选择向代码单元添加额外的元数据，这些元数据将转换在 `.ipynb` 文件中。例如，你可以像这样在代码单元格中添加标签：

````md
```{code-cell}
:tags: [tag1, tag2, tag3]
your-code
```
````

您也可以显式地在 `{code-cell}` 之后传递内核名称，以明确您正在运行的内核。例如：

````md
```{code-cell} python3
your-code
```
````

但是，请记住，每个页面只允许一个内核。

### Markdown 内容

代码单元之间的所有内容都使用[MyST Markdown 解析器](https://myst-parser.readthedocs.io/) 解析为 Markdown 内容。查阅 {doc}`../content/myst` 获取 MyST Markdown 的更多信息。

要明确地将 Markdown 内容拆分为两个 Markdown 单元格，请使用以下模式：

```md
Content in one Markdown cell

+++

Content in another Markdown cell
```

您也可以通过在 `+++` 后面添加 Python 字典来将元数据附加到单元格。
例如，要向上面的第二个单元格添加标记:

```md
Content in one Markdown cell

+++ {"tags": ["tag1", "tag2", "tag3"]}

Content in another Markdown cell
```

```{warning}
请注意，在 MyST 文件中通过 `+++` 语法指定的单元格中断和元数据只会传播到它们的 `.ipynb`。在生成书的 HTML 时，*Markdown单元格* 信息将被丢弃，以避免文档结构中的层次结构冲突。换句话说，只有 *code cell* 标签对生成的 HTML 有影响。
```
