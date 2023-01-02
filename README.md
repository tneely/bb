# `bb`: biology boilerplate

This repository provides boilerplate for computational biology projects. It provides quick and easy setup of consistent, organized, and reproducible development environments.

## Supported Languages

`bb` currently supports the following programming languages:

- Python

## Project Structure

### Data

`bb` is set up to promote healthy data hygiene.

Raw data should be stored in the `./data/raw` directory. This is for things like FASTQ files which contain your raw, unprocessed data.

Intermediate data, such as aligned BAM files, should be stored in `./data/interim`. This is for data you don't care about in the end, but need to compute your final results.

Your final results should be stored in `./data/processed`. This is for things like VCF files: your final output data or the end result of your project.

By default, data is not committed to git. Working with large files under source control can be cumbersome, but if you would like it tracked you can remove the `data/` entry from the top of the [.gitignore](.gitignore) file.

### Code

Code should be divided between exploratory notebooks and production ready pipeline code.

Notebooks are great for exploring your data and prototyping your pipeline. Your notebook code should be kept under the `./notebooks` directory.

Production ready or pipeline code is the for more streamlined processing of your data and should be kept in the `./src` directory.

## Getting Started

### Prerequisites

Before using `bb`, please install the following packages.

#### Pyenv

[Pyenv](https://github.com/pyenv/pyenv) is used to manage and switch between Python versions. We use it here ensure your project is always run using the same Python version.

To get started, install Pyenv with the following command:

```shell
curl https://pyenv.run | bash
```

Once installed, add the following to your `~/.bashrc` or `~/.zshrc` file:

```shell
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

After sourcing your `~/.*rc` file, install a recent version of Python and set it as your global default version:

```shell
pyenv install 3.11
pyenv global 3.11
```

#### pipx

[pipx](https://github.com/pypa/pipx/) is a tool to help you install global Python tools. pipx is like pip, but adds also creates an isolated environment for each application and its associated packages to run in. We will use it later to install Poetry.

You can install it using `pip`:

```shell
pip install pipx
# Make sure pipx is available on your path
pipx ensurepath
```

#### Poetry

[Poetry](https://github.com/python-poetry/poetry) helps us manage our project's Python packages in a deterministic way so that your code stays reproducible across users and devices.

You can install it using `pipx`:

```shell
pipx install poetry
```

### Installation

This repository is intended to be used as a template for standalone projects. If you have the GitHub CLI installed, you can clone this repository using the following:

```shell
gh repo create <new-repo-name> --template="tneely/bb"
```

Otherwise, navigate the GitHub UI to [use this template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template#creating-a-repository-from-a-template).

To see how to work with your new project, check out [DEVELOPMENT.md](./DEVELOPMENT.md).
