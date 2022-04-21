from lab03 import *
def test_1():
    assert integerDivision(27,4) == 6
    assert integerDivision(3,5) == 0
    assert integerDivision(3,3) == 1
    assert integerDivision(4,2) == 2
    assert integerDivision(7,2) == 3
    assert integerDivision(0,2) == 0


def test_2():
    assert collectEvenInts([1,2,3,4,5]) == [2,4]
    assert collectEvenInts([0,2,4,25]) == [0,2,4]
    assert collectEvenInts([2,2,2,2]) == [2,2,2,2]
    assert collectEvenInts([1,3,5,7]) == []
    assert collectEvenInts([]) == []

def test_3():
    assert countVowels("Hello World!") == 3
    assert countVowels("AAAAH!") == 4
    assert countVowels("!$#&@^%$#") == 0
    assert countVowels("") == 0
    assert countVowels("P o E,I!Lab@U") == 5

def test_4():
    assert reverseString("ABCDE") == "EDCBA"
    assert reverseString("!@#$%") == "%$#@!"
    assert reverseString("") == ""

def test_5():
    assert removeSubString("HAHAHAH","ha") == "HAHAHAH"
    assert removeSubString("HAHAHAH","HA") == "H"
    assert removeSubString("HAHAHAH","HAH") == "A"
    assert removeSubString("HAHAHAH","HAHA") == "HAH"
    assert removeSubString("","ha") == ""
    assert removeSubString("HAHAHAH","") == "HAHAHAH"



