(file-types:markdown)=
# Markdown 文件

可以使用普通的 Markdown 文件（例如，以 `.md` 结尾的文件）编写内容。Jupyter Book 支持任何被 Jupyter Notebook 支持的 Markdown 语法。Jupyter Notebook Markdown 是一种名为 [CommonMark Markdown](https://commonmark.org/) 的 Markdown 的扩展。虽然它缺少许多用于发布和文档化的特性，但它有许多用于标准文本处理的元素。

```{note}
如果你想要更深入的了解 CommonMark Markdown 概述和指南，请移步 [CommonMark Markdown 教程](https://commonmark.org/help/tutorial/)。
```

这一页描述了 Jupyter Notebook Markdown 的一些基本功能，以及如何将它们包含在你的书中。

```{margin}
Jupyter Book 还支持一个名为 **MyST Markdown** 的 Markdown 版本。这是 Jupyter Notebook Markdown 的延伸版本。它允许您包含引用和交叉引用，并控制更复杂的
向边距添加内容等功能。要了解更多信息，请查看 {doc}`../content/myst`。 
```

## 媒体嵌入

### 添加图片

您可以从您的 Markdown 文件引用外部媒体，如图像。如果你使用相对路径，当 Markdown 文件被复制时，它们将继续工作，只要它们指向存储库中的一个文件。

这是一个相对于书内容根目录的图像

![C-3PO_droid](../images/C-3PO_droid.png)

它是通过以下代码生成的：

```md
![C-3PO_droid](../images/C-3PO_droid.png)
```

:::{seealso}
[](../content/figures.md) 获取更多信息。
:::

### 添加影音

你甚至可以在网络上嵌入电影的引用！例如，这里有一个小 GIF 给你！

![giphy](https://media.giphy.com/media/yoJC2A59OCZHs1LXvW/giphy.gif)

当它被构建时，它将被包含在你的书中。

## 数学

对于 HTML 输出，Jupyter Book 使用了优秀的 [MathJax](http://docs.mathjax.org/en/latest/) 库，以及默认的 Jupyter Notebook 配置，用于从 latex 风格的语法呈现数学。

例如，这是一个用 MathJax 渲染的数学表达式：

$$
P(A_1 \cup A_2 \cup A_3)
& = P(B \cup A_3)  \\
& = P(B) + P(A_3) - P(BA_3) \\
&= P(A_1) + P(A_2) - P(A_1A_2) + P(A_3) - P(A_1A_3 \cup A_2A_3) \\
&= \sum_{i=1}^3 P(A_i) - \mathop{\sum \sum}_{1 \le i < j \le 3} P(A_iA_j) + P(A_1A_2A_3)
$$

:::{seealso}
[](../content/math.md) 获取更多信息。
:::

### 块级数学

可以通过将公式包装在 `$$` 字符中来包含块级数学。例如，下面的块：

```md
$$
wow = its^{math}
$$
```

输出的结果为：

$$
wow = its^{math}
$$

你也可以通过使用 LaTeX 风格的语法来包含数学块，使用 `\begin{align*}`。例如，下面的块：

```latex
\begin{align*}
yep = its_{more}^{math}
\end{align*}
```

结果是：

\begin{align*}
yep = its_{more}^{math}
\end{align*}

:::{important}
需要 [启用 `amsmath` MyST 扩展](math:latex)。
:::

## Markdown 的扩展 MyST Markdown

除了 CommonMark Markdown，Jupyter Book 还支持一个功能更齐全的 Markdown 版本，名为  **MyST Markdown**。这是 CommonMark 的一个超集，其中包括对发布计算性叙述有用的语法片段。更多信息关于 MyST Markdown，参阅 [](../content/myst.md)。
