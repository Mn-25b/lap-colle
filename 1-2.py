# Задача один
n = int(input())

b = ''

while n > 0:
    b = str(n % 2) + b
    n = n // 2

print("Двоичная система: " + b)

# задача два
c = 0
for i in b:
  if int(i) == 1:
    c = c + 1
print("в ней ноходяться: " + str(c) + " едениц")
