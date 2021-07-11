# 在线发布您的书

为您的图书构建 HTML 之后，您就可以在线托管它了。
最好的方法是使用托管“静态网站”的服务
（因为这就是您刚用 Jupyter Book 创建的内容）。
在本教程中，我们将介绍如何使用 GitHub Pages（一种流行且免费的在线托管平台）在线发布您的书。

(publish/online-repo)=
## 为您的书创建在线存储库

为了将托管的书与书的源内容连接起来，您应该将书的源内容放在公共存储库中。本节介绍一种创建自己的 GitHub 存储库并将书的内容添加到其中的方法。

1. 首先，登录 GitHub，然后转到“创建新存储库”页面：<https://github.com/new>

2. 接下来，给您的在线存储库起一个名称和描述。将您的存储库公开，不要使用 README 文件对其进行初始化，然后单击“创建存储库”。

3. 现在，将（当前为空）在线存储库克隆到本地计算机上的某个位置。您可以使用以下命令通过命令行执行此操作：

   ```bash
   git clone https://github.com/<my-org>/<my-repository-name>
   ```

4. 将所有书籍文件和文件夹复制到此新克隆的存储库中。例如，如果您是使用 `jupyter-book create mylocalbook` 在本地创建的书，而您的新存储库名为 `myonlinebook`，则可以通过命令行使用以下命令进行操作：

   ```bash
   cp -r mylocalbook/* myonlinebook/
   ```

5. 现在，您需要同步本地和远程（即在线）存储库。您可以使用以下命令执行此操作：

   ```bash
   cd myonlinebook
   git add ./*
   git commit -m "adding my first book!"
   git push
   ```

## 通过 GitHub Pages 在线发布您的书

我们刚刚将本书的“源文件”推送到了 GitHub 存储库中。这使得您或其他人可以公开访问。

接下来，我们将在线发布本书的“构建工件”，以便将其呈现为网站。

在构建的 HTML 中使用 GitHub Pages 的最简单方法是使用 [`ghp-import`](https://github.com/davisp/ghp-import) 包。`ghp-import` 是一个轻量级的 Python 软件包，可轻松将 HTML 内容推送到 GitHub 存储库。

`ghp-import` 的工作原理是将已构建的书的所有内容（即 `_build/html` 文件夹）复制到仓库的一个分支 `gh-pages` 中，并将其推送到 GitHub。`gh-pages` 分支将由 `ghp-import` 自动创建并填充。要使用 `ghp-import` 通过 GitHub Pages 在线托管您的图书，请执行以下步骤：

```{note}
在执行以下步骤之前，请确保已为书籍的每一页构建了 HTML（请参见 {doc}`上一节<../start/build>`）。您的书的 `_build/html` 文件夹中应该有 HTML 文件的集合。
```

1. 安装 `ghp-import`

   ```bash
   pip install ghp-import
   ```
2. 更新您的 GitHub 页面网站的设置：

    a. 使用 `gh-pages` 分支来托管您的网站。

    b. 如果要在自己的存储库中构建书籍，请选择根目录 `/`。如果要使用 jupyter-book 构建文档，请选择 `/docs` 目录。

3. 从书籍根目录的 `main` 分支（应包含 `_build/html` 文件夹）中，调用 `ghp-import` 并将其指向您的 HTML 文件，如下所示：

   ```bash
   ghp-import -n -p -f _build/html
   ```

```{warning}
确保您包含 `-n`：这告诉 GitHub *不要*用 [Jekyll](https://jekyllrb.com/) 来构建您的书，我们不希望这样做，因为我们的 HTML 已经建立了！
```

通常，几分钟后，您的网站应该可以通过以下网址在线查看：`https://<user>.github.io/<myonlinebook>/`。 如果不行，请在**Options** -> **GitHub Pages** 下检查您的存储库设置，以确保将 `gh-pages` 分支配置为 GitHub Pages 的构建源和/或查找 GitHub 的 URL 地址。

要更新您的在线图书，请在存储库的 `main` 分支上更改图书的内容，使用 `jupyter-book build mybookname/` 重新构建图书，然后使用 `ghp-import -n -p -f mylocalbook/_build/html` 将新建的 HTML 推送到 gh-pages 分支。

```{warning}
请从 [`ghp-import` GitHub 存储库](https://github.com/davisp/ghp-import) 注意此警告：

"...*`ghp-import` will DESTROY your gh-pages branch... and assumes that the `gh-pages` branch is 100% derivative. You should never edit files in your `gh-pages` branch by hand if you're using this script...*"
```
