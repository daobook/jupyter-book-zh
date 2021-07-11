# 建立你的书

添加内容并配置图书后，就该为您的书建立输出。

为此，我们将使用 `jupyter-book build` 命令行工具。

当前，有两种受支持的输出：书籍的 HTML网站，以及包含从书籍 HTML 构建的书籍所有页面的 PDF。

在本教程中，我们将专注于构建 HTML 输出。

## 先决条件

为了构建每个页面的 HTML，您应该遵循 [](overview.md) 和 [](create.md) 中的步骤。

您应该在 `mybookname/` 文件夹中包含一个 Notebook/Markdown 文件集合，`_toc.yml` 文件定义书的结构，以及在 `_config.yml` 文件中进行想要的任何配置。

## 建立书籍的 HTML

既然您的书的内容位于书的文件夹中，并且已经在 `_toc.yml` 中定义了书的结构，则可以为书构建 HTML。

通过运行以下命令来这样做：

```bash
jupyter-book build mybookname/
```

这将使用“静态网站生成器”生成一个功能全面的 HTML 网站。
该站点将放置在 `_build/html` 文件夹中。然后，您可以通过导航到该文件夹并使用 Web 浏览器打开 `html` 文件来打开站点中的页面。

:::{note}
您也可以将 `jupyter-book` 简写为 `jb`， 例如：
`jb build mybookname/`.
:::

## 源文件与构建文件

至此，您已经创建了 Jupyter 笔记本，markdown 文件和配置文件（包括 `_toc.yml` 和 `_config.yml`）的组合。

这些文件是您的 __source__ 文件。__source__ 文件包含 Jupyter Book 用来构建您的书所需的所有内容和配置。

另外，您已经在 `_build` 文件夹中创建了 _outputs_ 的集合。`_build` 文件夹包含您所有的静态网站 __build__ 文件。
__build__ 文件包含 Jupyter Book 的 `build` 命令的所有输出。
这些文件仅用于在浏览器中查看您的内容或与他人共享。

出版书籍的最佳做法是为 __source__ 和 __build__ 文件使用单独的分支。
例如，您可以告诉 git 忽略 `main` 分支上的 `_build` 文件夹，并将 `_build` 文件夹中的输出推送到名为 `gh-pages` 的分支。

稍后我们将介绍其中的一些内容。

:::{admonition} 关于页面缓存的注意事项
:class: tip
默认情况下，Jupyter Book 只会为自上次构建该书以来已更新的页面构建 HTML。

如果您想强制 Jupyter Book 重新构建特定页面，则可以在书的文件夹中编辑相应的文件，也可以删除该页面的 HTML `_build/html` 文件夹中。

您也可以使用 `--all` 选项发出完全重建的信号：

```bash
jupyter-book build --all mybookname/
```
:::

## 预览您构建的 HTML

要预览您的书，您可以在浏览器中打开生成的 HTML 文件。
双击本地文件夹中的 html 文件，或在浏览器导航栏中输入文件的绝对路径，并在开头添加 `file://`。（例如`file://Users/my_path_to_book/_build/index.html`）。

查看从您创建的 markdown 页面生成的网页。
请注意，您插入的链接是如何自动“解析”为指向正确位置的。
这样，您就可以保持从书的一个部分到另一部分的一致的指针。

## 下一步：出版您的书

现在，您已经为书创建了 HTML，现在该在线上发布它了。
在 [下一节](./publish.md) 中进行了介绍。
