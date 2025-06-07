ticket = input()

ticket_len = len(ticket)

for length in range(ticket_len, 1, -1):
    if length % 2 != 0:
        continue

    for start in range(ticket_len - length + 1):
        mid = start + length // 2
        left = sum(int(ticket[i]) for i in range(start, mid))
        right = sum(int(ticket[i]) for i in range(mid, start + length))

        if left == right:
            print(length)
            exit()

print(0)