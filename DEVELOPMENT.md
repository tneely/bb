# Developing with `bb`

## Writing Code

Generally, we expect code to be run from the command line. This boilerplate template uses [Click](https://click.palletsprojects.com) to create easy, composable command line interfaces. From [cli.py](src/cli.py), you can define new CLI arguments and options using the `@click` decorators.

## Running Code

To run your script simply use `poetry run python your_script.py`. Likewise if you have command line tools such as pytest or black you can run them using `poetry run pytest`.

This boilerplate template provides a simple entrypoint script to run your project. To get started, use `poetry run main`. This calls into the `main` function of [**init**.py](src/__init__.py), which will then invoke the `entry` function of [cli.py](src/entry.py).

```shell
$ poetry run main --name Taylor
Hello, Taylor!
```

## Installing Packages

Packages are managed with [Poetry](https://github.com/python-poetry/poetry). To install all packages in your project, run `poetry install`. Otherwise to add a new package, use `poetry add <package-name>`.

### Updating Packages

Poetry uses a lock file to ensure consistent versioning across systems and builds. To update to the latest versions, within the constraints of your `pyproject.toml` file, run `poetry update`.

If you want to use a later version than specified, in `pyproject.toml`, simply update the dependency in the file and use `poetry install` to install and update those dependencies.
