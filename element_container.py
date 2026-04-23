from __future__ import annotations

from collections.abc import Callable
from pathlib import Path


class ElementContainerMeta(type):
    """Metaclass giving container classes a hierarchical ``str`` / ``repr``.

    A container subclass sets ``_element_type`` to a type (or tuple of types).
    Class attributes whose value matches ``_element_type`` are listed as
    *elements*; nested classes that also use this metaclass are recursed into.

    Override ``_ctnr_formatter`` / ``_element_formatter`` to customise rendering.
    """

    _element_type: type | tuple[type, ...]

    def __str__(cls) -> str:
        return cls._element_ctnr_str(cls)

    def __repr__(cls) -> str:
        return cls._element_ctnr_str(cls)

    @staticmethod
    def _element_ctnr_str(ctnr, indent: int = 0) -> str:
        header = indent * "\t" + ctnr._ctnr_formatter(ctnr) + "\n"
        elements = ctnr._elements_str(ctnr, indent + 1)
        nested = ""
        for key, val in vars(ctnr).items():
            if isinstance(val, ElementContainerMeta) and not key.startswith("__"):
                nested += ctnr._element_ctnr_str(val, indent + 1)
        return header + elements + nested

    @staticmethod
    def _elements_str(ctnr, indent: int = 1) -> str:
        out = ""
        for key, val in vars(ctnr).items():
            if isinstance(val, ctnr._element_type) and not key.startswith("__"):
                out += indent * "\t" + ctnr._element_formatter(key, val) + "\n"
        return out

    @staticmethod
    def _ctnr_formatter(ctnr) -> str:
        return f"{ctnr.__name__}: {ctnr.__doc__ or ''}"

    @staticmethod
    def _element_formatter(key, val) -> str:
        return f"{key}: {val!r}"


class PathContainer(metaclass=ElementContainerMeta):
    _element_type = Path

    @staticmethod
    def _element_formatter(key, val: Path) -> str:
        return f"{key}: {val.absolute()}"


class StrContainer(metaclass=ElementContainerMeta):
    _element_type = str


class IDContainer(metaclass=ElementContainerMeta):
    _element_type = (str, int)


class FunctionContainer(metaclass=ElementContainerMeta):
    _element_type = Callable
