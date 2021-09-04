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

# 概述

本节简要概述了构建 Jupyter Book 的主要组件和步骤。有关更深入的信息，请参阅本指南的其他页面。

(start:install)=
## 安装 Jupyter Book

可以使用 [`pip`](https://pip.pypa.io/en/stable/) 安装 Jupyter Book：

```bash
pip install -U jupyter-book
```

在本地构建 Jupyter Book 所需的一切将被安装。

## Jupyter Book 的命令行界面

Jupyter Book 使用命令行界面来执行各种操作。例如，建造和清洁书籍。您可以运行以下命令查看哪些选项在您的控制下：

```{margin}
你可以简写 `jupyter-book` 为 `jb`。例如：
`jb create mybookname`。剩下的教程我们均使用 `jupyter-book`。
```

% 重复写这个，这样用户不会被混淆，但我们仍然得到输出
```bash
jupyter-book --help
```

```{code-cell}
:tags: [remove-input]

!jupyter-book --help
```

有关 CLI 的更完整信息，请参见 [](../reference/cli.md)。

## 书籍构建过程

构建一本 Jupyter Book 大致包括以下步骤：

1. **创建你的书的内容**。您可以用文件夹、文件和配置的集合来构造您的书。 参见 [](anatomy-of-a-book)。
2. **构建你的书**。使用 Jupyter Book 的命令行界面，您可以将页面转换为 HTML 或 PDF 图书。参见 [](build.md)。
3. **在网上发布你的书**。一旦你的书建好了，你就可以和别人分享了。最常见的是构建 HTML，并将其作为公共网站托管。参见 [](publish.md)。

:::{note}
我们将使用“book”这个词来描述本教程生成的输出，但是您也可以使用 Jupyter Book 来构建**文章**。阅读 [](structure:article) 了解更多信息。
:::

(anatomy-of-a-book)=
## Jupyter Book 的解剖

你需要做三件事来制作一本 Jupyter Book：

- 配置文件：`_config.yml`
- 目录文件：`_toc.yml`
- 你的书的内容

例如，考虑下面的文件夹结构，它组成了一个简单的 Jupyter Book。

```
mybookname/
├── _config.yml
├── _toc.yml
├── landing-page.md
└── page1.ipynb
```

我们将在下面简要介绍它们，您可以在本文档的其他地方找到关于它们的更多信息。

### Book 的配置（`_config.yml`）

您的书的所有配置都在一个名为 `_config.yml` 的 YAML 文件中。

您可以为您的图书定义元数据(比如它的标题)，添加图书标识，打开不同的“交互式”按钮(比如一个 {term}`Binder` 按钮，用于从 Jupyter Book 构建的页面)，等等。

```{margin}
有关本书配置文件的更多信息，请参见 [](../customize/config.md)。
```

下面是一个简单的 `_config.yml` 示例文件：

```yaml
# in _config.yml
title: "My book title"
logo: images/logo.png
execute:
  execute_notebooks: "off"
```

- `title`：定义书的标题。它将会被展示在左侧的侧边栏。
- `logo`：定义图书标识的图像文件的路径(它也会显示在侧边栏中)。
- `execute`：包含控制 [执行和缓存](https://jupyterbook.org/content/execute.html) 的配置选项集合。
  - `execute_notebooks: "off"`  告诉 Jupyter Book 不要执行任何它在构建书时发现的计算内容。默认情况下，Jupyter Book 会执行并缓存所有的图书内容。

:::{admonition} 更多关于 `_config.yml`
:class: tip
你可以用 `_config.yml` 文件做更多的事情。例如，您可以 [](source-repository-button) 或添加 [](../interactive/interactive.ipynb)。获取 `_config.yml` 的完整字段列表，请参见 [](../customize/config.md)。
:::

#### Book 的目录（`_toc.yml`）

Jupyter Book 使用你的目录来定义你的书的结构。例如，你的章节，分章节等等。

这是一个包含一组页面的 YAML 文件，每个页面都链接到书中的一个文件。下面是上面显示的两个内容文件的示例。

````{margin}
如果您想快速**生成一个基本的目录** YAML 文件，执行如下命令:

```bash
jupyter-book toc mybookname/
```

它会为你生成一个 TOC。注意，为了解析任何子文件夹，每个文件夹中必须至少有一个内容文件。
````

```yaml
# In _toc.yml
- file: landing-page
- file: page1
```

`_toc.yml` 中的每一项都指向单个文件。链接应该是相对于你的书的文件夹，没有扩展名。你可以将 TOC 文件的最顶层想象成书籍的章节(不包括登录页)。每一章的标题将从你文件的标题中推断出来。

第一个文件指定图书的登录页(在本例中，它是一个 markdown 文件)。登录页（landing page）是书籍内容层次结构中最高的页面。第二个文件指定图书的内容页(在本例中，它是一个 Jupyter Notebook)。

```{margin}
有关书的目录文件的更多信息，请参见 [](toc/structure).
```

:::{admonition} 更多关于 `_toc.yml`
:class: tip
您可以使用 `_toc.yml` 指定更复杂的图书配置。例如，您可以指定 **parts**、**sections** 和控制 **custom titles**。关于书的目录文件的更多信息，请参见 [](../customize/toc.md)。
:::

### 书籍内容

一组文本文件构成了你的书的内容。这些文件可以是几种类型中的一种，例如 markdown (`.md`)、Jupyter notebook (`.ipynb`)或 reStructuredText (`.rst`)文件(请参阅 [](../file-types/index.md) 以获得完整列表)。

在上面的例子中，列出了两个文件：一个 markdown 文件和一个 Jupyter Notebook。我们将在下一节中介绍它们。
