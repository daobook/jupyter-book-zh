(file-types:rst)=
# reStructuredText 文件

除了在 Markdown 中编写内容外，Jupyter Book 还支持用 [reStructuredText](https://docutils.sourceforge.io/rst.html)（Python 文档社区中常见的另一种标记语言）编写内容。

:::{warning}
只建议已经熟悉 reStructuredText 的用户使用它来编写内容。对于其他人，我们推荐使用 [MyST Markdown](../content/myst.md)，它具有 rST 和 Sphinx 的所有相同功能，但带有 Markdown 的味道。
:::

因为 Jupyter Book 在底层使用了 Sphinx，所以任何用 rST 为 Sphinx 生态系统编写的文档也应该在 Jupyter Book 中生效。如果您已经有了大量用 rST 编写的文档，并且您想在 Jupyter Book 中试用它，那么这是特别有用的。

关于使用 reStructuredText 编写内容的更多信息，我们建议阅读 [Sphinx rST文档](https://www.sphinx-doc.org/es/stable/rest.html)。

## 包括 reStructuredText 在 Markdown

要插入 rST 到 Markdown，你可以使用 [eval-rst 指令](myst-parser:syntax/directives/parsing)：

````md
```{eval-rst}
.. note::

   用 reStructuredText 写的注释。

.. include:: ./include-rst.rst
```
````

```{eval-rst}
.. note::

   用 reStructuredText 写的注释。

.. include:: ./include-rst.rst
```
