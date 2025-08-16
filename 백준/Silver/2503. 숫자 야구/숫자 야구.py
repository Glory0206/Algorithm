T = int(input())
q = []

for _ in range(T):
    num, strike, ball = map(int, input().split())
    q.append((str(num), strike, ball))

def check(n, guess, strike, ball):
    s = b = 0

    for i in range(3):
        if n[i] == guess[i]:
            s += 1
        elif n[i] in guess:
            b += 1
    return s == strike and b == ball

answer = 0

for i in range(123, 988):
    n = str(i)

    if '0' in n or len(set(n)) < 3:
        continue

    valid = True
    for guess, strike, ball in q:
        if not check(n, guess, strike, ball):
            valid = False
            break
    if valid:
        answer += 1
print(answer)