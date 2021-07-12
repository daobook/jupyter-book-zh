# 配置参考

您可以使用一个 **YAML配置文件(`_config.yml`)** 配置 Jupyter Book。
这个文件控制许多选项和特性标志。

这个页面是 `_config.yml` 的结构参考以及每个选项的默认值。
有关使用和配置特定功能的信息，请参见 **Topic Guides**。

:::{caution}
YAML 在处理某些类型的值时可能很棘手。例如，在 YAML 中使用字符串时，通常可以在字符串周围省略引号。但是，有些值如果周围没有字符串，则会被*转换*为布尔值。例如，`false`，`true`，`off` 等。此外，纯数字将被转换为 `float` 或 `int`，除非你在它们周围放置字符串。
:::

(config:defaults)=
## 默认配置项

下面是完整的默认配置文件。
任何你在自己的 `_config.yml` 中设置的东西将在它们被用于配置构建之前被合并到这些默认值中。

```{literalinclude} ../jupyter_book/default_config.yml
:language: yaml
:class: full-width
```
