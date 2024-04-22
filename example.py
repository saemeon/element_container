# %%
from element_container import *


class IdContainer(StrContainer):
    a = "str"
    b = "asdlfkjasdf"
    c = 29023
    d = True
    e = 3.2

    class funcontainer(FunctionContainer):
        a = lambda x: x**2

    class ze(StrContainer):
        key = "adlsfkj"
        hash = "lkdfja"
        fdate = "kdfjalsdfj"

    class P(PathContainer):
        """documentation P paths."""

        root = Path("dir")
        c = root / "c"
        d = root / "d"


class D(PathContainer):
    """documentation D doc"""

    c = Path("d/e")
    d = Path("e/f")


class paths1(PathContainer):
    """Container holding all paths of the project.

    The container allows autocompletion by dotaccess similar to python package and module access.
    It contains both "raw" paths and nested path containers.
    """

    a = Path("b/c")
    """a doc"""
    b = Path("c/d")
    """b doc """

    class P(PathContainer):
        """documentation P paths."""

        root = Path("dir")
        c = root / "c"
        d = root / "d"

    class O(PathContainer):
        """`O:` netdrive"""

        c = Path("d/e")
        d = Path("e/f")

        class C(PathContainer):
            c = Path("d/e")
            d = Path("e/f")

        D = D


# %%
paths1
# %%
