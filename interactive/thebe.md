---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(launch:thebe)=
# 使您的代码单元格可执行

这一节描述了如何为你的书带来交互性。这允许用户运行代码并查看输出，而无需离开页面。交互性是由运行在公共[**MyBinder**](https://mybinder.org) 服务上的内核提供的。

例如，单击此页上方的 {fa}`rocket` --> {guilabel}`Live Code` 按钮，并运行下面的代码。

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
plt.ion()

x = np.arange(500)
y = np.random.randn(500)

fig, ax = plt.subplots()
ax.scatter(x, y, c=y, s=x)
```

:::{warning}
这是一个实验性的特性，在未来可能会发生变化或意想不到的效果。
:::

## 激活 Thebe

为了使您的内容具有交互性，而不要求读者离开当前页面，您可以使用一个名为 [Thebe](https://github.com/executablebooks/thebe) 的项目。这为您提供了一个 {guilabel}`Live Code` 按钮，单击该按钮时，将把每个代码单元格转换为可以编辑的交互式单元格。它还向每个单元添加一个 "run" 按钮，并连接到在云中运行的 Binder 内核。

要将 Thebe 按钮添加到你的 Jupyter Book 页面，采取以下步骤：

1. 首先，[添加通用启动按钮配置](launchbuttons/configuration)。这使得 `thebe/` 可以为您的内容使用正确的环境和文件路径。
2. 激活 Thebe 集成与以下配置：

   ```yaml
   launch_buttons:
     thebe                  : true
   ```

## 配置 Thebe

此外，您还可以配置 Binder 设置，这些设置用于为 Thebe 提供运行代码的内核。它们使用与上面描述的 BinderHub 交互按钮相同的配置字段。有关如何做到这一点的信息，请参见 [BinderHub 启动按钮文档](launchbuttons/binder)。

+++

## 在初始化 Thebe 时预执行单元格

有时，您希望在请求内核时立即运行一些代码单元格。这可能是您随后对用户隐藏的代码，以便缩小用户与之交互的焦点。这是可以通过使用 Jupyter Notebook 的**单元格标签**。

将标签 {guilabel}`thebe-init` 添加到任何代码单元格将导致 Thebe 在接收到内核后运行这个单元格。任何后续 Thebe 单元格都可以访问相同的环境(例如，在初始化单元格中进行的任何模块导入)。

然后，您可以将其与诸如 {guilabel}`hide-input` 之类的东西配对，以便运行用户不会立即看到的初始化代码。例如，下面我们将初始化隐藏单元格中的一个变量，然后告诉另一个单元格打印该变量的输出。

```{code-cell} ipython3
:tags: [hide-input, thebe-init]

my_hidden_variable = 'wow, it worked!'
```

```{code-cell} ipython3
# The variable for this is defined in the cell above!
print(my_hidden_variable)
```
