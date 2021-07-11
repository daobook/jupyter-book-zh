(advanced/sphinx-config)=
# Advanced Sphinx usage

Jupyter Book uses the excellent documentation tool [Sphinx](http://www.sphinx-doc.org/)
to build your book and manage citations, cross-references, and extensibility.

While Jupyter Book comes pre-configured with several Sphinx extensions,
power-users may wish to add their own extensions and configuration.
This page describes how to do so.

:::{warning}
Adding your own Sphinx configuration and extensions may cause Jupyter Book to behave
unpredictably.
Use at your own risk!
:::

## Custom Sphinx extensions

To enable your own Sphinx extensions when building a Jupyter Book, use the following
configuration in your `_config.yml` file:

```yaml
sphinx:
  extra_extensions:
   - extension1
   - extension2
```

Any extensions that are listed will be appended to the list of Sphinx extensions at
build time.

:::{note}
Make sure that you have your extension installed on your machine, or Sphinx won't know
how to build the extensions.
:::

### An example: `sphinx-inline-tabs`

By default, Jupyter Book ships with [tabs via `sphinx-panels`](content:tabs).
There are other packages for tabs in the Sphinx ecosystem with different functionality.
One-such package is [`sphinx-inline-tabs`](https://sphinx-inline-tabs.readthedocs.io/en/latest/), which allows for _syncronized tabs_ in case you'd like your tabs to shift across the page at the same time.

`sphinx-inline-tabs` is not included with Jupyter Book by default, but we can activate it with Jupyter Book like so:

* **Install `sphinx-inline-tabs`**. Here's the command to do so:

  ```bash
  pip install sphinx-inline-tabs
  ```

* **Add `sphinx-inline-tabs` content to your book**. Here's an example with MyST Markdown:

  `````md
  First two tabs showing off defining a function.

  ````{tab} Python
  ```python
  def main():
      return
  ```
  ````
  ````{tab} C++
  ```c++
  int main(const int argc, const char **argv) {
    return 0;
  }
  ```
  ````

  Second two tabs showing off printing.

  ````{tab} Python
  ```python
  print("Hello World!")
  ```
  ````

  ````{tab} C++
  ```c++
  #include <iostream>

  int main() {
    std::cout << "Hello World!" << std::endl;
  }
  ```
  ````
  `````

* **Activate `sphinx-inline-tabs` in `_config.yml`**.
  [The `sphinx-inline-tabs` documentation](https://sphinx-inline-tabs.readthedocs.io/en/latest/) says we activate it in Sphinx by adding `extensions = ["sphinx_inline_tabs"]`, so we'll add it to our Jupyter Book like so:

  ```yaml
  sphinx:
    extra_extensions:
    - sphinx_inline_tabs
  ```

Now, Jupyter Book will know how to interpret the `{tab}` directive
(and any other directives that `sphinx-inline-tabs` supports).

For example, here is a rendered version of the tab code pasted above:

First two tabs showing off defining a function.

````{tab} Python
```python
def main():
    return
```
````
````{tab} C++
```c++
int main(const int argc, const char **argv) {
  return 0;
}
```
````

Second two tabs showing off printing.

````{tab} Python
```python
print("Hello World!")
```
````

````{tab} C++
```c++
#include <iostream>

int main() {
  std::cout << "Hello World!" << std::endl;
}
```
````

(config:sphinx:local_extensions)=
### Local Sphinx Extensions

[Sphinx is able to use local extensions](https://www.sphinx-doc.org/en/master/development/tutorials/helloworld.html#using-the-extension) by adding additional directories to the [Python path](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH). You can use local extensions by
specifying them as `local_extensions` in the `_config.yml` file.

To add a local extension that requires a path, use:

```yaml
sphinx:
  local_extensions:
    <name>: <path>
```

This will **append to the list of extensions already loaded by Jupyter Book** and update the `sys.path` so
the local extension can be found.

(sphinx:configuration)=
## Manual Sphinx configuration

You may also directly override the key-value pairs that Sphinx normally has
you configure in `conf.py`. To do so, use the following section of `_config.yml`:

```yaml
sphinx:
  config:
    key1: value1
    key2: value2
```

:::{warning}
Any options set in this section will **override** default configurations set by Jupyter Book.
Use at your own risk!
:::

:::{tip}
If you wish to inspect a `conf.py` representation of the generated configuration,
which Jupyter Book will pass to Sphinx, you can run from the command-line:

```bash
jb config sphinx mybookname/
```

:::

### Fine control of parsing and execution

As discussed in [the components of Jupyter Book](intro/jupyter-book-components), two of the main components of Jupyter Book are Sphinx extensions;
MyST-Parser for Markdown parsing, and MyST-NB for notebook execution and output rendering.

These two extensions are highly customizable *via* Sphinx configuration.
Some of their configuration is already exposed in the `_config.yml`, but you can also directly set configuration, see:

* the [MyST-Parser configuration options](myst-parser:sphinx/config-options)
* the [MyST-NB configuration options](myst-nb:start/config-options)

(sphinx/tex-macros)=
### Defining TeX macros

You can add LaTeX macros for the whole book by defining them under the `Macros` option of the `TeX` block. For example, the following two macros have been pre-defined in the Sphinx configuration

```yaml
sphinx:
  config:
    mathjax_config:
      TeX:
        Macros:
          "N": "\\mathbb{N}"
          "floor": ["\\lfloor#1\\rfloor", 1]
          "bmat" : ["\\left[\\begin{array}"]
          "emat" : ["\\end{array}\\right]"]
```

You can also define TeX macros for a specific file by introducing them at the beginning of the file under a `math` directive. For example

````md
```{math}

\newcommand\N{\mathbb{N}}
\newcommand\floor[1]{\lfloor#1\rfloor}
\newcommand{\bmat}{\left[\begin{array}}
\newcommand{\emat}{\end{array}\right]}
```
````

The commands can be used inside a `math` directive, `$$`, or in-line `$`. For example,

```md
$$
A = \bmat{} 1 & 1 \\ 2 & 1\\ 3 & 2 \emat{},\ b=\bmat{} 2\\ 3 \\ 4\emat{},\ \gamma = 0.5
$$
```

will be rendered as:

```{only} html
$$
A = \bmat{} 1 & 1 \\ 2 & 1\\ 3 & 2 \emat{},\ b=\bmat{} 2\\ 3 \\ 4\emat{},\ \gamma = 0.5
$$
```

:::{seealso}
[How MyST-Parser works with MathJax](myst-parser:syntax/mathjax),
and the section on [math and equations](myst-content/math).
:::

:::{important}
To have "bare" LaTeX rendered in HTML, enable the `amsmath` extension in your `_config.yml`:

```yaml
parse:
  myst_enable_extensions:
    # don't forget to list any other extensions you want enabled,
    # including those that are enabled by default!
    - amsmath
```

Then you can include:

```latex
\begin{equation}
  \int_0^\infty \frac{x^3}{e^x-1}\,dx = \frac{\pi^4}{15}
\end{equation}
```

which renders as

\begin{equation}
  \int_0^\infty \frac{x^3}{e^x-1}\,dx = \frac{\pi^4}{15}
\end{equation}

:::

## Enable a custom Sphinx builder from the CLI

You can initiate builds for a custom builder using:

```bash
jb build <project> --builder=custom --custom-builder=<builder-name>
```

Advanced `sphinx` users may find an extension that builds a different type of output from
the Sphinx AST such as [sphinx-tojupyter](https://github.com/QuantEcon/sphinx-tojupyter)
which is an extension for building notebooks that only includes `basic` markdown.

```{warning}
[sphinx-tojupyter](https://github.com/QuantEcon/sphinx-tojupyter) will be deprecated once
`myst` syntax rendering support is available in jupyter notebooks.
```

You can enable the `jupyter` builder by adding it to the `_config.yml`

```
sphinx:
  extra_extensions: [sphinx_tojupyter]
```

and using the `custom` option via `jupyter-book`:

```bash
jb build <project> --builder=custom --custom-builder=jupyter
```

```{warning}
**Developers:** When using other output targets, the package will need to support specifying the
`mime` type priority for `myst_nb` compatibility.

See [this code](https://github.com/QuantEcon/sphinx-tojupyter/blob/ef85226e5e3e30903b62ddda24d8a32d36687944/sphinx_tojupyter/__init__.py#L124) for
further details
```
