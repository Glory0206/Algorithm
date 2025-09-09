# G = current**2 - think**2
G = int(input())

current = 1
think = 1
answers = []

while current <= 100000:
    diff = current**2 - think**2

    if diff == G:
        answers.append(current)

    if diff > G:
        if think >= current:
            break
        think += 1
    else:
        current += 1

if not answers:
    print(-1)
else:
    for answer in answers:
        print(answer)