# Hypothesis

```{raw} html
<script async="async" src="https://hypothes.is/embed.js"></script>
```

[Hypothesis](https://hypothes.is/) 是一个集中式的 web 服务，允许您对 web 上的任意网页进行评论和注释。它允许你的读者登录并评论你的书。

```{note}
Hypothesis 在本页被激活。你可以通过点击页面右上角的 `<` 按钮来看到网页覆盖。
```

## 激活 `Hypothesis`

你可以通过在 `_conf.yml` 文件中添加以下内容来 `Hypothesis`：

```yaml
html:
  comments:
    hypothesis: true
```

这将在您的文档中添加一个 [Hypothesis 覆盖层](https://web.hypothes.is/)。这个扩展只是激活你的 Sphinx 网站上的 Hypothesis JavaScript 包。

当您构建文档时，您将看到屏幕右侧的 Hypothesis 覆盖层。
