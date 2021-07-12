---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# 执行并缓存页面

Jupyter Book 可以自动运行和缓存任何笔记本的页面。笔记本可以在每次构建文档时运行，也可以在本地缓存，以便只有当笔记本中的代码单元发生更改时才会重新运行笔记本。

缓存行为由 [`_config.yml` 文件](../customize/config.md) 中的 `execute:` 部分控制。有关每个配置选项及其效果，请参见下面的部分。

:::{tip}
如果你想执行 Markdown 文件中的代码，你可以使用 MyST Markdown 中的 `{code-cell}` 指令。查看 [](../file-types/myst-notebooks.md) 以获取更多信息。
:::

## 触发笔记本执行

默认情况下，Jupyter Book 将执行任何具有笔记本结构且至少缺少一个输出的内容文件。这相当于 `_config.yml` 中的以下配置:

```yaml
execute:
  execute_notebooks: auto
```

这将只执行缺少至少一个输出的笔记本。如果笔记本已经填充了它的所有输出，那么它将不会被执行。

要**强制执行所有笔记本，而不管它们的输出**，请将上面的配置值更改为：

```yaml
execute_notebooks: force
```

要**使用 [jupyter-cache] 缓存执行输出**，请将上面的配置值更改为：

```yaml
execute:
  execute_notebooks: cache
```

有关更多信息，请参见 {ref}`execute/cache` 。

要**关闭笔记本执行**，请将上述配置值更改为：

```yaml
execute:
  execute_notebooks: 'off'
```

(execute/exclude)=
## 从执行中排除文件

要**从执行中排除某些文件模式**，请使用以下配置：

```yaml
execute:
  exclude_patterns:
    - 'pattern1'
    - 'pattern2'
    - '*pattern3withwildcard'
```

任何匹配 `exclude_patterns` 中的一个项的文件都不会被执行。

:::{tip}
要自动排除目录之外的所有文件，请参见 [](config:exclude-non-toc-files)
:::

(execute/cache)=
## 缓存笔记本执行

您也可以使用 [jupyter-cache] 缓存执行笔记本页面的结果。在这种情况下，当执行页面时，它的输出将存储在本地数据库中。这允许您确保文档中的输出是最新的，同时节省时间，避免不必要的重新执行。它还允许您在 `git` 存储库中存储 `.ipynb` 文件，而不需要它们的输出，但在构建站点时仍然利用缓存节省时间。

当你重新构建你的网站时，会发生以下情况：

* 自上次构建以来**代码单元**没有发生变化的笔记本将不会被重新执行。相反，它们的输出将从缓存中提取并插入到您的站点中。
* 对其代码单元**有任何更改的笔记本**将被重新执行，缓存将被新的输出更新。

要启用笔记本输出的缓存，请使用以下配置：

```yaml
execute:
  execute_notebooks: cache
```

默认情况下，缓存将放置在构建文件夹的父目录中。一般来说，这是 `_build/.jupyter_cache` 中。

你也可以指定一个路径到你想要使用的 jupyter cache 的位置：

```yaml
execute:
  cache: path/to/mycache
```

该路径应该指向一个**空文件夹**，或者一个文件夹中已经**存在的 jupyter cache**。

[jupyter-cache]: https://github.com/executablebooks/jupyter-cache "the Jupyter Cache Project"

## 执行配置

你可以使用 `_config.yml` 在项目级别控制笔记本的执行和输出内容的处理，但在某些情况下，也在笔记本和代码单元级别。下面我们将探讨几种实现这一目标的方法。

:::{seealso}
[](jupyter-cell-tags) 和 [](./code-outputs.md).
:::

### 执行工作目录

:::{important}
`cache` 的默认行为现在是在本地目录中运行。这是 `v0.7` 的一个变化。
:::

默认情况下，运行笔记本的命令工作目录（cwd）将是笔记本所在的目录（对于 `auto` 和 `cache` 而言）。这意味着需要在相对路径上访问 assets 的笔记本可以工作。

或者，如果您希望您的笔记本在一个临时文件夹中隔离您的笔记本执行，您可以使用以下 `_config.yml` 设置：

```yaml
execute:
  run_in_temp: true
```

### 设置执行超时

执行超时定义了每个笔记本单元格允许运行的最大时间(以秒为单位)。如果执行时间较长，将引发异常。默认值是 30 秒，因此对于长时间运行的单元格，您可能希望指定一个更高的值。`timeout` 选项也可以设置为 `-1`，以删除对执行时间的任何限制。

你可以在 `_config.yml` 中设置所有笔记本执行的超时时间：

```yaml
execute:
  timeout: 100
```

这个全局值也可以通过添加到你的笔记本元数据来覆盖每个笔记本：

```json
{
 "metadata": {
  "execution": {
      "timeout": 30
  }
}
```

### 处理引发错误的代码

在某些情况下，您可能希望有意地显示不起作用的代码（例如，显示错误消息）

你可以在 `_config.yml` 中允许所有笔记本出错：

```yaml
execute:
  allow_errors: true
```

这个全局值也可以通过添加到你的笔记本元数据来覆盖每个笔记本：

```json
{
 "metadata": {
  "execution": {
      "allow_errors": false
  }
}
```

最后，通过向代码单元格添加 `raises-exception` 标记，可以允许单元格级别的错误。这可以通过一个 Jupyter 接口来实现，或者通过 `{code-cell}` 指令:

Lastly, you can allow errors at a cell level, by adding a `raises-exception` tag to your code cell.
This can be done via a Jupyter interface, or via the `{code-cell}` directive like so:

````md
```{code-cell}
---
tags: [raises-exception]
---
print(thisvariabledoesntexist)
```
````

将产生

```{code-cell}
---
tags: [raises-exception]
---
print(thisvariabledoesntexist)
```

### 处理产生标准错误的代码

您可能还希望控制如何处理 stderr 输出。

或者，您可以使用 `nb_output_stderr` 配置值在全局配置级别配置如何处理 stdout。

你可以在 `_config.yml` 中配置所有笔记本的默认行为：

```yaml
execute:
  stderr_output: show
```

其中值为：

* `"show"` （默认）：显示所有 stderr（除非有 `remove-stderr` 标记）
* `"remove"`: 移除全部 stderr
* `"remove-warn"`：移除全部 stderr，但如果有发现，就记录警告
* `"warn"`, `"error"` 或 `"severe"`：如果发现任何标准错误，则将其记录在某个级别。

你也可以在单元格级别删除 stderr，使用 `remove-stderr` [cell 标签](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#cell-tags)，如下所示：

````md
```{code-cell} ipython3
:tags: [remove-stderr]

import sys
print("this is some stdout")
print("this is some stderr", file=sys.stderr)
```
````

生成：

```{code-cell} ipython3
:tags: [remove-stderr]

import sys
print("this is some stdout")
print("this is some stderr", file=sys.stderr)
```

### 处理产生标准输出的代码

与 stderr 类似，您可以使用 `remove-stdout` 标记在单元格级别删除 stdout，通过此标记

````md
```{code-cell} ipython3
:tags: [remove-stdout]

import sys
print("this is some stdout")
print("this is some stderr", file=sys.stderr)
```
````

产生以下：

```{code-cell} ipython3
:tags: [remove-stdout]

import sys
print("this is some stdout")
print("this is some stderr", file=sys.stderr)
```

## 执行统计数据

当笔记本被执行时，某些统计数据被 MyST-NB 存储在构建环境中。访问和可视化这些数据的最简单的方法是使用 `{nb-exec-table}` 指令。

:::{seealso}
[MyST-NB 文档](myst-nb:execute/statistics)，用于创建自己的指令来操作这些数据。
:::

简单的指令

````md
```{nb-exec-table}
```
````

输出：

```{nb-exec-table}
```
