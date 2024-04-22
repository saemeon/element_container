# %%
from __future__ import annotations

from pathlib import Path
from typing import Callable, Union


class ElementContainerMeta(type):
    _element_type: type = NotImplemented

    def __str__(self) -> str:
        return self._element_ctnr_str(self)

    def __repr__(self) -> str:
        return self._element_ctnr_str(self)

    @staticmethod
    def _element_ctnr_str(ctnr: ElementContainerMeta, indent: int = 0) -> str:
        # header = indent * "\t" + f"{ctnr.__name__}: {ctnr.__doc__  or ''}" +"\n"
        header = indent * "\t" + ctnr._ctnr_formatter(ctnr) + "\n"
        elements_str = ctnr._elements_str(ctnr, indent + 1)
        nested_ctnrs_str = ""
        for key, val in vars(ctnr).items():
            if isinstance(val, ElementContainerMeta) and (not key.startswith("__")):
                nested_ctnrs_str += ctnr._element_ctnr_str(val, indent + 1)
        return header + elements_str + nested_ctnrs_str

    @staticmethod
    def _elements_str(ctnr: ElementContainerMeta, indent: int = 1) -> str:
        elements_str = ""
        for key, val in vars(ctnr).items():
            if isinstance(val, ctnr._element_type) and (not key.startswith("__")):
                elements_str += indent * "\t" + ctnr._element_formatter(key, val) + "\n"
                # elements_str += indent * "\t" + f"{key}: {repr(val)}" + "\n"
        return elements_str

    @staticmethod
    def _ctnr_formatter(ctnr) -> str:
        """Default container string formatter."""
        return f"{ctnr.__name__}: {ctnr.__doc__  or ''}"

    @staticmethod
    def _element_formatter(key, val) -> str:
        """Default element string formatter."""
        return f"{key}: {repr(val)}"


class PathContainer(metaclass=ElementContainerMeta):
    _element_type = Path

    @staticmethod
    def _ctnr_formatter(ctnr) -> str:
        """Default container string formatter."""
        return f"adfa{ctnr.__name__}: {ctnr.__doc__  or ''}"

    @staticmethod
    def _element_formatter(key, val) -> str:
        return f"{key}: {val.absolute()}"


class StrContainer(metaclass=ElementContainerMeta):
    _element_type: type = str


class IDContainer(metaclass=ElementContainerMeta):
    _element_type = Union[
        str,
        int,
    ]


class FunctionContainer(metaclass=ElementContainerMeta):
    _element_type = Callable
