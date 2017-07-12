

str = raw_input()
maxInt = 2147483647
minInt = -2147483648
flag = 1
integer = 0

for i in range(len(str)):
    if str[i].isdigit() or str[i] == '-' or str[i] == '+':
        if str[i] == '-':
            flag = 0
        elif str[i].isdigit():
            integer = integer * 10 + (ord(str[i]) - 48)
        for j in range(i+1,len(str)):
            if not str[j].isdigit():
                break
            integer = integer * 10 + (ord(str[j]) - 48)
        if flag == 0:
            integer = - integer
        if integer > maxInt:
            return maxInt
        elif integer < minInt:
            return minInt
        else:
            return integer
    elif str[i].isspace():
        continue
    else:
        return 0
return 0
