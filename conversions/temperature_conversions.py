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


def fahrenheit_to_celsius(fahrenheit: float, ndigits: int = 2) -> float:
    """
    Convert a given value from Fahrenheit to Celsius and
    round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Fahrenheit
    Wikipedia reference: https://en.wikipedia.org/wiki/Celsius
    >>> fahrenheit_to_celsius(273.354, 3)
    134.086
    >>> fahrenheit_to_celsius(273.354, 0)
    134.0
    >>> fahrenheit_to_celsius(0)
    -17.78
    >>> fahrenheit_to_celsius(20.0)
    -6.67
    >>> fahrenheit_to_celsius(40.0)
    4.44
    >>> fahrenheit_to_celsius(60)
    15.56
    >>> fahrenheit_to_celsius(80)
    26.67
    >>> fahrenheit_to_celsius("100")
    37.78
    >>> fahrenheit_to_celsius("fahrenheit")
    Traceback (most recent call last):
        ...
    ValueError: could not convert string to float: 'fahrenheit'
    """
    return round((float(fahrenheit) - 32) * 5 / 9, ndigits)


def fahrenheit_to_kelvin(fahrenheit: float, ndigits: int = 2) -> float:
    """
    Convert a given value from Fahrenheit to Kelvin and
    round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Fahrenheit
    Wikipedia reference: https://en.wikipedia.org/wiki/Kelvin
    >>> fahrenheit_to_kelvin(273.354, 3)
    407.236
    >>> fahrenheit_to_kelvin(273.354, 0)
    407.0
    >>> fahrenheit_to_kelvin(0)
    255.37
    >>> fahrenheit_to_kelvin(20.0)
    266.48
    >>> fahrenheit_to_kelvin(40.0)
    277.59
    >>> fahrenheit_to_kelvin(60)
    288.71
    >>> fahrenheit_to_kelvin(80)
    299.82
    >>> fahrenheit_to_kelvin("100")
    310.93
    >>> fahrenheit_to_kelvin("fahrenheit")
    Traceback (most recent call last):
        ...
    ValueError: could not convert string to float: 'fahrenheit'
    """
    return round(((float(fahrenheit) - 32) * 5 / 9) + 273.15, ndigits)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
