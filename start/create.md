# 创建书籍的源文件

现在，我们了解了书的结构，让我们创建一个样本书来学习。

## 快速生成样本书

Jupyter Book 随附了一个轻量级的示例书，可帮助您了解书的结构。通过运行以下命令来创建样本书：

```
jupyter-book create mynewbook/
```

这将生成一个迷你的 Jupyter Book，您可以在本地进行构建和浏览。它将为您做出一些决定，您可以在 `_config.yml` 中探索本书的配置，并在 `_toc.yml` 中探索书的结构。将此书用作灵感或作为工作的起点。

## 研究书的内容文件

首先，请注意至少有两种不同的内容文件：**markdown** 文件（以 `.md` 结尾）和 **Jupyter Notebooks**（以 `.ipynb` 结尾）。

我们将在下面进行讨论。

### Markdown 文件（`.md`）

Markdown 是一种 [markup language](https://en.wikipedia.org/wiki/Markup_language) 的示例-一种用额外的字符和语法构造文本的方法，该字符和语法赋予其额外的含义（例如，使用`**bold**`表示 **粗体**。
它非常流行，并在许多不同的技术平台上使用。

Markdown文件略有变化，通常称为*markdown的风格*。
Jupyter Book 支持两种 Markdown 样式：

- [CommonMark markdown](https://commonmark.org/)：标准 markdown，这是很常见的。
- [MyST Markdown](../content/myst.md)：CommonMark 的扩展，具有用于富文档的附加功能。

让我们看一下模板书中的 markdown 文件之一：`intro.md`：

````md
# Welcome to your Jupyter Book

This is a small sample book to give you a feel for how book content is
structured.

:::{note}
Here is a note!
:::

And here is a code block:

```
e = mc^2
```

Check out the content pages bundled with this sample book to see more.
````

在上方，您看到几种不同的结构：

- `#` 符号表示 CommonMark 标记中的“节标题”。

  例如，它们定义了此页面上的节标题。
- `:::{note}` 是 MyST Markdown 中的“指令”（**directive**）。
  它的呈现样式如下：

  :::{note}
  I'm a note!
  :::
- ` ``` ` 表示CommonMark标记中的“代码块”。
  它的呈现方式如下：

  ```
  e=mc^2
  ```

所有内容文件必须有一个页面标题(指定为第一个标题)。所有随后的标题必须线性增加(所以没有从 H1 跳转到 H3)。请参见 [](rules-all-content-types) 了解所有内容必须遵守的更多规则。

想了解更多关于 MyST markdown 的信息以及你可以用它做的所有事情，请查看 [](../content/myst.md)。

### Jupyter Notebooks (`.ipynb`)

我们要注意的另一种类型是一个以 `.ipynb` 结尾的 **Jupyter Notebook** 的内容。
Jupyter Notebook 集计算内容和叙述内容于一体。
每个笔记本都与一个 **kernel** (又名 Python、R、Julia 等)相关联，该内核定义了用于执行笔记本计算内容的语言。

默认情况下，当 Jupyter Book 构建你的书，**笔记本将被执行，其输出缓存**。在后续构建中，只有当代码发生更改时，笔记本页面才会重新执行。

:::{margin} ✨带有文本文件的笔记本✨
您还可以将 Jupyter 笔记本存储为 markdown 文件或其他文本文件。查看 [](../file-types/myst-notebooks.md) 和 [](../file-types/jupytext.Rmd)。
:::

任何由笔记本产生的输出都会被插入到你的内置笔记本中(尽管它们可能不在你的输入笔记本中)。通过这种方式，您不需要将笔记本的输出存储在存储库中。更多信息请参见 [](../content/execute.md)。

还有许多其他有趣的事情你可以做的笔记本内容作为你的书的一部分。我们建议查看 [](../content/code-outputs.md) 以及 [](../interactive/interactive.md) 来开始使用 Jupyter notebook。

## 检查配置文件

除了这些内容文件之外，您的书还有一个**配置文件** (`_config.yml`))。
这在很多方面控制了你的书的行为。

我为你做了几个决定。
让我们来看几个例子:

这段代码配置了一些关于你的书的元数据，并确定了左上角显示的 logo：

```yaml
# Book settings
# Learn more at https://jupyterbook.org/customize/config.html

title: My sample book
author: The Jupyter Book Community
logo: logo.png
```

这个配置激活了您的书的**citations**(参见 [](../tutorials/references.md) 开始引文和参考)。

```yaml
# Add a bibtex file so that we can create citations
bibtex_bibfiles:
  - references.bib
```

这个配置告诉 Jupyter Book **每次**这本书被重新构建时执行你所有的 Jupyter 笔记本文件，而不是缓存它们。

```yaml
# Force re-execution of notebooks on each build.
# See https://jupyterbook.org/content/execute.html
execute:
  execute_notebooks: force
```

查看配置文件中的其他内容，并将其引用到本文档中的页面中，以了解它的功能。

## 你的书的目录

最后，你的书也有一个**目录**告诉 Jupyter Book 你的每个内容源文件应该去哪里。

```yaml
- file: intro
- file: markdown
- file: notebooks
```

这是一个简单的目录，由三页组成。
TOC 的第一项总是你的书的登陆页：人们在看你的书时看到的第一页。

后续页面按顺序定义。
除了定义一个页面列表之外，你还可以做很多事情——请参阅 [](../customize/toc.md) 来了解更多关于结构化你的书的信息。

## 创建自己的内容文件

现在您已经看到了一些示例内容文件，请尝试创建您自己的内容文件!

在包含所有示例书内容的文件夹中，创建一个名为 `mymarkdownfile.md` 的新文件。填入以下内容:

```md
# Here's my sample title

This is some sample text.

(section-label)=
## Here's my first section

Here is a [reference to the intro](intro.md). Here is a reference to [](section-label).
```

我们添加了两个新的标记语法，它们都与**交叉引用**相关。

- `(section-label)=` 是附加到节标题的标签。它指的是后面的任何标题，并允许您稍后在您的文本中引用这个标签。
- `[link text](link-target)` 语法是你在 markdown 中指定链接的方式。这里我们已经链接到另一个页面，以及我们上面创建的标签。

在构建图书时，您将在输出中看到这些链接是如何解析的。

## 下一步：构建你的书

现在您已经有了一个 Jupyter Book 文件夹结构，您可以为图书的每个页面创建 HTML(或 PDF)。这将在下一节中讨论。
