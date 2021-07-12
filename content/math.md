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

(myst-content/math)=
# 数学和公式

Jupyter Book使用 [MathJax](http://docs.mathjax.org/) 在 HTML 图书版本中排版数学。这使您可以在在线内容中使用 LaTeX 风格的数学。此页面显示了几种控制方法。

:::{seealso}
有关公式编号的更多信息，请参见 [MathJax 公式编号文档](http://docs.mathjax.org/en/v2.7-latest/tex.html#automatic-equation-numbering)。
:::

:::{tip}

默认情况下，当前使用 MathJax 版本 2。如果您使用大量数学运算，则可能要尝试使用版本 3，该版本声称可将加载速度提高 $60-80\%$：

```yaml
sphinx:
  config:
    mathjax_path: https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js
```

细节见 [Sphinx documentation](sphinx:sphinx.ext.mathjax)。

:::

## 行内数学

要插入行内数学，请在 Markdown 单元格内使用 `$` 符号。例如，文本 `$this_{is}^{inline}$` 将产生：$this_{is}^{inline}$。

+++

## 数学块

您还可以为单独的公式包括数学块。这使您可以将注意力集中在更复杂或更长时间的公式上，以及在页面中链接到它们。要使用块公式，请将公式包装在 `$$` 或 `\begin` 语句中。

例如，

```latex
$$
  \int_0^\infty \frac{x^3}{e^x-1}\,dx = \frac{\pi^4}{15}
$$
```

结果是：

$$
  \int_0^\infty \frac{x^3}{e^x-1}\,dx = \frac{\pi^4}{15}
$$

+++

(math:latex)=
### Latex 风格的数学

您可以使用 `amsmath` MyST 扩展启用解析 LaTeX 样式的数学块。通过将以下内容添加到 `_config.yml` 中来启用它

```yaml
parse:
  myst_enable_extensions:
    # don't forget to list any other extensions you want enabled,
    # including those that are enabled by default!
    - amsmath
```

启用后，您可以定义数学块，如下所示：

```latex
\begin{gather*}
a_1=b_1+c_1\\
a_2=b_2+c_2-d_2+e_2
\end{gather*}

\begin{align}
a_{11}& =b_{11}&
  a_{12}& =b_{12}\\
a_{21}& =b_{21}&
  a_{22}& =b_{22}+c_{22}
\end{align}
```

结果是：

\begin{gather*}
a_1=b_1+c_1\\
a_2=b_2+c_2-d_2+e_2
\end{gather*}

\begin{align}
a_{11}& =b_{11}&
  a_{12}& =b_{12}\\
a_{21}& =b_{21}&
  a_{22}& =b_{22}+c_{22}
\end{align}

:::{seealso}
MyST 教程有 [dollar 数学语法](myst-parser:syntax/math)，[LaTeX 数学语法](myst-parser:syntax/amsmath) 和 [MyST-Parser 如何与 MathJax 一起使用](myst-parser:syntax/mathjax)。

对于高级用法，还请参见如何 [定义 MathJax TeX 宏](sphinx/tex-macros)。
:::

+++

### 公式编号

如果您希望对公式进行编号，以便以后可以引用它们，请使用 **math 指令**。看起来像这样：

````md
```{math}
:label: my_label
my_math
```
````

例如，以下代码：

````md
```{math}
:label: my_label
w_{t+1} = (1 + r_{t+1}) s(w_t) + y_{t+1}
```
````

会产生

```{math}
:label: my_label
w_{t+1} = (1 + r_{t+1}) s(w_t) + y_{t+1}
```

或者，您可以使用带有前缀标签的美元数学语法：

```md
$$
  w_{t+1} = (1 + r_{t+1}) s(w_t) + y_{t+1}
$$ (my_other_label)
```

会产生

$$
  w_{t+1} = (1 + r_{t+1}) s(w_t) + y_{t+1}
$$ (my_other_label)

:::{note}
标签不能以整数开头，否则将无法被引用，如果被引用，则会引发警告消息。例如，不能引用 `:label: 1` 和 `:label: 1eq`。
:::

### 链接到公式

如果您创建了带有标签的公式，则可以从文本内（以及跨页面！）链接到该公式。

您可以使用通过 `{eq}` 角色提供的标签来引用公式。例如：

```md
- A link to an equation directive: {eq}`my_label`
- A link to a dollar math block: {eq}`my_other_label`
```

结果是

- A link to an equation directive: {eq}`my_label`
- A link to a dollar math block: {eq}`my_other_label`

:::{note}
LaTeX 环境中的 `\labels` 目前尚未识别，因此无法引用。我们希望在以后的更新中实现这一点(见 [executablebooks/MyST-Parser#202](https://github.com/executablebooks/MyST-Parser/issues/202))！
:::
