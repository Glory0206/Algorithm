N, M = map(int, input().split())
j = int(input())

turn = [int(input()) for _ in range(j)]
move_count = 0

left = 1
right = M

for spot in turn:
    if spot > right:
        move = spot - right
        move_count += move
        left += move
        right += move
    elif spot < left:
        move = left - spot
        move_count += move
        left -= move
        right -= move

print(move_count)