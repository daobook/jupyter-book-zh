(working-on-windows)=
# Windows 上的配置

Jupyter Book 现在也在 Python 3.7 的 Windows 环境下进行了测试 😀。

有关其规范，请参阅 GitHub CI 使用的[`windows-latest` runner](https://docs.github.com/en/actions/reference/virtual-environments-for-github-hosted-runners#supported-runners-and-hardware-resources)。

然而，在使用 Python 3.8 时，笔记本（notebook）执行有一个已知的不兼容性
(见问题[#906](https://github.com/executablebooks/jupyter-book/issues/906))。

如果你运行的是最新版本的 Windows 10，遇到任何问题，你也可以尝试一下
[安装 Windows Linux 子系统](https://docs.microsoft.com/en-us/windows/wsl/install-win10)。

截至 2020 年 6 月 5 日，有三个需要针对 windows 系统进行修改的未解决问题。
我们希望这些问题在 0.8 版的 Jupyter Book 中得到修复，但是，如果仍然出现任何问题，
我们留下这些社区提示，它们对一些用户来说是有用的。

1. 字符编码

    Jupyter Book 目前在 Windows 上以本机 Windows 编码读取和写入文件，这将导致 UTF8 编码的笔记本中某些字符的编码错误。

    **Work-around:**  从 [Python 3.7](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUTF8) 开始
    设置 `PYTHONUTF8=1` 的 cmd.exe 或 powershell 环境将覆盖本机语言环境编码，并对所有输入/输出使用 UTF8。

    :::{tip}
    为了方便使用这个选项，
    EOAS/UBC 笔记本课件项目创建了一个 Conda 包[runjb](https://anaconda.org/eoas_ubc/runjb)，[为 powershell 自动执行此操作](https://github.com/eoas-ubc/eoas_tlef/blob/master/converted_docs/wintools/binwin/runjb.ps1)
    :::

2. 一个新的 Windows 事件循环

   asyncio 事件循环[已在Python 3.8 中更改](https://github.com/sphinx-doc/sphinx/issues/7310)导致 sphinx-build 失败。

   **Work-around:**  Pin to Python 3.7.6. 这个 [environment_win.yml](https://github.com/eoas-ubc/quantecon-mini-example/blob/windows/environment_win.yml) 文件做到了这一点，并且还安装了 runjb 来修复问题1。

3. 嵌套的目录

   目前 `_toc.yml` 对于一些 Windows 用户来说，引用子文件夹中的 Markdown 文件是失败的。也就是说，这个[原始_toc.yml](https://github.com/eoas-ubc/quantecon-mini-example/blob/master/mini_book/_toc.yml)文件将会失败，并有一个消息说 Jupyter Book " "```cannot find index.md```"

   **Work-around**: 把书的布局平铺到一个层次，即：
   [此 `_toc.yml`](https://github.com/eoas-ubc/quantecon-mini-example/blob/windows/mini_book/docs/_toc.yml) 文件适用于 Windows。
   
**Summary**

在 Windows 10 上使用 miniconda powershell 终端应该可以成功执行以下工作流程:

1. `conda install git`
2. `git clone https://github.com/eoas-ubc/quantecon-mini-example.git`
3. `cd quantecon-mini-example`
4. `git checkout windows`
5. `conda env create -f environment_win.yml`
6. `conda activate wintest`
7. `cd mini_book`
8. `runjb docs`

构建完成后，使用以下命令查看 HTML:

`start docs\_build\html\index.html`
