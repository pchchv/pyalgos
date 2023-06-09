"""
Conversion of volume units.

WIKI REFERENCES:
    https://en.wikipedia.org/wiki/Cubic_metre
    https://en.wikipedia.org/wiki/Litre
    https://en.wiktionary.org/wiki/kilolitre
    https://en.wikipedia.org/wiki/Gallon
    https://en.wikipedia.org/wiki/Cubic_yard
    https://en.wikipedia.org/wiki/Cubic_foot
    https://en.wikipedia.org/wiki/Cup_(unit)
"""

from collections import namedtuple

from_to = namedtuple("from_to", "from_ to")

METRIC_CONVERSION = {
    "cubicmeter": from_to(1, 1),
    "litre": from_to(0.001, 1000),
    "kilolitre": from_to(1, 1),
    "gallon": from_to(0.00454, 264.172),
    "cubicyard": from_to(0.76455, 1.30795),
    "cubicfoot": from_to(0.028, 35.3147),
    "cup": from_to(0.000236588, 4226.75),
}


def volume_conversion(value: float, from_type: str, to_type: str) -> float:
    """
    Conversion between volume units.
    >>> volume_conversion(4, "cubicmeter", "litre")
    4000
    >>> volume_conversion(1, "litre", "gallon")
    0.264172
    >>> volume_conversion(1, "kilolitre", "cubicmeter")
    1
    >>> volume_conversion(3, "gallon", "cubicyard")
    0.017814279
    >>> volume_conversion(2, "cubicyard", "litre")
    1529.1
    >>> volume_conversion(4, "cubicfoot", "cup")
    473.396
    >>> volume_conversion(1, "cup", "kilolitre")
    0.000236588
    >>> volume_conversion(4, "wrongUnit", "litre")
    Traceback (most recent call last):
        ...
    ValueError: Invalid 'from_type' value: 'wrongUnit'  Supported values are:
    cubicmeter, litre, kilolitre, gallon, cubicyard, cubicfoot, cup
    """
    if from_type not in METRIC_CONVERSION:
        raise ValueError(
            f"Invalid 'from_type' value: \
                {from_type!r}  Supported values are:\n"
            + ", ".join(METRIC_CONVERSION)
        )
    if to_type not in METRIC_CONVERSION:
        raise ValueError(
            f"Invalid 'to_type' value: {to_type!r}.  Supported values are:\n"
            + ", ".join(METRIC_CONVERSION)
        )
    return value * \
        METRIC_CONVERSION[from_type].from_ * METRIC_CONVERSION[to_type].to


if __name__ == "__main__":
    import doctest

    doctest.testmod()
