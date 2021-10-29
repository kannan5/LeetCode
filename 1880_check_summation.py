import string


values = dict()

for index, letter in enumerate(string.ascii_lowercase):
    values[letter] = index 


def isSumEqual(firstWord, secondWord, targetWord):
    wordSum = int(''.join(str(values[x]) for x in firstWord)) + int(''.join(str(values[y]) for y in secondWord))
    targetWordSum = int(''.join(str(values [z]) for z in targetWord))
    return wordSum == targetWordSum

print(isSumEqual("aaa","a","aaaa"))
print(isSumEqual("aab","a","aaaa"))
print(isSumEqual("acb","cba","cdb"))

