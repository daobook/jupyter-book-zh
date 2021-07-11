# from pathlib import Path

import jsonschema
import pytest

from jupyter_book.cli.main import sphinx
from jupyter_book.config import get_final_config, validate_yaml

pytest_plugins = "pytester"


@pytest.mark.parametrize(
    "user_config",
    [
        {},
        {"title": "hallo"},
        {"html": {"extra_footer": ""}},
        {"execute": {"execute_notebooks": "cache"}},
        {"parse": {"myst_enable_extensions": ["linkify"]}},
        {"latex": {"latex_documents": {"targetname": "book.tex", "title": "other"}}},
        {"launch_buttons": {"binderhub_url": "other"}},
        {"repository": {"url": "other"}},
        {"exclude_patterns": ["new"]},
        {
            "sphinx": {
                "extra_extensions": ["other"],
                "local_extensions": {"helloworld": "./ext"},
                "config": {
                    "html_theme_options": {
                        "launch_buttons": {"binderhub_url": "other"}
                    },
                    "html_theme": "other",
                    "new": "value",
                },
            }
        },
    ],
    ids=[
        "empty",
        "title",
        "html.extra_footer",
        "execute.method",
        "extended_syntax",
        "latex_doc",
        "launch_buttons",
        "repository",
        "exclude_patterns",
        "sphinx",
    ],
)
def test_get_final_config(user_config, data_regression):
    cli_config = {"latex_individualpages": False}
    final_config, metadata = get_final_config(
        user_yaml=user_config,
        cli_config=cli_config,
        validate=True,
        raise_on_invalid=True,
    )
    data_regression.check(
        {"_user_config": user_config, "final": final_config, "metadata": metadata}
    )


def test_validate_yaml():
    with pytest.raises(jsonschema.ValidationError):
        validate_yaml({"title": 1}, raise_on_errors=True)
    assert "Warning" in validate_yaml({"title": 1}, raise_on_errors=False)
    assert validate_yaml({"title": ""}, raise_on_errors=False) is None


def test_config_sphinx_command_only_build_toc_files(
    cli, temp_with_override, file_regression
):
    temp_with_override.joinpath("_config.yml").write_text(
        "only_build_toc_files: True\n", encoding="utf8"
    )
    temp_with_override.joinpath("_config.yml").write_text(
        "exclude_patterns: [test_config/*]\n", encoding="utf8"
    )

    temp_with_override.joinpath("_toc.yml").write_text("root: intro\n", encoding="utf8")
    result = cli.invoke(sphinx, temp_with_override.as_posix())

    assert result.exit_code == 0, result.exception
    # remove global_toc which is path dependent
    output = "\n".join(
        line
        for line in result.output.splitlines()
        if not line.startswith("external_toc_path")
    )

    file_regression.check(output, encoding="utf8")


def test_config_sphinx_command(cli, temp_with_override, file_regression):
    temp_with_override.joinpath("_config.yml").write_text(
        "title: test\n", encoding="utf8"
    )
    temp_with_override.joinpath("_toc.yml").write_text("root: intro\n", encoding="utf8")
    result = cli.invoke(sphinx, temp_with_override.as_posix())
    assert result.exit_code == 0, result.exception
    # remove global_toc which is path dependent
    output = "\n".join(
        line
        for line in result.output.splitlines()
        if not line.startswith("external_toc_path")
    )
    file_regression.check(output, encoding="utf8")


# TODO sphinx-external-toc now handles appending to exclude_patterns
# but we may want to add similar tests there, checking the output of exclude_patterns

# @pytest.mark.parametrize(
#     "toc_file, filename",
#     [("p.md", "p.md"), ("p", "p.md"), ("[]p", "[]p.md"), ("[t]p.md", "[t]p.md")],
# )
# def test_only_build_toc_files(testdir, toc_file, filename):
#     cli_config = {"latex_individualpages": False}
#     toc = Path("toc.yml")
#     toc.write_text(f"- file: '{toc_file}'\n")
#     Path(filename).write_text("")
#     Path("exclude.md").write_text("")
#     user_config = {"only_build_toc_files": True}

#     final_config, metadata = get_final_config(
#         user_yaml=user_config,
#         cli_config=cli_config,
#         validate=True,
#         raise_on_invalid=True,
#     )

#     assert "exclude.md" in final_config["exclude_patterns"]
#     assert filename not in final_config["exclude_patterns"]


# def test_only_build_toc_files_with_exclude_patterns(testdir):
#     cli_config = {"latex_individualpages": False}
#     toc = Path("toc.yml")
#     toc.write_text("- file: landing\n")
#     Path("landing.md").write_text("")
#     Path("exclude.md").write_text("")
#     user_config = {
#         "only_build_toc_files": True,
#         "exclude_patterns": ["my/*", "patterns"],
#     }

#     final_config, metadata = get_final_config(
#         user_yaml=user_config,
#         cli_config=cli_config,
#         validate=True,
#         raise_on_invalid=True,
#     )

#     assert "exclude.md" in final_config["exclude_patterns"]
#     assert "my/*" in final_config["exclude_patterns"]
#     assert "patterns" in final_config["exclude_patterns"]
#     assert "landing.md" not in final_config["exclude_patterns"]


# def test_only_build_toc_files_non_default_source_dir(testdir):
#     cli_config = {"latex_individualpages": False}
#     toc = Path("toc.yml")
#     toc.write_text("- file: landing\n")
#     sourcedir = Path("s")
#     subdir = sourcedir / "subdir"
#     subdir.mkdir(parents=True)
#     Path(sourcedir / "landing.md").write_text("")
#     Path(sourcedir / "exclude.md").write_text("")
#     Path(subdir / "sub.md").write_text("")
#     user_config = {"only_build_toc_files": True}

#     final_config, metadata = get_final_config(
#         user_yaml=user_config,
#         cli_config=cli_config,
#         validate=True,
#         raise_on_invalid=True,
#         sourcedir=sourcedir,
#     )

#     assert "exclude.md" in final_config["exclude_patterns"]
#     assert "subdir/sub.md" in final_config["exclude_patterns"]
#     assert "landing.md" not in final_config["exclude_patterns"]


# def test_only_build_toc_files_missing_toc(testdir):
#     cli_config = {"latex_individualpages": False}
#     user_config = {"only_build_toc_files": True}

#     with pytest.raises(ValueError, match=r".*you must have a toc.*"):
#         get_final_config(
#             user_yaml=user_config,
#             cli_config=cli_config,
#             validate=True,
#             raise_on_invalid=True,
#         )


def test_get_final_config_custom_myst_extensions(data_regression):
    cli_config = {"latex_individualpages": False}
    user_config = {"parse": {"myst_extra_extensions": ["linkify"]}}
    final_config, metadata = get_final_config(
        user_yaml=user_config,
        cli_config=cli_config,
        validate=True,
        raise_on_invalid=True,
    )
    data_regression.check(
        {"_user_config": user_config, "final": final_config, "metadata": metadata}
    )


def test_get_final_config_bibtex(data_regression):
    cli_config = {"latex_individualpages": False}
    user_config = {"bibtex_bibfiles": ["tmp.bib"]}
    final_config, metadata = get_final_config(
        user_yaml=user_config,
        cli_config=cli_config,
        validate=True,
        raise_on_invalid=True,
    )
    assert "sphinxcontrib.bibtex" in final_config["extensions"]
