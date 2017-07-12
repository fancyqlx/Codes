"""
    By using string strcuture, we only need to determine whether the i-th number is equal to (length-i-1)-th number.
"""

str = int(raw_input())
if x < 0:
    return False
s = str(x)
length = len(s)
if length == 1:
    return True
for i in range(length/2):
    if s[i] != s[length-i-1]:
        return False
return True
