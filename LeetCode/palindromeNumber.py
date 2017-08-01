"""
    A method using reversing integer takes O(N) time.
"""

str = int(raw_input())
if x < 0:
    return False
high = pow(10,len(str(x))-1)
result = 0
low = 1
origin = x
while high != 0:
    y = x/high
    result += y * low
    x = x%high
    high /= 10
    low *=10
if origin == result:
    return True
else:
    return False
