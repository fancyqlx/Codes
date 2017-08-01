
str = raw_input()
maxInt = 2147483647
minInt = -2147483648
result = ""

for i in range(len(str)):
    if str[i].isdigit() or str[i] == '-' or str[i] == '+':
        result += str[i]
        for j in range(i+1,len(str)):
            if not str[j].isdigit():
                break
            result += str[j]
        break
    elif str[i].isspace():
        continue
    else:
        return 0

if result == "" or result == "+" or result == "-":
    return 0

integer = int(result)

if integer > maxInt:
    return maxInt
elif integer < minInt:
    return minInt
else:
    return integer
