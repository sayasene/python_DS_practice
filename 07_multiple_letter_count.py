def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    phrase_letter_dict = {}
    for letter in phrase:
        if letter in phrase_letter_dict.keys():
            phrase_letter_dict[letter] += 1
        else:
            phrase_letter_dict[letter] = 1
    return phrase_letter_dict
