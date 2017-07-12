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


spe_case = float(target)/2

if spe_case in nums:
    i = nums.index(spe_case)
    for j in range(i+1,n):
        if nums[j] == spe_case:
            print [i,j]

d = {}
for i in range(n):
    d[nums[i]] = i
print d
for i in d:
    if d.has_key(target-i):
        print [d[i],d[target-i]]
