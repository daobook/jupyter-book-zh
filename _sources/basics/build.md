# 使用 Build 命令行界面

写完书的内容后，就该构建书的输出了，以便与他人分享。例如，您可能希望构建一个静态网站托管的 HTML 文件，或与同事共享的 PDF 文件。

## 通过命令行构建

构建你的书的基本方法是通过下面的命令：

```bash
jupyter-book build <path-to-book>
```

此外，您可以控制生成的输出的类型，以及您的书进行构建的方式。本页的其余部分涵盖了其中一些选项。

## 构建输出的类型

您可以使用 Jupyter Book 构建各种输出。要选择不同的构建器，请在从命令行运行  `jupyter-book build`时使用 `--builder <builder-name>` 配置。以下是可供你选择的构建器名单：

- `html`：HTML输出（默认）
- `dirhtml`：HTML 输出具有 `<filename>/index.html` 结构。
- `pdfhtml`：通过HTML输出构建PDF（参阅 [](pdf:html)）
- `linkcheck`：运行 Sphinx 链接检查器（参阅 [](html:link-check)）
- `latex`：为你的书建立 Latex 文件
- `pdflatex`：通过 Latex 构建你的书的 PDF 格式（参考 [](pdf:latex)）

## 从你的书的构建中排除一些页面

默认情况下，Jupyter Book 将构建在你的书的文件夹中找到的所有内容文件，即使它们没有在 `_toc.yml` 中指定（如果它发现了一个没有列出的文件，就会发出警告）。

如果你想让 Jupyter Book 完全跳过一个文件，你可以在 `_config.yml` 中使用以下配置：

```yaml
exclude_patterns: [pattern1/*, path/to/myfile.ipynb]
```

任何匹配这里描述的模式的文件都将被排除在构建之外。如果您想要排除正在执行的文件，但仍然希望它们由 Jupyter Book 构建，请参阅 (execute/exclude)。

(clean-build)=
## 清理你的书的生成文件

在构建图书时，可以“清理”生成的文件。如果你最近修改了很多内容，以确保你从头开始写书，这通常是有用的。

你可以通过运行以下命令来清理你的书生成的内容：

```bash
jupyter-book clean mybookname/
```

默认情况下，这将删除 `mybookname/_build`  中的所有除了一个名为 `.jupyter_cache` 文件夹的文件夹。这可以确保重新生成图书的内容，而运行图书的代码生成的缓存不会被删除（因为重新生成可能需要一些时间）。

要删除 `.jupyter_cache` 文件夹，添加 `--all` 标志，如下所示:

```bash
jupyter-book clean mybookname/ --all
```

这将完全删除 `_build/` 目录中的文件夹。

(config:exclude-non-toc-files)=
## 禁用在 TOC 中未指定的构建文件

默认情况下，Jupyter Book 将构建您的图书文件夹中的所有文件，无论它们是否在目录表中指定。要禁用此行为并只构建TOC中指定的文件，请使用 `_config.yml` 中的以下模式：

```yaml
only_build_toc_files: true
```

注意，隐藏文件夹中的文件（例如 `.github` 或 `.venv`）仍然会被构建，即使它们没有在 TOC 中指定。您应该显式地排除这些文件。

## 调试您的书的构建过程

当调试你的书构建时，以下选项可能会很有帮助：

```bash
jupyter-book build -W -n --keep-going mybookname/
```

这将检查丢失的引用(`-n`)，将它们转换为错误(`-W`)，但仍将尝试运行完整的构建(`--keep-going`)，以便您可以在一次运行中看到所有错误。

你也可以使用 `-v` 或 `-vvv` 来增加详细级别。
