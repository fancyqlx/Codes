"""
    This method utilize string structure to construct new string.
    The time complexity is O(n) where n is the length of origin string.
    I have thought this method would be faster than another one, but it is actually slower.
"""

s = raw_input()
numRows = int(raw_input())

array = ["" for i in range(numRows)]

row = 0
column = 0

if numRows == 1:
    print s
else:
    i = 0
    while i < len(s):
        for row in range(numRows):
            if i == len(s):
                break
            array[row] += s[i]
            i += 1
        for row in range(numRows-2,0,-1):
            if i == len(s):
                break
            array[row] += s[i]
            i += 1
    result = ""
    for j in array:
        result = result + j

    print result

