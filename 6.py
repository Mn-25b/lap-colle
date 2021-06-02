# задача 6
x = int(input())
y = 0
for i in range(1, x+1):
  if x % i == 0:
    y = y + 1
print(y)
