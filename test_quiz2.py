from Q15 import longestLength
from Q16 import long_words
from Q17 import is_vowel
from Q18 import pangram
from Q19 import song
from Q20 import translate


def test_longestLength():

    result = longestLength(["bountiess", "milka", "python"])
    expected = 9
    assert result == expected


def test_long_words():

    result = long_words(["bountiess", "milka", "python"])
    expected = "bountiess"
    assert result == expected


def test_is_vowel():

    result = is_vowel("h")
    expected = False
    assert result == expected


def test_pangram():

    result = pangram("quick fox")
    expected = True
    assert result == expected


def test_song():

    result = song("99 bottles of beer on the wall, 99 bottles of beer")
    expected = "Take one down, pass it around,1bottles of beer on the wall."
    assert result == expected


def test_translate():

    result = translate(['Merry'])
    expected = "god"
    assert result == expected
