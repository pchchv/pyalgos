""" Convert between different units of temperature """


def celsius_to_fahrenheit(celsius: float, ndigits: int = 2) -> float:
    """
    Convert a given value from Celsius to Fahrenheit and
    round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Celsius
    Wikipedia reference: https://en.wikipedia.org/wiki/Fahrenheit
    >>> celsius_to_fahrenheit(273.354, 3)
    524.037
    >>> celsius_to_fahrenheit(273.354, 0)
    524.0
    >>> celsius_to_fahrenheit(-40.0)
    -40.0
    >>> celsius_to_fahrenheit(-20.0)
    -4.0
    >>> celsius_to_fahrenheit(0)
    32.0
    >>> celsius_to_fahrenheit(20)
    68.0
    >>> celsius_to_fahrenheit("40")
    104.0
    >>> celsius_to_fahrenheit("celsius")
    Traceback (most recent call last):
        ...
    ValueError: could not convert string to float: 'celsius'
    """
    return round((float(celsius) * 9 / 5) + 32, ndigits)


def celsius_to_kelvin(celsius: float, ndigits: int = 2) -> float:
    """
    Convert a given value from Celsius to Kelvin and
    round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Celsius
    Wikipedia reference: https://en.wikipedia.org/wiki/Kelvin
    >>> celsius_to_kelvin(273.354, 3)
    546.504
    >>> celsius_to_kelvin(273.354, 0)
    547.0
    >>> celsius_to_kelvin(0)
    273.15
    >>> celsius_to_kelvin(20.0)
    293.15
    >>> celsius_to_kelvin("40")
    313.15
    >>> celsius_to_kelvin("celsius")
    Traceback (most recent call last):
        ...
    ValueError: could not convert string to float: 'celsius'
    """
    return round(float(celsius) + 273.15, ndigits)


def celsius_to_rankine(celsius: float, ndigits: int = 2) -> float:
    """
    Convert a given value from Celsius to Rankine and
    round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Celsius
    Wikipedia reference: https://en.wikipedia.org/wiki/Rankine_scale
    >>> celsius_to_rankine(273.354, 3)
    983.707
    >>> celsius_to_rankine(273.354, 0)
    984.0
    >>> celsius_to_rankine(0)
    491.67
    >>> celsius_to_rankine(20.0)
    527.67
    >>> celsius_to_rankine("40")
    563.67
    >>> celsius_to_rankine("celsius")
    Traceback (most recent call last):
        ...
    ValueError: could not convert string to float: 'celsius'
    """
    return round((float(celsius) * 9 / 5) + 491.67, ndigits)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
