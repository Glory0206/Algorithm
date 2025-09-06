cm = {
  '0' : 4,
  '1' : 2,

}

for i in range(2, 10):
    cm[str(i)] = 3

while True:
  result = 0
  num = input()

  if num == '0':
    break

  for n in num:
    result += cm[n]

  print(result + len(num) + 1)