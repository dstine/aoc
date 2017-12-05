import csv

def day4_1(filename):
    return day4(filename, equals_test)

def day4_2(filename):
    return day4(filename, anagram_test)

def day4(filename, test):
    path = "aoc/aoc-2017/data/" + filename
    valid_phrases = 0
    with open(path) as file:
        reader  = csv.reader(file, delimiter=" ")
        for row in reader:
            if is_valid_phrase(row, test):
                valid_phrases += 1
    return valid_phrases

def equals_test(word, seen):
    return word in seen

def anagram_test(word, seen):
    sorted_word = "".join(sorted(word))
    for s in seen:
        sorted_s = "".join(sorted(s))
        if sorted_word == sorted_s:
            return True
    return False

def is_valid_phrase(phrase, test):
    seen = []
    for word in phrase:
        if test(word, seen):
            return False
        seen.append(word)
    return True
