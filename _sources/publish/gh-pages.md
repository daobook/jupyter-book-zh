(publish/gh-pages)=
# GitHub Pages 与 Actions

一旦你的内容在 GitHub 上，你可以很容易地托管它作为一个 [GitHub Pages](https://docs.github.com/en/github/working-with-github-pages) 网站。这是一个 GitHub 托管静态文件的服务，就像它们是一个独立的网站。

有三种方法可以让你快速在 GitHub 页面上托管你的书:

* 复制/粘贴你的书的HTML到 `docs/` 文件夹，或 `gh-pages` 的存储库分支。
* 使用 `ghp-import` 工具自动将您构建的文档推送到 `gh-pages` 分支。
* 使用 GitHub Action 自动构建你的书和更新你的网站时，你改变的内容。

我们将涵盖下面的每个选项。

## 手动将你的书的内容放到网上

在这种情况下，你手动构建你的书的文件，然后把它们推到一个 GitHub 仓库，以便作为一个网站托管。
有两种方法

:::{admonition} 确保先完成这些步骤
:class: warning
在执行以下任何操作之前，请确保已完成以下两个步骤:

1. 为你的书构建HTML(见 [](../start/build.md))。
  在你的书的 `_build/html` 文件夹中应该有一个 HTML 文件集合。
2. 配置你的 GitHub 库，通过 GitHub 页面在你选择的位置(一个分支或 `docs/` 文件夹)服务一个网站。
   更多信息请参见[GitHub Pages文档](https://docs.github.com/en/github/working-with-github-pages)。
:::

### (选项1)复制并粘贴你的书的 `_build` 内容到一个新的文件夹

最简单的方法来托管你的书在线是简单地复制一切是在 `_build` 内，并把它放在一个位置，GitHub 页面知道看。
我们推荐两个地方：

在一个单独的分支中
: 你可以配置 GitHub Pages 来构建你指定的分支中的任何书籍。
  默认情况下，是 `gh-pages`。

在主分支的 `docs/` 文件夹中
: 如果你想把构建好的书放在源文件旁边，你可以把它们粘贴到 `docs/` 文件夹中。
  :::{warning}
  请注意，将所有图书的构建文件复制到与源文件相同的分支中，会导致您的存储库随着时间的推移变得非常大，特别是如果您的图书中有许多图像。
  :::

无论哪种情况，请遵循以下步骤：

1. 复制 `_build/html` 目录的内容到 `docs`(或你的其他分支)。
2. 添加一个名为 `.nojekyll` 的文件在你书的内容旁边。
   这告诉 GitHub Pages 把你的文件当作一个“静态HTML网站”。
3. 将你的更改推送到 GitHub，然后 [configure it to start hosting your documentation](https://docs.github.com/en/github/working-with-github-pages).

### (选项2)使用 `ghp-import` 自动推送你的构建文件

使用 GitHub 页面与你构建的 HTML 最简单的方法是使用 [`ghp-import`](https://github.com/davisp/ghp-import) 包。`ghp-import` 是一个轻量级的 Python 包，可以很容易地将 HTML 内容推送到 GitHub 存储库。

`ghp-import` 通过复制你构建的书的*所有*内容(即 `_build/html` 文件夹)到你的存储库名为 `gh-pages` 的分支，并将其推送到 GitHub。
`gh-pages` 分支将由 `ghp-import` 自动创建并填充。
使用 `ghp-import` 来托管您的图书在线 GitHub 页面遵循以下步骤:

1. 安装 `ghp-import`

   ```bash
   pip install ghp-import
   ```

2. 从你的书的根目录的 `main` 分支(它应该包含 `_build/html` 文件夹)调用 `ghp-import`，并指向你的 HTML 文件，像这样：

   ```bash
   ghp-import -n -p -f _build/html
   ```

```{warning}
确保包含了`-n`。这将添加一个名为 `.nojekyll` 到你的书的输出，这告诉 GitHub 不要使用 [Jekyll](https://jekyllrb.com/) 构建你的书。
```

通常在几分钟后，您的网站应该可以在线查看，网址如：`https://<user>.github.io/<myonlinebook>/`。如果不行，检查你的仓库设置下**Options** -> **GitHub Pages**，以确保 `gh-pages` 分支配置为 GitHub 页面的构建源和/或找到 GitHub 正在为你构建的 url 地址。

要更新你的在线图书，请在你的存储库的 `main` 分支上修改你的图书的内容，用 `jupyter-book build mybookname/` 重新构建你的图书，然后像以前一样使用 `ghp-import -n -p -f mylocalbook/_build/html` 将新构建的 HTML 推到 `gh-pages` 分支。

```{warning}
注意这个警告来自 [`ghp-import` GitHub repository](https://github.com/davisp/ghp-import)：

"...*`ghp-import` will DESTROY your gh-pages branch... and assumes that the `gh-pages` branch is 100% derivative. You should never edit files in your `gh-pages` branch by hand if you're using this script...*"
```

(publish/gh-actions)=
## Automatically host your book with GitHub Actions

[GitHub Actions](https://docs.github.com/en/actions) 是一个让你在 GitHub 上自动化的工具。
它被用于各种各样的事情，比如测试、发布包和持续集成。

请注意，如果你没有在 GitHub 上托管你的书，或者如果你想要另一个用户友好的服务来自动构建它，请参阅 [guide to publishing your book on Netlify](./netlify.md)。

```{note}
在使用 GitHub Actions 自动托管你的 Jupyter Books 之前，你应该熟悉 GitHub Actions。
参见 [GitHub Actions文档](https://help.github.com/en/actions) 获取更多信息。
```

要用 GitHub 的 Actions 构建你的书，你需要创建一个做以下事情的动作:

* 当 `main` (或任何一个)分支上发生一个 *push* 事件时激活，该分支有你最新的书内容。
* 安装 Jupyter Book 和构建图书所需的任何依赖项。
* 构建你的书的 HTML。
* 使用 `gh-pages` 动作将 HTML 上传到 `gh-pages` 分支。

作为参考，[这里有一个示例库](https://github.com/executablebooks/github-action-demo) 使用 GitHub Actions 构建了一本书。

```{note}
确保你的 `requirements.txt` 文件中的 Jupyter Book 版本至少是
`0.7.0`.
```

:::{tip}
你可以使用 [Jupyter Book cookiecutter](https://github.com/executablebooks/cookiecutter-jupyter-book) 快速创建一个已经包含 GitHub Actions 工作流文件的图书模板，该文件需要自动部署你的图书到 GitHub 页面：

```bash
jupyter-book create --cookiecutter mybookpath/
```

更多帮助，请参阅 [Jupyter Book cookiecutter GitHub repository](https://github.com/executablebooks/cookiecutter-jupyter-book)，或运行:

```bash
jupyter-book create --help
```
:::

下面是一个 Github Action 的简单 YAML 配置，它将把你的书发布到一个 `gh-pages` 分支。

```yaml
name: deploy-book

# Only run this when the master branch changes
on:
  push:
    branches:
    - master
    # If your git repository has the Jupyter Book within some-subfolder next to
    # unrelated files, you can make this run only if a file within that specific
    # folder has been modified.
    #
    # paths:
    # - some-subfolder/**

# This job installs dependencies, build the book, and pushes it to `gh-pages`
jobs:
  deploy-book:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2

    # Install dependencies
    - name: Set up Python 3.7
      uses: actions/setup-python@v2
      with:
        python-version: 3.8

    - name: Install dependencies
      run: |
        pip install -r requirements.txt

    # Build the book
    - name: Build the book
      run: |
        jupyter-book build .

    # Push the book's HTML to github-pages
    - name: GitHub Pages action
      uses: peaceiris/actions-gh-pages@v3.6.1
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./_build/html
```

如果你想把你的站点部署到一个用户和组织库的 GitHub 页面(`<username>.github.io`)，检查另一个示例工作流和可用的选项在 [peaceiris/actions-gh-pages](https://github.com/peaceiris/actions-gh-pages) 的 README。
