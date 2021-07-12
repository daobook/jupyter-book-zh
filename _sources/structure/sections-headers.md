(toc/structure)=
# 标题和章节如何映射到书的结构

Jupyter Book 在底层使用 {term}`Sphinx` 文档引擎，它以特定的方式表示图书的结构。`_toc.yml` 结构的不同选择和你页面中的标题结构将会对你的书的整体结构产生不同的结果。这里有一些一般的技巧和最佳实践。

```{note}
当您为[图书的章节编号](toc/numbering)或[通过 Latex 构建图书的 PDF 文件](pdf:latex)时，这一点尤为重要。
```

**chapters 在你的书的层次结构的顶部**。你的 `_toc.yml` 的顶层包含一个 chapters 列表。每个文件的标题将是章的标题。

**headers 映射到 sections**。 Jupyter Book 将你的书解释为一组章节，并根据 `_toc.yml` 的层次结构决定这些章节应该如何嵌套和标题的层次结构。在一个文件中，它发现的第一个 `##` 头将定义文件中最顶部的部分，而下面的任何随后的 `###` 头将成为子部分（直到遇到另一个 `##` section）。如果页面嵌套在另一个页面下（见下文），则此行为略有不同。 

**嵌套文件在其父文件的最后一部分下面定义部分**。如果指定嵌套在文件下的 sections（使用 `sections:` 关键字），那么这些节将从父页最后一个标题的下面开始。

例如，如果你的 `_toc.yml` 文件是这样的

```yaml
format: jb-book
root: myintro
chapters:
- file: chapter1
  sections:
  - file: chapter1section
```

然后，`chapter1section` 将在 `chapter1` 的章节下开始。`chapter1section` 的任何标题都将被视为 `chapter1` 中的“下一个标题-更深的”章节。

换句话说，如果 `chapter1` 和 `chapter1section` 是这样的：

````{panels}
`chapter1.md`
^^^^^^^^^^^^^
```md
# Chapter 1 title

## Chapter 1 second header
```
---
`chapter1section.md`
^^^^^^^^^^^^^^^^^^^^

```md
# Chapter 1 section title

## Chapter 1 section second header
```
````
那么你的书就会这样对待他们：

```md
# Chapter 1 title

## Chapter 1 second header

### Chapter 1 section title

#### Chapter 1 section second header
```

然而,如果 `chapter1.md` 有一个额外的第三级 header 文件，像这样：

````{panels}
`chapter1.md`
^^^^^^^^^^^^^
```md
# Chapter 1 title

## Chapter 1 second header

### Chapter 1 third header
```
---
`chapter1section.md`
^^^^^^^^^^^^^^^^^^^^

```md
# Chapter 1 section title

## Chapter 1 section second header
```
````

那么你的书就会这样对待他们：

```md
# Chapter 1 title

## Chapter 1 second header

### Chapter 1 third header

#### Chapter 1 section title

##### Chapter 1 section second header
```

在设计文件结构时要记住这一点。

:::{tip}
一个好的经验法则是采用以下两种方法中的一种：

1. **不要在你的介绍页上加上标题**。这本书的序言和每一章的介绍都是如此。相反，将标题留给包含更多内容的页面，并在使用标题的地方使用**粗体文本**。
   Instead, leave the headers to pages that have more content in them, and use
   **bolded text** where you would otherwise use headers.
2. **使用扁平的文件列表，而不是嵌套的文件**。这样，section 层次结构只在每个 section 中的单个文件中定义。然而，这意味着通常您将拥有更长的文件。
:::
