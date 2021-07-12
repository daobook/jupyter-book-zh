# 高级 HTML 输出

(custom-assets)=
## Custom CSS or JavaScript

If you'd like to include custom CSS rules or JavaScript scripts in your book, add them to a folder called `_static` in your book's folder.
Any files that end in `.css` or `.js` in this folder will automatically be copied into your built book HTML and linked in the header of each page.

For example, to include a custom CSS file `myfile.css` in a Jupyter Book folder with the following structure:

```
mybook/
├── _config.yml
├── _toc.yml
└── page1.md
```

Add the static file here:

```
├── _config.yml
├── _toc.yml
├── page1.md
└── _static
    └── myfile.css
```

The rules should then automatically be applied to your site. In general, these
CSS and JS files will be loaded *after* others are loaded on your page, so they
should overwrite pre-existing rules and behaviour.

### An example: justify the text

If you want the text of you book to be justified instead of left aligned then create `myfile.css` under `mybook/_static` with the following CSS:

```css
p {
    text-align: justify;
}
```

## 启用 Google Analytics

如果你有谷歌账户，你可以使用谷歌 Analytics 来收集一些关于你的 Jupyter Book 的流量信息。有了这个工具，你可以知道有多少人在使用你的书，他们来自哪里，他们如何访问它，他们使用的是桌面版本还是移动版本等等。

要添加谷歌 Analytics 到您的 Jupyter Book，导航到[谷歌 Analytics](https://analytics.google.com/analytics/web/)，创建一个新的谷歌 Analytics 帐户，并添加您的 Jupyter Book 的 url 到一个新的属性。一旦你设置好了一切，你的谷歌 Analytics 属性将拥有一个所谓的 Tracking-ID，它通常以字母 UA 开头。你需要做的就是复制这个 ID 并粘贴到你的配置文件中：

```yaml
html:
  google_analytics_id: UA-XXXXXXXXX-X
```

(html:link-check)=
## 检查你书中的外部链接

如果您想确保您的书之外的链接是有效的，请使用 Jupyter Book 运行 Sphinx 链接检查器。这将检查您的每个外部链接，并确保它们解析。

```{margin}
请注意，您必须确保每个链接都是正确的 target，链接检查器只会确保它能够解析。
```

运行链接检查器，使用如下命令：

```bash
jupyter-book build mybookname/ --builder linkcheck
```

它会打印出你书中每个链接的状态，以便你以后可以解决任何不正确的链接。

(raw-html-in-markdown)=
## 在 Markdown 中使用原始 HTML

Jupyter Notebook Markdown 允许您在 Markdown 单元格中使用原始 HTML。在大多数情况下，这是不鼓励的，因为它通常只是作为原始文本通过构建过程，所以不会受到以下过程的影响：

- 相对路径修正
- 将 assets 复制到构建文件夹
- 多种输出类型格式化（例如，它不会显示在 PDF！）

例如，我们在下面添加：

```md
<a href="intro">Go Home HTML!</a>

[Go Home Markdown!](intro)
```

你会发现 HTML 链接被打断了：

<a href="intro">Go Home HTML!</a>

[Go Home Markdown!](intro)

:::{tip}
注意，MyST Markdown 现在有一些扩展语法特性，可以允许您以正确的方式使用某些 HTML 元素。

例如，原始 HTML 图像标记

```html
<img src="../images/fun-fish.png" alt="the fun fish!" width="200px"/>
```

变成

<img src="../images/fun-fish.png" alt="the fun fish!" width="200px"/>

有关详细信息，请参阅[图像部分](content-blocks-images)。
:::

## 添加额外的 HTML 到你的书

在 Jupyter Book 中有一些地方可以添加额外的任意 HTML。在所有情况下，这都是通过 `_config.yml` 文件中的配置值来完成的。

### 在你的页脚拓展 HTML

要在书的页脚添加额外的 HTML，使用以下配置：

```yaml
html:
    extra_footer: |
        <div>
            your html
        </div>
```

`extra_footer` 的内容将被插入到页面的 HTML 中，但在所有其他页脚内容之后。

### 添加额外的 HTML 到你的左导航栏

要在书的左侧导航栏中添加额外的 HTML，请使用以下配置：

```yaml
html:
    extra_navbar: |
        <div>
            your html
        </div>
```

`extra_navbar` 的内容会被插入到页面的 HTML中，在所有其他 HTML 内容之后。

## 向 HTML 页脚添加许可证

如果您想为您的书添加更详细的许可证，或者想为许可证添加到外部页面的链接，最简单的方法是使用自定义页脚。你可以禁用自动添加到每个页脚的“版权”文本，并添加任何你想要的页脚 HTML。

例如，请看下面的配置：

```yaml
html:
  extra_footer: |
    <p>
    ... Add license info here...
    </p>
sphinx:
  config:
    html_show_copyright: false
```

注意，这可能不适用于 LaTeX 生成的页面的 PDF 构建。


(sphinx:manual-assets)=
## 手动指定网站中要包含的额外文件/文件夹

Jupyter Book 将复制任何文件，从其页面内的链接，使链接工作在构建网站。然而，有时你想手动确保文件和文件夹包含在你构建的网站中。例如，如果您希望从构建文档之外而不是从构建文档内部链接到它们。

若要手动指定要复制的项，请使用 [`html_extra_path` Sphinx 配置](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_extra_path)。你可以用 Jupyter Book 这样配置：

```yaml
sphinx:
  config:
    html_extra_path: ['folder1', 'folder2']
```

当你构建你的书的 HTML, Jupyter Book 将确保所有文件和文件夹内指定的文件夹 `html_extra_path` 将复制到你构建的网站。

例如，如果你的书中有这样的文件夹结构：

```bash
assets
└── data
    └── mydataset.csv
```

和以下 Jupyter Book配置：

```yaml
sphinx:
  config:
    html_extra_path: ['assets']
```

然后可以通过 `yourwebsite.com/data/mydataset.csv` 访问该数据集。

## 配置提升可访问性

声明书中使用的主要语言有助于改善屏幕阅读器和浏览器翻译工具。

可以通过在 `_config.yml` 中的 `sphinx` 配置中为 `language` 选项提供适当的 [语言代码](https://www.w3schools.com/tags/ref_language_codes.asp) 来配置：

```yaml
sphinx:
  config:
    language: en
```

这个例子将把书的语言设置为英语，在你书的 HTML 中，它将表示为 `<html lang="en">...</html>`。
