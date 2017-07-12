"""
    This method utilize string structure to construct new string.
    The time complexity is O(n) where n is the length of origin string.
"""

s = raw_input()
numRows = int(raw_input())

array = ["" for i in range(numRows)]

row = 0
column = 0

if numRows == 1:
    print s
else:
    for i in range(len(s)):
        if column % (numRows-1) == 0:
            array[row] = array[row] + s[i]
            row = row + 1
            if row == numRows:
                column = column + 1
                row = 0
        else:
            array[numRows - 1 - column % (numRows-1)] += s[i]
            column = column + 1

    result = ""
    for i in array:
        result = result + i

    print result
