def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    letters = list(phrase)
    reversed_letters = letters[::-1]
    return ''.join(reversed_letters)

    