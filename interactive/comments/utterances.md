# Utterances

Utterances 是一个基于 GitHub Issues 构建的评论引擎。它在你的页面中嵌入了一个评论框，用户(拥有 GitHub 帐户)可以用它来提问。这些将成为你选择的仓库中 GitHub issue 中的评论。

```{note}
Utterances 在这个页面上被激活。您可以在本页内容的底部看到评论框。点击 "log in" 按钮，您将能够发表评论!
```

## 激活 `utterances`

您可以通过在 `_conf.yml` 文件中添加以下内容来激活 `utterances`：

```yaml
html:
  comments:
    utterances:
      repo: "github-org/github-repo"
```

注意，当你在本地预览你的书时，`utterances` UI 不会显示，它必须在网络上的某个地方运行。

## 配置 `utterances`

您可以为 utterances 传递可选的额外配置。你可以通过在配置中在 `repo:` 旁边提供 `key:val` 对来做到这一点。请参阅[您的选项的 `utterances` 文档](https://utteranc.es/#configuration)。

当您构建文档时，页面底部将有一个评论框。如果读者通过 GitHub 登录，他们将能够发布评论，这些评论将映射到 GitHub 存储库中的 issue。

% This HTML activates utterances only on this page
```{raw} html
<script
   type="text/javascript"
   src="https://utteranc.es/client.js"
   async="async"
   repo="executablebooks/jupyter-book"
   issue-term="pathname"
   theme="github-light"
   label="💬 comment"
   crossorigin="anonymous"
/>
```
