from questions.test_15 import highest_limit
from questions.test_16 import long_words
from questions.test_17 import is_vowel
from questions.test_18 import pangram
from questions.test_19 import song
from questions.test_20 import translate


def test_highest_limit():

    result = highest_limit(["bountiess", "milka", "python"])
    expected = 9
    assert result == expected


def test_long_words():

    result = long_words(["bountiess", "milka", "python"], 7)
    expected = ["bountiess"]
    assert result == expected


def test_is_vowel():

    result = is_vowel("h")
    expected = False
    assert result == expected


def test_pangram():

    result = pangram("quick fox")
    expected = False
    assert result == expected


def test_song():

    result = song()
    expected = "Take one down, pass it around,1bottles of beer on the wall."
    assert result == expected


def test_translate():

    result = translate(['Merry'])
    expected = ['god']
    assert result == expected
