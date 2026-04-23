# %%
from enum import EnumMeta, Enum, member


def enum_str(enum):
    return "\n".join(
        [
            str(
                (key, val if type(val.value) != CustomEnumMeta else enum_str(val.value))
            )
            for key, val in enum.__members__.items()
        ]
    )


class CustomEnumMeta(EnumMeta):
    def __repr__(self):
        print(self.__members__)
        # return "\n".join([f"{value}" for value in self.__members__.values()])
        return enum_str(self)


class Endpoints(Enum, metaclass=CustomEnumMeta):
    publication_half = (1, 2)
    publication_full = 3, 4
    word_half = 5, 6
    word_full = 5, 7

    @member
    class Inner(tuple, Enum, metaclass=CustomEnumMeta):
        a = (1, 2)
        b = (2, 3)
        c = (3, 4)


Endpoints

# %%


class EnumContainerMeta(EnumMeta):

    def __str__(self) -> str:
        return self._element_ctnr_str(self)

    def __repr__(self) -> str:
        return self._element_ctnr_str(self)

    @staticmethod
    def _element_ctnr_str(ctnr: EnumContainerMeta, indent: int = 0) -> str:
        return [
            (key, val if type(val.value) != CustomEnumMeta else repr(val))
            for key, val in ctnr.__members__.items()
        ]

    @staticmethod
    def _elements_str(ctnr: EnumContainerMeta, indent: int = 1) -> str:
        elements_str = ""
        for key, val in vars(ctnr).items():
            if isinstance(val, ctnr._element_type) and (not key.startswith("__")):
                elements_str += indent * "\t" + ctnr._element_formatter(key, val) + "\n"
        return elements_str

    @staticmethod
    def _ctnr_formatter(ctnr) -> str:
        """Default container string formatter."""
        return f"{ctnr.__name__}: {ctnr.__doc__  or ''}"

    @staticmethod
    def _element_formatter(key, val) -> str:
        """Default element string formatter."""
        return f"{key}: {repr(val)}"


# %%
