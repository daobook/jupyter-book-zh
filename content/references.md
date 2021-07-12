---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(content:references)=
# 引用和交叉引用

因为 `jupyter-book` 是建立在 {term}`Sphinx` 之上的，有很多方法可以在你的书中引用内容(甚至跨其他书籍，或 Sphinx 网站)。

引用是通过**角色**或**markdown 链接语法**来完成的，这取决于你的用例。书中有几种引用内容的方法，这取决于你想要参考的内容类型。

:::{seealso}
如果你已经开始学习，请查看 [](../tutorials/references.md) 以获得更多信息。
:::

(content:references:labels)=
## 引用 section 标签

标签是一种将标签添加到内容部分的方法，以便以后可以引用它们。如果你想快速插入到书的其他部分的链接，这是很有用的。标签可以添加在页面的主要元素之前，如标题或 `figure`。

要添加一个标签，在你想要标记的元素前使用以下模式：

```md
(my-label)=
# The thing to label
```

例如，我们在本节的标题上面添加了以下标签：

```md
(content:references:labels)=
## Cross-references and labels
```

您可以使用两种语法在内容中插入对标签的交叉引用：

- `` {ref}`label-text` ``
- `[](label-text)`

例如，语法 `` {ref}`content:references:labels` `` 或 `[](content:references:labels)` 会产生到这个部分的链接，像这样 {ref}`content:references:labels`。

(references:figures)=
## 引用图像

要在你的书中引用一个图，首先添加一个图，并确保它有一个 `name` 和一个关联的字幕:

`````{panels}
源
^^^
````md
```{figure} ../images/cool.jpg
:name: my-fig-ref

My figure title.
```
````
---
结果
^^^
```{figure} ../images/cool.jpg
:name: my-fig-ref

My figure title.
```
`````

然后，通过其 `:name:` 值引用该图形。例如:

| source                                         | result                                   |
|------------------------------------------------|------------------------------------------|
| `` Here is {ref}`my-fig-ref` ``               | Here is {ref}`my-fig-ref`               |
| `` Here is {ref}`My cool fig <my-fig-ref>` `` | Here is {ref}`My cool fig <my-fig-ref>`              |
| `` Here is [](my-fig-ref) ``               | Here is [](my-fig-ref)               |
| `` Here is [My cool fig](my-fig-ref) `` | Here is [My cool fig](my-fig-ref)              |
| `` Here is {numref}`my-fig-ref` ``            | Here is {numref}`my-fig-ref`            |
| `` Here is {numref}`Custom Figure %s text ` `` | Here is {numref}`Custom Figure %s text <my-fig-ref>` |

(references:tables)=
## 引用表格

要引用一个表，首先创建一个表，并确保它有一个 `:name:` 和一个 title:

`````{panels}
source
^^^
````md
```{table} My table title
:name: my-table-ref

| header 1 | header 2 |
|---|---|
| 3 | 4 |
```
````
---
result
^^^
```{table} My table title
:name: my-table-ref

| header 1 | header 2 |
|---|---|
| 3 | 4 |
```
`````

以下是引用该内容的几种方法：

| source                                         | result                                   |
|------------------------------------------------|------------------------------------------|
| `` Here is {ref}`my-table-ref` ``               | Here is {ref}`my-table-ref`               |
| `` Here is {ref}`My cool table <my-table-ref>` `` | Here is {ref}`My cool table <my-table-ref>`              |
| `` Here is [](my-table-ref) ``               | Here is [](my-table-ref)               |
| `` Here is [My cool table](my-table-ref) `` | Here is [My cool table](my-table-ref)              |
| `` Here is {numref}`my-table-ref` ``            | Here is {numref}`my-table-ref`            |
| `` Here is {numref}`Custom Table %s text ` `` | Here is {numref}`Custom Table %s text <my-table-ref>` |


## 引用内容文件

要引用书籍内容的其他文件，可以使用 `{doc}` 角色，或者使用 Markdown 链接语法直接链接到另一个文件。例如:

| source                                         | result                                   |
|------------------------------------------------|------------------------------------------|
| `` Here is {doc}`../file-types/myst-notebooks` ``               | Here is {doc}`../file-types/myst-notebooks`               |
| `` Here is {doc}`A different page <../file-types/myst-notebooks>` `` | Here is {doc}`A different page <../file-types/myst-notebooks>`              |
| `` Here is [](../file-types/myst-notebooks.md) ``               | Here is [](../file-types/myst-notebooks.md)               |
| `` Here is [A different page](../file-types/myst-notebooks.md) `` | Here is [A different page](../file-types/myst-notebooks.md)              |

## 引用公式

要引用公式，首先插入一个带有如下标签的公式：

```{math}
:label: my-math-ref
w_{t+1} = (1 + r_{t+1}) s(w_t) + y_{t+1}
```

要引用公式，请使用 `{eq}` 角色。它会自动插入等式的个数。注意，您不能修改等式链接的文本。

例如：

- `` See Equation `{eq}`my-math-ref` `` 结果:见公式 {eq}`my-math-ref`
- `` See Equation [](my-math-ref) `` 结果:见公式 [](my-math-ref).


(references:custom-text)=
## 选择引用文本

如果你想选择渲染引用链接的文本，使用以下模式：

```md
{someref}`your text here <reference-target>`
```

在上面，`reference-target` 是您所引用的目标，`your text here` 是页面上显示的文本。

例如，引用如下:

```{list-table}
:header-rows: 1

* - Raw text
  - Rendered text
* - ``{ref}`Here's another references section <content:references:labels>` ``
  - {ref}`Here's another references section <content:references:labels>`
* - ``{doc}`Here's the code outputs section <code-outputs>` ``
  - {doc}`Here's the code outputs section <code-outputs>`
```


## 引用编号

您可以在表格或图表中添加**编号引用**。要向 [表](references:tables)或 [图形](references:figures) 添加编号引用，请使用 `{numref}` 角色。如果您希望使用 [自定义文本](references:custom-text)，请添加 `%s` 作为数字的占位符。

有关用法，请参阅下面一节中的示例。

(references:markdown-syntax)=
## 使用 markdown 链接语法的引用

如果你想使用 Markdown 风格的语法，那么 MyST Markdown 将尝试从以上引用类型中找到一个引用(以及更多!)

这有一个优点，你可以在你的文本中使用嵌套的标记语法，例如：

```{list-table}
:header-rows: 1

- * Raw text
  * Rendered text
- * ```md
    [A **bolded _reference_** to a page](./myst.md)

    [A reference to a header](content:references:labels)
    ```
  * [A **bolded _reference_** to a page](./myst.md)

    [A reference to a header](content:references:labels)
```

将标题保留为空意味着引用将目标作为文本，例如语法

```md
[](./myst.md)
```

将链接到一个节，并使用它的标题文本作为链接文本本身：

[](./myst.md)

:::{admonition} 内部和外部 URLs
:class: tip
你可以在 `_config.yml` 中控制 MyST Markdown 如何区分内部引用和外部 URLs。例如，

```yaml
parse:
   myst_url_schemes: [mailto, http, https]
```

意味着 `[Jupyter Book](https://jupyterbook.org)` 将被识别为一个 URL，但 `[Citations](content:citations)`  将不会：

* [Jupyter Book](https://jupyterbook.org)
* [Citations](content:citations)

:::

## 检查遗漏的引用

你可以在构建 Jupyter  Book 时检查丢失的参考。要做到这一点，可以使用以下选项:

```bash
jupyter-book build -W -n --keep-going docs/
```

这将检查丢失的引用(`-n`)并将它们转换为错误(`-W`)，但仍将尝试运行完整的构建(`--keep-going`)，以便您可以在一次运行中看到所有错误。
