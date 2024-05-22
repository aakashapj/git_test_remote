p = 'llo'
s = 'Hello'
def findPattern(s,p):
    #Your code below
    for i in range(len(s)):
        check = s[i:(len(p)+i)]
        if p == check:
            return i

    return -1

print(findPattern('Hello', 'llo'))