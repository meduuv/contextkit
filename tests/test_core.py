from contextkit import merge, trim


def test_trim_and_merge():
    assert trim("abcdef", 3) == "abc"
    assert merge([" first ", "", "second"]) == "first\n\nsecond"
