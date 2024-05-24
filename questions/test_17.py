def is_vowel(ch):

    if len(ch) == 1 and ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u': # noqa
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_vowel('i'))
