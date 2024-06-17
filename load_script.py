import re;

myFile = open("testtext.txt", "r+")
wholeS = myFile.read()


splat = re.split(", *|  *", wholeS)
print(splat)