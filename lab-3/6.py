#задача 6
n = str(input())
text = ''.join(reversed(n))
if n == text:
  print('yes')
else:
  print('no')