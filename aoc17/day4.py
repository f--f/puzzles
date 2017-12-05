"""Advent of Code Day 4: High-Entropy Passphrases"""

def num_valid_phrases(text, valid_func=None):
    """Return number of valid phrases in a text string where each phrase is
    separated by a new line, given an arbitrary validation function."""
    phrases = text.splitlines()
    num_valid = sum(1 for p in phrases if valid_func(p))
    return num_valid

# Validation functions for Part 1 & 2
# Approach: Compare number of phrases with number in set (eliminates doubles)
valid_p1 = lambda p: len(set(p.split())) == len(p.split())
def valid_p2(p):
    """Part 2 Approach: Sort before comparing to eliminate anagram phrases"""
    p_sorted = [''.join(sorted(word)) for word in p.split()]
    return len(set(p_sorted)) == len(p.split())

# Part 1
assert valid_p1("aa bb cc dd ee")
assert not valid_p1("aa bb cc dd aa")
assert valid_p1("aa bb cc dd aaa")
assert num_valid_phrases("aa bb cc dd ee\n"
                         "aa bb cc dd aa\n"
                         "aa bb cc dd aaa", valid_p1) == 2

# Part 2
assert valid_p2("abcde fghij")
assert not valid_p2("abcde xyz ecdab")
assert valid_p2("a ab abc abd abf abj")
assert valid_p2("iiii oiii ooii oooi oooo")
assert not valid_p2("oiii ioii iioi iiio")
assert num_valid_phrases("abcde fghij\n"
                         "abcde xyz ecdab\n"
                         "oiii ioii iioi iiio", valid_p2) == 1
