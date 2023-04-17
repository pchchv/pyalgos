"""
The LZ77 compression algorithm.
A lossless data compression algorithm
published by Abraham Lempel and Jacob Ziv in 1977.
Also known as LZ1 or sliding window compression.
Forms the basis for many variations, including LZW, LZSS, LZMA, and others.

It uses a “sliding window” method.
Within the sliding window we have a search buffer and a look ahead buffer.
len(sliding_window) = len(search_buffer) + len(look_ahead_buffer)

LZ77 controls the dictionary, which uses triples consisting of:
- Search buffer offset, which is the distance between the beginning of
the phrase and the beginning of the file.
- Match length, is the number of characters that make up the phrase.
- The indicator is represented by a character,
which will be encoded as follows.

As the file is parsed, the dictionary is dynamically updated to
reflect the compressed content and data size.

Examples:
"cabracadabrarrarrad" <-> [(0, 0, 'c'), (0, 0, 'a'), (0, 0, 'b'), (0, 0, 'r'),
                           (3, 1, 'c'), (2, 1, 'd'), (7, 4, 'r'), (3, 5, 'd')]
"ababcbababaa" <-> [(0, 0, 'a'), (0, 0, 'b'), (2, 2, 'c'), (4, 3, 'a'),
                    (2, 2, 'a')]
"aacaacabcabaaac" <-> [(0, 0, 'a'), (1, 1, 'c'), (3, 4, 'b'), (3, 3, 'a'),
                       (1, 2, 'c')]

Sources:
en.wikipedia.org/wiki/LZ77_and_LZ78
"""


from dataclasses import dataclass


@dataclass
class Token:
    """
    Dataclass representing a triplet, called token,
    consisting of length, offset, and indicator.
    This triplet is used during LZ77 compression.
    """

    offset: int
    length: int
    indicator: str

    def __repr__(self) -> str:
        """
        >>> token = Token(1, 2, "c")
        >>> repr(token)
        '(1, 2, c)'
        >>> str(token)
        '(1, 2, c)'
        """
        return f"({self.offset}, {self.length}, {self.indicator})"
