"""
Functions useful for doing molecular chemistry:
* molarity_to_normality
* moles_to_pressure
* moles_to_volume
* pressure_and_volume_to_temperature
"""


def molarity_to_normality(nfactor: int, moles: float, volume: float) -> float:
    """
    Convert molarity to normality.
      Volume is taken in litres.
      Wiki reference: https://en.wikipedia.org/wiki/Equivalent_concentration
      Wiki reference: https://en.wikipedia.org/wiki/Molar_concentration
      >>> molarity_to_normality(2, 3.1, 0.31)
      20
      >>> molarity_to_normality(4, 11.4, 5.7)
      8
    """
    return round(float(moles / volume) * nfactor)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
