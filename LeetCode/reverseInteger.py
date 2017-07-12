"""
    It is easy to devise an O(n) time algorithm by adding corresponding numbers
    from most significant to least significant of original number.
"""

x = int(raw_input())
maxInt = 2147483647

flag = True
if x < 0:
    flag = False
    x = -x

length = len(str(x))
high = pow(10,length-1)
factor = 1
result = 0

while(high != 0):
    y = x/high
    x = x%high
    result += y * factor
    high /= 10
    factor *= 10

if result > maxInt:
    print 0
elif flag:
    print result
else:
    print -result
