# cli-fun
Experimenting with Click and other fun examples!


## Usage

### No Install

Assuming that all dependent packages are installed, the package directory can be
run directly without installing this package. This can allow for fast
development without needing to install.

```bash
python -m cli_fun --help
```


### Install

It may be easier to install this package to gather all the dependencies. Include
the `-e` flag for development so package changes will reflect in the CLI without
reinstalling.

```bash
pip install -U .

# With editable flag for development
pip install -U -e .

f --help
```


#### Bash Completion

Getting bash completion will require installing the package first.

```bash
eval "$(_F_COMPLETE=source f)"
```
