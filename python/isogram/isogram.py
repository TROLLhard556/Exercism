def is_isogram(string):
    letters = [char for char in string.lower() if char.isalpha()]
    unique = []
    for char in letters:
        if char not in unique:
            unique.append(char)
        else:
            return False

    return True

