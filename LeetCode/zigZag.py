"""
    This method utilize string structure to construct new string.
    The time complexity is O(n) where n is the length of origin string.
"""

s = raw_input()
numRows = int(raw_input())

result = ""
if numRows == 1:
    print s
else:
    cycle = 2 * numRows - 2
    length = len(s)
    n = length/cycle + 1
    if length%cycle == 0:
        n -= 1
    for i in range(n):
        result += s[cycle*i]
    for i in range(1,numRows-1):
        for j in range(n):
            first = cycle * j + i
            second = cycle * j + cycle - i
            if first <= length-1 and second <= length - 1:
                result += s[first]
                result += s[second]
            elif first <= length-1:
                result += s[first]
    for i in range(n):
        if i == n-1 and cycle*i+numRows-1 > length-1:
            break
        result += s[cycle*i+numRows-1]

    print result
