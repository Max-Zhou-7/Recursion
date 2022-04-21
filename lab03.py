def integerDivision(n,k):

    if n-k < 0:
        return 0
    return integerDivision(n-k,k)+1
    

def collectEvenInts(listOfInt):
    if listOfInt == []:
        return []
    if len(listOfInt) == 1:
        if listOfInt[0] % 2 != 0:
            return []
        if listOfInt[0] % 2 == 0:
            return [listOfInt[0]]
    return collectEvenInts(listOfInt[:-1]) + collectEvenInts([listOfInt[-1]])



def countVowels(someString):
    if someString == "":
        return 0
    if len(someString) == 1:
        if someString[0] in "AEIOUaeiou":
            return 1
        else:
            return 0
    return countVowels(someString[:-1]) + countVowels(someString[-1])

# def count(s):
#     if s == "":
#         return 0
#     if s[0] in "AEIOUaeiou":
#         return 1 + count(s[1:])
#     else:
#         return count(s[1:])

def reverseString(s):
    if s == "":
        return ""
    if len(s) == 1:
        return s
    return reverseString(s[1:])+reverseString(s[0])

def removeSubString(s,sub):
    if s == "":
         return ""  
    if sub == "":
        return s
    if s[:len(sub)] == sub:
        if len(s) == len(sub):
            return ""
        else:
            return removeSubString(s[len(sub):],sub)
    else:
        return s[0] + removeSubString(s[1:],sub)
    


