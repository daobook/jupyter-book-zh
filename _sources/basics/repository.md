# 将您的书连接到代码存储库

有很多方法可以将图书内容与公共存储库中的源文件连接起来。下面介绍一些选择。

(source-repository-button)=
## 添加源存储库按钮

这里有一组按钮，您可以使用它们链接回源存储库。这允许用户浏览存储库，或采取建议编辑或打开问题等操作。在每种情况下，它们都需要设置以下配置：
There is a collection of buttons that you can use to link back to your source

```yaml
repository:
  url: https://github.com/{your-book-url}
```

### 给存储库添加一个链接

要添加到存储库的链接，请添加以下配置：

```yaml
repository:
  url: https://github.com/{your-book-url}
html:
  use_repository_button: true
```

### 添加一个按钮来打开议题

要添加一个按钮来打开关于当前页面的议题，使用以下配置：

```yaml
repository:
  url: https://github.com/{your-book-url}
html:
  use_issues_button: true
```

### 添加一个按钮来建议编辑

您可以向每个页面添加一个按钮，允许用户直接编辑页面文本，并提交一个 pull 请求来更新文档。要包含此按钮，请使用以下配置：

```yaml
repository:
  url: https://github.com/{your-book-url}
  path_to_book: path/to/your/book  # An optional path to your book, defaults to repo root
  branch: yourbranch  # An optional branch, defaults to `master`
html:
  use_edit_page_button: true
```
