"""
    This is the second straightforward way to address two sum problem.
    By using hash table,
    it is easy to reduce the time complexity from n*n to n*logn.
"""

nums = []
n = int(raw_input())
for i in range(n):
    nums.append(int(raw_input()))
target = int(raw_input())

d = {}

for i in range(n):
    temp = target - nums[i]
    if d.has_key(temp):
        print [i,d[temp]]
    d[nums[i]] = i
