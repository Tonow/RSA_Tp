"""
Fichier:	 python 3.
Ecrit par :	 Tonow
Le :		 Date
Sujet:		 TODO
"""

from binascii import unhexlify

def long_to_bytes(val, endianness='big'):
    """
    Use :ref:`string formatting` and :func:`~binascii.unhexlify` to
    convert ``val``, a :func:`long`, to a byte :func:`str`.

    :param long val: The value to pack

    :param str endianness: The endianness of the result. ``'big'`` for
      big-endian, ``'little'`` for little-endian.

    If you want byte- and word-ordering to differ, you're on your own.

    Using :ref:`string formatting` lets us use Python's C innards.
    """

    # one (1) hex digit per four (4) bits
    width = val.bit_length()

    # unhexlify wants an even multiple of eight (8) bits, but we don't
    # want more digits than we need (hence the ternary-ish 'or')
    width += 8 - ((width % 8) or 8)

    # format width specifier: four (4) bits per hex digit
    fmt = '%%0%dx' % (width // 4)

    # prepend zero (0) to the width, to zero-pad the output
    sortie = unhexlify(fmt % val)

    if endianness == 'little':
        sortie = sortie[::-1]

    return sortie


def EstProbablementPremier(nombre):
    """
    Vrais si nombre est premier, Faux si nombre
    non premier (avec epsilone = 1/4)
    """


def modexp(base, expo, mod):
    result = 1
    while expo > 0:
        if (expo & 1) > 0:
            result = (result * base) % mod
        expo = expo >> 1
        base = (base * base) % mod
    return result


def pgcd(a, b):
    """
    Calcule le pgcd de a par b.
    """
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
