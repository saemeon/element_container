# %%
from pathlib import Path

from element_container import (
    FunctionContainer,
    IDContainer,
    PathContainer,
    StrContainer,
)


class paths(PathContainer):
    """All project paths.

    Dot-access with IDE autocompletion, like a module tree of constants.
    """

    root = Path("project")
    readme = root / "README.md"

    class data(PathContainer):
        """Data subtree."""

        root = Path("project/data")
        raw = root / "raw"
        processed = root / "processed"

    class src(PathContainer):
        """Source subtree."""

        root = Path("project/src")
        main = root / "main.py"


class labels(StrContainer):
    """Human-readable labels."""

    user = "User"
    session = "Session"


class ids(IDContainer):
    """Mixed str / int identifiers."""

    alice = "u_alice"
    bob = 42


class ops(FunctionContainer):
    """Small inline callables."""

    square = lambda x: x**2  # noqa: E731
    double = lambda x: x * 2  # noqa: E731


# %%
print(paths)
print(labels)
print(ids)
print(ops)
