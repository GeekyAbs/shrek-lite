# shrek lite

A simple expense tracker CLI.

## Install

```
cd shrek-lite
uv venv
uv pip install -e .
uv tool install .
```

## Usage

Add an expense (you'll be prompted to pick a category by number):

```
shrek add 100
```

Show total expenses (overall and by category):

```
shrek total
```

## Uninstall (global)

```
uv tool uninstall shrek-lite
```
