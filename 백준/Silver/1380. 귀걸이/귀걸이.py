from collections import Counter

turn = 1

while True:
  n = int(input())

  if n == 0:
    break

  students = {i : input() for i in range(1, n + 1)}
  counts = {}

  for _ in range(n * 2 - 1):
    student_num_str, t = input().split(' ')
    student_num = int(student_num_str)

    counts[student_num] = counts.get(student_num, 0) + 1

  for num, count in counts.items():
    if count % 2 != 0:
      print(f"{turn} {students[num]}")
      break
      
  turn += 1