# element_container

A tiny metaclass that turns a Python class into a pretty-printed, nested
namespace of constants.

## Idea

You often want a dot-accessible registry — project paths, string ids, small
callables — with IDE autocompletion and docstrings that live next to the
values. Classes already give you dot-access, nesting, and docstrings.
`element_container` just teaches the class to print itself as a readable tree.

- Subclass one of the container types
  (`PathContainer`, `StrContainer`, `IDContainer`, `FunctionContainer`)
  — or define your own with `ElementContainerMeta`.
- Set class attributes. Values whose type matches the container's
  `_element_type` are rendered as *leaves*; nested container classes are
  recursed into.
- `print(MyClass)` walks the tree. No instances required.

## Example

```python
from pathlib import Path
from element_container import PathContainer


class paths(PathContainer):
    """All project paths."""

    root = Path("project")
    readme = root / "README.md"

    class data(PathContainer):
        """Data subtree."""

        root = Path("project/data")
        raw = root / "raw"
        processed = root / "processed"


print(paths)
```

Output:

```text
paths: All project paths.
    root: /abs/.../project
    readme: /abs/.../project/README.md
    data: Data subtree.
        root: /abs/.../project/data
        raw: /abs/.../project/data/raw
        processed: /abs/.../project/data/processed
```

Access values the normal way:

```python
paths.readme          # Path('project/README.md')
paths.data.raw        # Path('project/data/raw')
```

See [example.py](example.py) for `StrContainer`, `IDContainer`, and
`FunctionContainer` demos.

## Built-in containers

- `PathContainer` — `pathlib.Path` values, formatted as absolute paths.
- `StrContainer` — `str` values.
- `IDContainer` — mixed `str` / `int` ids.
- `FunctionContainer` — callables.

## Custom containers

Pick your own leaf type:

```python
from element_container import ElementContainerMeta


class FloatContainer(metaclass=ElementContainerMeta):
    _element_type = float
```

Override `_ctnr_formatter(ctnr)` or `_element_formatter(key, val)` to
customise the rendered output.
