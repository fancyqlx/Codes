"""
    This is the most straightforward way to address two sum problem.
    The time complexity can be O(n^2).
"""

nums = []
n = int(raw_input())
for i in range(n):
    nums.append(int(raw_input()))
target = int(raw_input())


for i in range(n):
    for j in range(i + 1, n):
        if nums[i] + nums[j] == target:
            print [i, j]
