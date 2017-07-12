"""
    This is the second straightforward way to address two sum problem.
    It is easy to reduce the time complexity from n*n to n*logn.
"""

nums = []
n = int(raw_input())
for i in range(n):
    nums.append(int(raw_input()))
target = int(raw_input())


for i in range(n):
    temp = target - nums[i]
    if (temp in nums) and nums.index(temp) != i:
        print [i, nums.index(temp)]
