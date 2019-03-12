import pytest


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

MORSE_TO_LETTER = {
    morse: letter
    for letter, morse in LETTER_TO_MORSE.items()
}


def decode(morse_message: str):
    """
    Декодирует строку из азбуки Морзе в английский
    """
    decoded_letters = [
        MORSE_TO_LETTER[letter] for letter in morse_message.split()
    ]

    return ''.join(decoded_letters)


def print_in_file(param1, param2):
    with open('result_decode', 'a+', encoding='utf-8') as new_file:
        print('{}{}{}'.format(param1, ' - ', param2), file=new_file)


@pytest.mark.parametrize('test_input, result', [
                        ('....', 'h'),
                        ('..', 'i')
                        ])
def test_decode_second(test_input, result):
    assert decode(test_input) == result.upper()
    print_in_file(test_input, result)


@pytest.mark.parametrize('test_input, result', [
                        ('..---', '2'),
                        ('...--', '3')
                        ])
def test_decode_third(test_input, result):
    assert decode(test_input) == result.upper()
    print_in_file(test_input, result)


@pytest.mark.parametrize('test_input, result', [
                        ('... --- ...', 'SOS'),
                        ('-.--', 'Y'),
                        ('.', 'E'),
                        ('.-', 'A'),
                        ('....', 'H')
                        ])
def test_decode_first(test_input, result):
    assert decode(test_input) == result.upper()
    print_in_file(test_input, result)


if __name__ == '__main__':
    pytest.main([__file__])
