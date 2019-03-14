import doctest


dict_test_string_encode = {'1': 'SOS',
                           '2': 'SOs',
                           '3': 'SoS',
                           '4': 'sos'}


LETTER_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-',
    ' ': ' '
}


def encode(message: str) -> str:
    """
    doctest
    >>> encode(dict_test_string_encode['1'])
    encoded_message = ... --- ...
    >>> try:
    ...     encode(dict_test_string_encode['4'])
    ... except KeyError:
    ...     logging.exception('LOW REGISTER')
    >>> encode(dict_test_string_encode['4'].upper())
    encoded_message = ... --- ...
    """

    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)




