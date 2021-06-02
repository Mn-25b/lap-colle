#задача 4
n = int(input())
arr = []
a = 1
i = 1
while i:
  if (a**2) <= n:
    arr.append(a**2)
    a = a + 1
  else:
    i = 0
print(arr)