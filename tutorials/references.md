(tutorials:references)=
# 开始使用引用

引用（references）使您可以引用书中的其他内容或外部内容。它们使您可以自动生成指向该内容的链接，或向引用添加诸如*数字*之类的额外信息。

引文（Citations）和参考书目（bibliographies）允许您引用学术著作，并提供参考书目，以使读者可以阅读参考文献。

本教程介绍了为您的书设置 **references** 以及 **citations and bibliographies** 的基础。

:::{seealso}
有关引用和参考语法的更多信息，请参见 [`sphinxcontrib-bibtex` 文档](https://sphinxcontrib-bibtex.readthedocs.io/en/latest/usage.html#roles-and-directives)。
请注意，本文档在编写时就考虑了 rST 语法，您需要针对 Markdown 内容调整 指令/角色 语法。
:::

## 先决条件

本教程假定您已经从 [](../start/your-first-book.md) 创建了一个演示 Jupyter Book，或者您可以使用自己的 Jupyter Book。

## references 的基本结构

Jupyter Book 中的交叉引用通常涉及两件事：

1. 为某事创建一个 **label**。这是您将在后面的 reference 中引用的东西。
2. 使用 **target** 创建 reference。这个 target 通常是您在 `#1` 中创建的 label。

## 创建 label

首先，我们将创建一个 label。
label 必须位于标题之前。
然后，您可以在文本中的其他地方引用它们。

首先，在您的书中创建一个新的 markdown 文件（或编辑一个预先存在的文件）。
添加带有标签的 markdown 标头，如下所示：

```md
(my-label)=
## My header

Some text
```

这就是您指定label `my-label` 的方式，该 label 指向下面的标头（`## My header`）。

:::{margin}
您还可以使用以下语法以这种方式引用 label：

```
Some text and {ref}`my-label`
```
:::

## 引用你的 label

现在，您已经创建了 label，您可以从其他地方引用它。
尝试在同一页面（或其他页面）上添加以下 markdown。

```md
Here's some text and [here's my label](my-label).
```

现在，重新构建书籍的 HTML：

```bash
jb build pathto/mybook
```

您应该看到您的参考文献已替换为指向页面上正确位置的链接。

## 创建 citation

接下来，我们将添加一个 *citation*.

### 创建一个 bibtex 文件

您需要一个 [bibtex](http://www.bibtex.org/) 文件来存储 citation 的信息。
在这种情况下，我们将创建一个空的 bibtex 文件，并使用一个引用填充该文件。

```bash
touch references.bib
```

接下来，将您的书配置为包含此 bibtex 文件，如下所示：

```yaml
# In _config.yml
bibtex_bibfiles:
    - references.bib
```

这将激活 [`sphinxcontrib.bibtex` 扩展](https://sphinxcontrib-bibtex.readthedocs.io/en/latest/)

最后，注意默认的引用样式是 `label`，它在呈现的 HTML 中显示为 [ABC21] 的内联链接；[这里将详细描述](https://sphinxcontrib-bibtex.readthedocs.io/en/latest/usage.html#referencing-style)它和其他样式。您可以在书的 `_config.yml` 中调整引用样式：

```yaml
# In _config.yml
sphinx:
  config:
    bibtex_reference_style: author_year
```

### 添加你的 references

向您的 BibTex 文件添加一些引用。这是一个示例引用：

```latex
@article{perez2011python
,	title	= {Python: an ecosystem for scientific computing}
,	author	= {Perez, Fernando and Granger, Brian E and Hunter, John D}
,	journal	= {Computing in Science \\& Engineering}
,	volume	= {13}
,	number	= {2}
,	pages	= {13--21}
,	year	= {2011}
,	publisher	= {AIP Publishing}
}
```

:::{seealso}
有关 BibTex 参考样式的信息，请参见 [BibTex 文档](http://www.bibtex.org/Using/)。
:::

### 添加一个 citation

在您的内容中，添加以下语法以包括引用：

```md
Here is my nifty citation {cite}`perez2011python`.
```

重新构建您的书，它应该看起来像这样：

Here is my nifty citation {cite}`perez2011python`.

### 一次添加多个引用

现在尝试通过用逗号分隔每个引文来一次添加多个引文。

将以下文本添加到您的页面：

```md
Here are multiple citations {cite}`perez2011python,holdgraf_rapid_2016,RePEc:the:publsh:1367,caporaso2010qiime`!
```

重新构建您的书，它应该看起来像这样：

Here are multiple citations {cite}`perez2011python,holdgraf_rapid_2016,RePEc:the:publsh:1367,caporaso2010qiime`!

## 添加一个 bibliography

最后，我们将为引文生成一个 bibliography。
当您引用某些内容时，将自动创建此参考书目的链接。

我们将使用 `{bibliography}` 指令将一本书添加到我们的书中。
将以下内容添加到您的页面：

````md
```{bibliography}
```
````

这将生成书中所有引用的 bibliography。
有关示例，请参见下面的 bibliography。

:::{seealso}
有关配置和使用引文和参考书目的更多信息，请参见 [](content:references).
:::

## Bibliography

bibliography 示例，供参考：

```{footbibliography}
```
