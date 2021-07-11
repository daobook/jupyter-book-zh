# 为 Jupyter Book 贡献

欢迎来到 `jupyter-book` 仓库！我们很高兴你能来这里并想要有所贡献。✨

:::{admonition} 一定要看看我们的行为准则
可执行书籍社区遵循[行为准则](https://github.com/executablebooks/.github/blob/master/CODE_OF_CONDUCT.md)，以确保我们的在线空间是令人愉快的，包容性的，并对所有贡献者具有生产力。
:::

## 开发指南

有关开发约定、实践和基础设施的信息，请参阅 [`executablebooks/` 开发指南](https://github.com/executablebooks/.github/blob/master/CONTRIBUTING.md)。

## 文档指南

Jupyter Book 的文档是受到 [Diataxis 文档框架](https://diataxis.fr/)的启发。这将文档分为四个主要区域：

**教程**
: **面向学习的循序渐进的指南**。他们给学习者一种工具是如何工作的感觉，并让他们对学习更多的东西感到兴奋。教程位于文档的专门部分。

**How-To 指南**
: **告诉读者如何做某事的简短指南**。他们假定更多的 Jupyter Book 背景知识（通常，他们已经阅读教程）。他们专注于“做事”而不是长篇大论的解释。How-To 指南构成了大部分的 Jupyter Book 文档，并且针对不同的主题分为不同的部分。

**参考**
: **完整地描述了 Jupyter Book 的结构和功能**。它更具有编程性，更少叙述性，更感兴趣的是涵盖所有的配置和选项，而不是描述如何以及何时使用它们。Jupyter Book 在我们的主题部分之后有一个参考部分。此外，它下面有一个组织级参考部分。

**解释**
: **关于与 Jupyter 有关的主题和概念的更高层次的讨论**。他们不太专注于做事情，而更专注于获得关于  Jupyter Book 如何工作的概念性框架。Jupyter Book 目前没有专门的解释部分，但欢迎添加解释性内容和一个专门的部分。

这四个方面并不是  Jupyter Book 文档的**严格规则**，但是应该作为决定文档内容和位置的灵感。任何属于该框架的文档贡献（例如，添加一个新教程，添加一个 How to 部分）都是最受欢迎的！

## 入门指南

要开始使用 Jupyter Book 的*代码库*，请执行以下步骤：

### 克隆并安装该包

```bash
git clone https://github.com/executablebooks/jupyter-book
cd jupyter-book
```

接下来，安装：

```bash
pip install -e .[all]
```

这将在本地安装 Jupyter Book，以及测试它所需的包和确保代码风格的包。

### 安装 pre-commit 钩子

在提交之前，Jupyter Book 使用 [pre-commit](https://pre-commit.com/) 来确保代码风格和质量。这确保了 Jupyter Book 的外观和感觉随时间和开发人员保持一致。`pre-commit` 是在使用 `pip install -e .[code_style]` 安装 Jupyter Book 时安装的。

要为您的克隆启用 `pre-commit`，请从存储库根目录运行以下命令：

```bash
pre-commit install
```

从现在开始，当你提交到 Jupyter Book 时，`pre-commit` 将确保你的代码根据一些检查看起来是正确的。

### 运行测试

对于代码测试，Jupyter Book 使用 [pytest](https://docs.pytest.org)。可以使用以下命令运行所有测试，或仅运行不需要额外安装的测试：

```shell
>> pytest -m 'not requires_chrome and not requires_tex'
```

您也可以使用 [tox](https://tox.readthedocs.io) 在多个隔离的环境中运行测试，而且不需要安装初始依赖项（有关可用的测试环境和进一步说明，请参阅 `tox.ini` 文件）：

```shell
>> tox -e py38-sphinx3 -- -m 'not requires_chrome and not requires_tex'
```

除了 *PDF 测试*外，两者都将运行 Jupyter Book 测试套件。这是因为运行 PDF 生成测试需要一个完整的 LaTeX 环境，而您可能没有设置这个环境。

:::{note}
Jupyter Book 使用 [pytest-xdist](https://github.com/pytest-dev/pytest-xdist) 并行运行测试。您可以通过使用 `-n` 参数和您希望使用的 CPU 数量运行测试来利用这一点。例如：`pytest -n 4` 这使得测试运行得更快。
:::

### 要测试 PDF 生成

如果你想测试（或尝试）PDF 的生成，请执行以下步骤：

**通过 HTML 生成 PDF 文件**请确保使用 `pip install -e .[pdfhtml]` 安装 Jupiter Book。这将安装 [`pyppeteer`](https://github.com/pyppeteer/pyppeteer)，它运行一个 headless chrome 会话来将你的书转换成 PDF。接下来，遵照 {ref}`pdf:html` 的安装说明。然后，您应该能够通过 HTML 构建图书的 PDF。

**要通过 LaTeX 生成 PDF 文件**，确保您在本地安装了一个可工作的 LaTeX 发行版。请按照 {ref}`pdf:latex` 说明进行操作。

如果您已经安装了 HTML 和 LaTeX 生成的需求，那么您应该能够使用 pytest 运行完整的测试套件。

### GitHub Actions Artifacts

每个 pull 请求都包含一个测试，即使用 `pdfhtml` 和 `pdflatex` 编写器将 `docs` 构建为 `PDF` 文件。这些测试构建 `pdf` 文件，然后将其保存为附加到每个运行的工作流的工件（artifact）。

可以从[工作流运行的右上角](https://github.com/actions/upload-artifact#where-does-the-upload-go)检索这些 `pdf` 文件。

## Jupyter Book 的仓库结构

本节将介绍 [Jupyter Book 存储库](https://github.com/executablebooks/jupyter-book) 的一般结构，并解释哪些部分位于何处。

Jupyter Book 存储库包含两个主要部分：

### MyST Markdown

Jupyter Book 支持名为“MyST Markdown”的 Jupyter Markdown 扩展版本。有关 MyST 语法和如何使用它的信息，请参见 [MyST-Parser 文档](https://myst-parser.readthedocs.io/en/latest/using/syntax.html)。

### 命令行工具和 Python 包

这是用来帮助创建和构建书籍。可以在 [`./jupyter_book`](https://github.com/executablebooks/jupyter-book/tree/master/jupyter_book) 中找到。

* **`commands/` 文件夹中的 CLI**。这是用户通过命令行创建、构建和控制图书的接口。
* **`sphinx.py` 模块构建书籍**。
* **`yaml.py` 模块处理配置**。
* **`toc.py` 模块准备目录**。

Jupyter Book 中其他模块处理更具体的功能。请参阅它们的模块文档字符串以获得更多信息。

### Jupyter Book 模板

Jupyter Book 捆绑了一个小的模板书来渲染内容。`jupyter-book build` 可以立即建立。可以在 [`jupyter_book/book_template`](https://github.com/executablebooks/jupyter-book/tree/master/jupyter_book/book_template) 中获取。

### 示例

这里有一些示例，说明如何使用这些代码来帮助您入门。

Here are a few examples of how this code gets used to help you get started.

* 当运行 `jupyter-book create mybook/` 时，`create.py` 模块会使用 `jupyter_book/book_template/` 中的模板生成一个空模板。
* 当运行 `jupyter-book build mybook/` 时，`build.py` 模块循环遍历页面内容文件，并使用 `page/` 模块将每个文件转换为 HTML，并将其放在 `mybook/_build` 中。

希望这个解释能让你了解情况，并帮助你理解这些部分是如何组合在一起的。如果你有任何问题，请随时[打开一个 issue 寻求](https://github.com/executablebooks/jupyter-book/issues/new)帮助！

## Jupyter Book 栈中的其他主要工具

Jupyter Book 依赖于 Python/Sphinx 生态系统中的一组开源工具。这些工具做了许多繁重的工作，并且是许多改进和改变将需要的地方。以下是主要工具的列表以及它们支持的功能：

* {term}`Sphinx 文档引擎<Sphinx>` 用于构建图书输出。这依赖于许多由 Jupyter Book 开发的扩展。
* {term}`MyST Markdown<MyST>` 被 {term}`MyST-Parser<MyST-Parser>` 解析为 Sphinx。
* {term}`MyST-NB 包<MyST-NB>` 将 Jupyter 笔记本解析为 Sphinx，并控制笔记本执行的某些部分。它还允许 [将代码输出插入内容中](content:code-outputs:glue)。
* {term}`Jupyter-Cache` 在构建时管理笔记本内容的执行和缓存。它是由 {term}`MyST-NB` 控制。
* {term}`Sphinx Book Theme` 定义了 Jupyter Book 的外观和感觉，并且是大多数 CSS 规则的定义的。
