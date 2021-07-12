(content:citations)=
# 引用和参考书目

您可以使用存储在图书文件夹中的 `bibtex` 文件中的引用来添加引用和参考书目。然后，您可以使用 `{cite}` 角色在 Markdown 中添加一个引用，并使用 `{bibliography}` 指令包含 bibtex 文件中的书目。

```{seealso}
这个功能使用了优秀的 [sphinxcontrib-bibtex](https://sphinxcontrib-bibtex.readthedocs.io/en/latest/) 扩展。
```

## 基础引用

从 Jupyter Book 中的引用开始，请查阅 [](tutorials:references).

## 更改内联引用样式

您可以使用一些替代角色来更改内联引用样式。下面是一些例子：

- 引文 `` {cite:p}`perez2011python` `` 结果是 {cite:p}`perez2011python`
- 引文 `` {cite:t}`perez2011python` `` 结果是 {cite:t}`perez2011python`
- 引文 `` {cite:ps}`perez2011python` `` 结果是 {cite:ps}`perez2011python`
- 引文 `` {cite:ts}`perez2011python` `` 结果是 {cite:ts}`perez2011python`

:::{seealso}
要获得更完整的内联引用样式列表，请查看 [`sphinxcontrib-bibtex` 文档](https://sphinxcontrib-bibtex.readthedocs.io/en/latest/usage.html#roles-and-directives)。
:::

## 选择你的参考书目样式

您还可以自定义引用的样式。默认情况下，引用以 `alpha` 样式显示。其他当前支持的样式包括 `plain`、`unsrt` 和 `unsrtalpha`。这些样式创建以下书目格式：

* `alpha`: 使用字母数字（alphanumeric）的引用标签，引用按作者、年份排序。
* `plain`: 使用数字（numeric）参考标签，引文按作者、年份排序。
* `unsrt`: 使用数字参考标签，引文按外观顺序排序。
* `unsrtalpha`: 使用字母数字（alphanumeric）引用标签，引用按外观顺序排序。

要设置你的参考样式，使用`style`选项：

````md
```{bibliography}
:style: unsrt
```
````

## 更改引用样式

有几个选项可以作为内联引用的格式。要选择一个，请使用 `_config.yml` 中的以下配置。

```yaml
# In _config.yml
# In _config.yml
sphinx:
  config:
    bibtex_reference_style: author_year # label, super, and author-year.
```

:::{seealso}
有关配置选项列表和更多细节，请参阅 [`sphinxcontrib-bibtex` 文档](https://sphinxcontrib-bibtex.readthedocs.io/en/latest/usage.html#referencing-style)
:::

## 局部参考书目

您可能希望在每个文档的末尾包含一个参考书目列表，而不是在单独的文档中包含一个单独的参考书目。然而，拥有多个书目指令可能会导致 `sphinx` 发出 `duplicate citation warnings`。

一个常见的修复方法是在 bibliography 指令中添加一个 `filter`：

````md
```{bibliography}
:filter: docname in docnames
```
````

参见 [局部参考书目](https://sphinxcontrib-bibtex.readthedocs.io/en/latest/usage.html#section-local-bibliographies) 中的 `sphinxcontrib-bibtex` 文档。

(citations/bibliography)=
## 参考书目示例

参考书目示例：

```{bibliography}
```
