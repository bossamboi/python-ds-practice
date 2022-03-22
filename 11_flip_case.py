def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    flipped = ''
    for letter in phrase:
        if letter.lower() == to_swap.lower():
            flipped += letter.swapcase()
        else:
            flipped += letter
    return flipped

    # list_phrase = list(phrase)
    # swapped_list = [letter.swapcase() for letter in list_phrase if letter.lower() == to_swap.lower()]
    # return ''.join(swapped_list)