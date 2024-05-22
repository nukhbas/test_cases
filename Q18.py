def pangram(str):

    letter = "abcdefghijklmnopqrstuvwxyz"
    for char in letter:
        if char not in str.lower():
            return False
    return True


if __name__ == '__main__':

    string = 'the quick brown fox jumps over the lazy dog'
    if (pangram(string) == True): # noqa
        print("True")
    else:
        print("False")
