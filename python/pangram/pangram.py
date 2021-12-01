def is_pangram(sentence):
    # first remove spaces from sentence: replace(" ", "")
    # then make the string lowercase: .lower()
    # then sort the resulting string alphabetically: sorted()
    # then remove duplicates: set()
    # then compare to a string of the alphabet
    # remove special characters and punctuation: "".join(i for i in ... if i.isalpha())
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    str = "".join(i for i in sorted(set(sentence.replace(" ", "").lower())) if i.isalpha())

    if str == alphabet:
        return True
    else:
        return False
