---
substitutions:
  key1: "I'm a **substitution**"
  key2: |
    ```{note}
    {{ key1 }}
    ```
  fishy: |
    ```{image} /images/fun-fish.png
    :alt: fishy
    :width: 200px
    ```
  jinja: "[Jinja templates](https://jinja.palletsprojects.com/en/2.11.x/)"
  repo_name: "jupyter-book"
  repo_url: "[my repo url](https://github.com/executablebooks/jupyter-book)"
---

# 特殊内容块

指令和角色的常见用法是指定内容的“特殊块”。这使您可以包含更复杂的信息，例如警告和注释，引文和图形。本节涵盖了一些常见的内容。

(content-blocks:myst-extensions)=
## MyST 语法扩展

{term}`MyST Markdown` 具有支持的基本语法，并且可以启用其他语法以添加其他功能。默认情况下，Jupyter Book 为 MyST 启用了一些额外的语法，以更加类似于 Jupyter Notebook 和界面中的 Markdown 体验。

这些扩展是：

`dollarmath`
: 为数学块支持 `$$` 和 `$` 语法。参见 [](./math.md)。

`linkify`
: 自动检测 Markdown 中类似 HTML 的链接并将其转换为超链接。

`substitution`
: 为了允许您定义 Markdown “变量”并在使用它们时替换文本。看 [](content:substitutions)。

`colon_fence`
: 为了使您可以使用 `:::` 防护栅栏，以便使其更易于在不支持 MyST 的界面中呈现。查阅 [](admonitions:colons)。

要启用自己的语法扩展，请使用以下配置模式：

```yaml
parse:
  myst_enable_extensions:
    - extension-1
    - extension-2
```

请注意，这将“覆盖”默认的 Jupyter Book 扩展名列表。您应该包括要启用的所有扩展。

:::{seealso}
有关 MuST 中语法扩展的列表，请参见 [MyST 文档](https://myst-parser.readthedocs.io/en/latest/using/syntax-optional.html)。
:::

(content:admonitions)=
## 备注、警告和其他提示

假设您希望突出显示与页面叙述略有不同的特定文本块。您可以为此使用 **`{note}`** 指令。

例如，以下文本：

````md
```{note}
Here is a note!
```
````

结果如下：

```{note}
Here is a note!
```

````{margin} 关于嵌套的说明
您可以将警告（和其他内容块）彼此嵌套。例如：

:::{note}
这是边距块内的一个 note 块
:::

有关执行此操作的说明，请参见 {ref}`markdown/nesting`。
````

有许多类似样式的文本块。例如，下面是一个 `{warning}` 块：

`````{warning}
这是警告！它是通过以下方式创建的：
````
```{warning}
```
````
`````

有关选项的完整列表，请参见 [`sphinx-book-theme` 文档](https://sphinx-book-theme.readthedocs.io/en/latest/reference/demo.html#admonitions)。

### 具有自定义标题的文本块

您还可以通过使用 **`{admonition}`** 指令来选择消息框的标题。例如，以下文本：

````md
```{admonition} Here's your admonition
Here's the admonition content
```
````

结果如下：

```{admonition} Here's your admonition
Here's the admonition content
```

如果您想对这些块进行样式设置，请使用 `:class:` 选项。例如：

`````{admonition} This admonition was styled...
:class: tip
Using the following pattern:
````
```{admonition} My title
:class: tip
My content
```
````
`````

(admonitions:colons)=
### 与 `:::` 兼容 Markdown 的指令

上面的提示语法使用常规的 [指令语法](content:myst/directives)。但是，如果您使用的接口不支持 {term}`MyST Markdown`，它将呈现为原始文字块。许多指令内部都包含 markdown，如果您希望此 markdown 可以“正常”呈现，则还可以使用 `:::` 栅栏而不是 ` ``` ` 栅栏来定义指令。结果，指令的内容将呈现为 markdown。

例如：

```md
:::{note}
This text is **standard** _Markdown_
:::
```

:::{note}
This text is **standard** _Markdown_
:::

类似于普通指令，这些警告也可以嵌套：

```md
::::{important}
:::{note}
This text is **standard** _Markdown_
:::
::::
```

::::{important}
:::{note}
This text is **standard** _Markdown_
:::
::::

:::{note}
尽管通常建议仅对内容中包含纯 markdown 的指令使用该语法，但是可以将其用于任何类型的指令。
:::

### 将代码单元输出插入提示

如果您想在提示框内插入运行代码的输出，建议使用 [`glue` 函数](content:code-outputs:glue)。例如，我们将从 [代码输出页面](./code-outputs.md) 插入粘贴到书中的输出之一。

下面的代码：

````md
```{note}
Here's my figure:
{glue:figure}`sorted_means_fig`
```
````

生成：

```{note}
Here's my figure:
{glue:}`sorted_means_fig`
```

请参阅 [](content:code-outputs:glue)，以获取有关如何使用 `glue` 将输出直接插入内容中的更多信息。

:::{tip}
要隐藏生成要插入的变量的代码输入和输出，请使用 `remove_cell` 标签。有关更多信息和其他标签选项，请参见 [](../interactive/hiding.md)。
:::

(content-blocks:html-admonitions)=
### HTML admonitions

`admonition` 语法的一个缺点是它不会在不支持该语法的接口中呈现（例如 GitHub）。如果您想使用*纯定义为 HTML* 的提示，MyST 可以通过 `html_admonitions` 扩展来解析它们。要使用它，请首先通过以下配置启用它：

```yaml
parse:
  myst_enable_extensions:
    # 不要忘记列出您要启用的其他任何扩展，
    # 包括默认情况下启用的那些！
    - html_admonition
```

然后，您可以像这样在书中定义警告：

:::{tabbed} Markdown 输入
```html
<div class="admonition note" name="html-admonition" style="background: lightgreen; padding: 10px">
<p class="title">This is the **title**</p>
This is the *content*
</div>
```
:::

:::{tabbed} 渲染输出
<div class="admonition note" name="html-admonition" style="background: lightgreen; padding: 10px">
<p class="title">This is the **title**</p>
This is the *content*
</div>
:::

有关 HTML 警示的更多信息，请参见 [](myst-parser:syntax/html-admonition)。

(content/panels)=
## Panels

`panels` 为您提供了一种简便的方法，可将内容块组织到页面上的灵活容器中。它们对于创建类似卡片的布局，灵活的列和网格很有用。`panels` 基于 [Bootstrap CSS](https://getbootstrap.com/docs/4.5/components/card/)，并利用 Bootstrap 的类来控制面板的外观。

这是一个创建两个 `panels` 的示例：

`````
````{panels}
Panel header 1
^^^
Panel body 1
+++
Panel footer 1
---

Panel header 2
^^^
Panel body 2
+++
Panel footer 2
````
`````

- `---` 分隔每个面板
- `^^^` 定义面板页眉（header）
- `+++` 定义面板页脚（footer）

```{note}
面板页眉和页脚是可选的。如果您的面板中未包含 `^^^` 或 `+++`，它们将不会显示。
```

您可以将各种内容嵌入面板中。例如，以下面板：

````{panels}
Content of the left panel.

{badge}`example-badge,badge-primary`

---

```{link-button} content/panels
:text: Clickable right panel
:type: ref
:classes: stretched-link
```
````

使用以下内容创建：

`````md
````{panels}
Content of the left panel.

{badge}`example-badge,badge-primary`

---

```{link-button} content/panels
:text: Clickable right panel
:type: ref
:classes: stretched-link
```

````
`````

```{seealso}
有关更多信息，请参见 [Sphinx Panels 卡片布局文档](https://sphinx-panels.readthedocs.io/en/latest/#card-layout)。
```

### 控制面板的外观

您可以通过将 bootstrap 传递到面板的页眉/主体/页脚来控制面板的外观。您可以通过将配置选项传递给 `{panels}` 指令来实现。

例如：

```{seealso}
有关更多信息，请参见 [Panel 卡片样式文档](https://sphinx-panels.readthedocs.io/en/latest/#card-styling)。
```

例如，您可以使用 [Bootstrap column 类](https://getbootstrap.com/docs/4.0/layout/grid/) 控制面板中的列数。这些面板：

````{panels}
:column: col-4
:card: border-2
Header A
^^^
Body A
---
Header B
^^^
Body B
---
Header C
^^^
Body C
````

通过以下代码创建：

`````
````{panels}
:column: col-4
:card: border-2
Header A
^^^
Body A
---
Header B
^^^
Body B
---
Header C
^^^
Body C
````
`````

(content:dropdowns)=
## 下拉菜单

下拉菜单使您可以将内容隐藏在标题和按钮后面。Jupyter Book 中有两种下拉菜单：

### `{dropdown}` 指令

使用 `{dropdown}` 指令创建带有标题的可点击下拉菜单。

例如：

`````{panels}
源
^^^
````
```{dropdown} Here's my dropdown
And here's my dropdown content
```
````
---
结果
^^^
```{dropdown} Here's my dropdown
And here's my dropdown content
```
`````

(content/toggle-admonitions)=
### 下拉式提示

您还可以隐藏提示栏的主体，以便用户必须单击按钮才能显示其内容。如果您希望包含一些用户无法立即看到的文本，这将很有帮助。

要将提示变成下拉菜单，请向其中添加 `dropdown` 类。例如：

`````{panels}
源
^^^
````md
```{note}
:class: dropdown
The note body will be hidden!
```
````
---
结果
^^^
```{note}
:class: dropdown
The note body will be hidden!
```
`````

您可以将其与 `{admonition}` 指令结合使用，以包括自己的标题和样式。例如：

`````{panels}
source
^^^
````md
:::{admonition} Click here!
:class: tip, dropdown
Here's what's inside!
:::
````
---
result
^^^
:::{admonition} Click here!
:class: tip, dropdown
Here's what's inside!
:::
`````

:::{important}
下拉菜单式提示要求在查看它们的浏览器中启用 JavaScript。相比之下，下面的 [dropdown 指令](content/panels) 纯粹*通过* HTML + CSS 起作用。
:::

(content/definition-lists)=

## 定义清单

通过在您的 `_config.yml` 中定义以下设置来启用定义清单：

```yaml
parse:
  myst_enable_extensions:
    # 不要忘记列出您要启用的其他任何扩展，
    # 包括默认情况下启用的那些！
    - deflist
```

定义清单利用了 [markdown-it-py deflist 插件](https://markdown-it-py.readthedocs.io/en/latest/plugins.html)，它本身是基于 [Pandoc 定义清单规范](http://johnmacfarlane.net/pandoc/README.html#definition-lists)。

这里有个例子：

````{panels}
source
^^^
```md
Term 1
: Definition

Term 2
: Definition
```
---
result
^^^
Term 1
: Definition

Term 2
: Definition
````

来自 [Pandoc 文档](https://pandoc.org/MANUAL.html#definition-lists):

> 每个术语必须占一行，可以选择在其后跟随一个空白行，并且必须跟随一个或多个定义。
> 定义以冒号或波浪号开头，可以缩进一个或两个空格。
>
> 一个术语可以具有多个定义，并且每个定义都可以包含一个或多个块元素（段落，代码块，列表等）。

这是一个更复杂的示例，展示了其中一些功能：

Term *with Markdown*
: Definition [with reference](content/definition-lists)

  A second paragraph
: A second definition

Term 2
  ~ Definition 2a
  ~ Definition 2b

Term 3
:     A code block
: > A quote
: A final definition, that can even include images:

  <img src="../images/fun-fish.png" alt="fishy" width="200px">

这是使用以下 Markdown 创建的：

```md
Term *with Markdown*
: Definition [with reference](ontent/definition-lists)

  A second paragraph

Term 2
  ~ Definition 2a
  ~ Definition 2b

Term 3
:     A code block

: > A quote

: A final definition, that can even include images:

  <img src="../images/fun-fish.png" alt="fishy" width="200px">
```

## 语录和题词

语录和题词（Quotations and epigraphs） 提供突出显示他人提供的信息的方法。

### 语录

**常规语录**由标准的 Markdown 语法控制，即通过在一行或多行文本的前面插入一个插入符号（`>`）来控制。例如：

````{panels}
source
^^^
```md
> Here is a cool quotation.
>
> From me, Jo the Jovyan
```
---
result
^^^
> Here is a cool quotation.
>
> From me, Jo the Jovyan
````

### 题词

**题词**引起人们对引文的更多关注，并突出了其作者。您应该将它们保持相对较短，以免它们占用过多的垂直空间。这是题词的外观：

`````{panels}
source
^^^
````md
```{epigraph}
Here is a cool quotation.

From me, Jo the Jovyan
```
````
---
result
^^^
```{epigraph}
Here is a cool quotation.

From me, Jo the Jovyan
```
`````

您可以通过在最后一行中添加 `--`，再加上引用的作者，来为题词提供“署名”。例如：

`````{panels}
source
^^^
````md
```{epigraph}
Here is a cool quotation.

-- Jo the Jovyan
```
````
---
result
^^^
```{epigraph}
Here is a cool quotation.

-- Jo the Jovyan
```
`````

## 术语表

术语表允许您在词汇表中定义术语，以便随后可以在整个内容中链接回它。您可以使用以下语法创建术语表：

````md
```{glossary}
Term one
  An indented explanation of term 1

A second term
  An indented explanation of term2
```
````

这将创建：

```{glossary}
Term one
  An indented explanation of term 1

A second term
  An indented explanation of term2
```

要在术语表中引用术语，请使用 `{term}` 角色。例如，`` {term}`Term one` `` 变成 {term}`Term one`，而 `` {term}`A second term` `` 变成 {term}`A second term`。

(content:tabs)=
## 选项卡式内容

您还可以使用 [`sphinx-panels`](sphinx-panels:panels/usage) 生成 [**选项卡式内容**](sphinx-panels:components-tabbed)。这使您可以显示用户可以单击的各种选项卡式内容块。

例如，以下是一组标签，以几种不同的语言展示代码：

````{tabbed} c++

```{code-block} c++

int main(const int argc, const char **argv) {
  return 0;
}
```
````

````{tabbed} python

```{code-block} python

def main():
    return
```
````

````{tabbed} java

```{code-block} java

class Main {
    public static void main(String[] args) {
    }
}
```
````

````{tabbed} julia

```{code-block} julia

function main()
end
```
````

````{tabbed} fortran

```{code-block} fortran

PROGRAM main
END PROGRAM main
```
````

您可以将这个功能与 `{tabbed}` 指令一起使用。您可以提供一系列的 `{tabbed}` 指令，并且每个指令都将用于生成一个新的选项卡（除非在 `{tabbed}` 指令中添加 `:new-group:` 选项。）

例如，以下代码：

````
```{tabbed} Tab 1 title
My first tab
```

```{tabbed} Tab 2 title
My second tab with `some code`!
```
````

输出

```{tabbed} Tab 1 title
My first tab
```

```{tabbed} Tab 2 title
My second tab with `some code`!
```

使用 [`glue` 函数](glue/gluing) 在选项卡中**插入代码输出**。例如，以下选项卡使用此函数来粘合这些文档中其他位置生成的图像和表格：

````{tabbed} A histogram
```{glue:figure} boot_fig
:figwidth: 300px
:name: "fig-boot-tab"

This is a **caption**, with an embedded `{glue:text}` element: {glue:text}`boot_mean:.2f`!
```
````
````{tabbed} A table
```{glue:figure} df_tbl
:figwidth: 300px
:name: "tbl:df-tab"

A caption for a pandas table.
```
````
``````{tabbed} Code to generate this
`````
````{tabbed} A histogram
```{glue:figure} boot_fig
:figwidth: 300px
:name: "fig-boot-tab"

This is a **caption**, with an embedded `{glue:text}` element: {glue:text}`boot_mean:.2f`!
```
````

````{tabbed} A table
```{glue:figure} df_tbl
:figwidth: 300px
:name: "tbl:df-tab"

A caption for a pandas table.
```
````

````{tabbed} Code to generate this
`{ code block here }`
````
`````
``````

有关如何使用此功能的更多信息，请参见 [`sphinx-panels` 选项卡式](sphinx-panels:components-tabbed) 文档。

(content:substitutions)=
## markdown 中的置换和变量

置换（`Substitutions`）允许您在页面的 front-matter 定义**变量**，然后将这些变量**插入**整个内容中。

要使用置换，请首先将 front-matter 的内容添加到页面顶部，如下所示：

````yaml
---
substitutions:
  key1: "I'm a **substitution**"
  key2: |
    ```{note}
    {{ key1 }}
    ```
  fishy: |
    ```{image} img/fun-fish.png
    :alt: fishy
    :width: 200px
    ```
---
````

您可以内联或作为块使用这些置换，甚至可以将置换嵌套在其他置换中（但禁止循环引用）：

:::{tabbed} Markdown 输入

```md
Inline: {{ key1 }}

Block level:

{{ key2 }}

```
:::

:::{tabbed} 渲染输出
Inline: {{ key1 }}

Block level:

{{ key2 }}
:::

您还可以在其他 markdown 结构（例如表格）中插入置换项：

:::{tabbed} Markdown 输入

```md
| col1     | col2      |
| -------- | --------- |
| {{key2}} | {{fishy}} |
```
:::

:::{tabbed} 渲染输出
| col1     | col2      |
| -------- | --------- |
| {{key2}} | {{fishy}} |
:::

:::{seealso}
有关置换的更多信息，请参见 [](myst-parser:syntax/substitutions)。
:::

### 为整本书定义置换

您还可以使用以下配置定义书籍级置换变量：

```yaml
parse:
  myst_substitutions:
    key: value
```

这些置换内容将在您的整本书中提供。例如，在本书的 `_config.yml` 文件中定义了全局置换键 `my-global-substitution`，`{{ sub3 }}` 产生：{{ sub3 }}。

### 格式化置换

MyST 替换使用 {{ jinja }} 来置换键/值。这意味着您可以将任何标准的 Jinja 格式应用于置换。例如，您可以像这样 **replace 置换文本**：

:::{tabbed} Markdown 输入

```md
The original key1: {{ key1 }}

{{ key1 | replace("a substitution", "the best substitution")}}
```
:::

:::{tabbed} 渲染输出
The original key1: {{ key1 }}

{{ key1 | replace("a **substitution**", "**the best substitution**")}}
:::

### 在链接中使用置换

如果您想使用置换来插入和修改书中的“链接”，请探索以下两种方法：

1. **将整个 markdown 链接定义为变量**。例如：

   :::{tabbed} Markdown 输入

   ```yaml
   substitutions:
     repo_url: [my repo url](https://github.com/executablebooks/jupyter-book)
   ```
   ```md
   Here's my link: {{ repo_url }}
   ```
   :::

   :::{tabbed} 渲染输出
   Here's my link: {{ repo_url }}
   :::
2. 使用 Jinja 功能插入变量。由于置换使用  {{ jinja }}，因此您还可以访问置换中的 **Python 格式** 操作。例如：

   :::{tabbed} Markdown 输入

   ```yaml
   substitutions:
     repo_name: jupyter-book
   ```
   ```md
   Here's my link: {{ '[my repo: `{repo}`](https://github.com/executablebooks/{repo})'.format(repo=repo_name) }}
   ```
   :::

   :::{tabbed} 渲染输出
   Here's my link: {{ '[my repo: `{repo}`](https://github.com/executablebooks/{repo})'.format(repo=repo_name) }}
   :::

## 引用和交叉引用

你可以在你的书中添加**引用和交叉引用**（citations and cross-references）。有关如何执行此操作的更多信息，请参见 {doc}`citations`。

## 图形

您可以彻底自定义书中图形的外观。有关更多信息，请参见 {doc}`figures`。

## 页面布局和侧边栏内容

您还可以使用 MyST 来控制页面布局的各个方面。有关此的更多信息，请参见 {doc}`layout`。

## 脚注

您可以使用标准的 Markdown 语法在您的书中添加脚注。这将包括对内嵌脚注的编号引用，并将脚注附加到页面底部的脚注列表中。

要创建脚注，请首先使用以下语法内联插入参考：`[^mylabel]`。然后，为该标签定义文本，如下所示：

```md
[^mylabel]: My footnote text.
```

您可以在页面中的任何位置定义 `[^mylabel]`，尽管其定义始终位于构建页面的底部。例如，这是脚注 [^mynote]，而另一个脚注 [^mynote2]。您可以单击其中任何一个以查看此页面底部的脚注。

[^mynote]: Here's the text of my first note.
[^mynote2]: And the text of my second note.
            Note that
            [you can include Markdown footnote definitions](https://executablebooks.org).

(custom-div-blocks)=
## 自定义 `<div>` 块

您可以使用 `{div}` 指令添加自定义 `div` 块以及所需的任何类。指令 `{div}` 将所有内容与您提供的类一起包装在单个 `<div>` 中。例如：

````md
```{div} my-class
**Some content.**
```
````

构建您的书籍时，将产生以下 HTML：

```html
<div class="my-class">
  <strong>Some content.</strong>
</div>
```

如果您想使用 [自定义 CSS 或 JavaScript](custom-assets) 为书本添加样式，这可能会很有用。
