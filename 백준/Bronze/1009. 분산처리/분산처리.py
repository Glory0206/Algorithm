import sys

cycle_dict = {
    0: [10],
    1: [1],
    2: [2, 4, 8, 6],
    3: [3, 9, 7, 1],
    4: [4, 6],
    5: [5],
    6: [6],
    7: [7, 9, 3, 1],
    8: [8, 4, 2, 6],
    9: [9, 1],
}

T = int(sys.stdin.readline())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())

    # 밑수 a의 1의 자리
    a %= 10
    # 해당 숫자의 반복 주기 불러오기
    cycle = cycle_dict[a]

    # b번째 거듭제곱의 결과는 cycle 내에서 (b-1) 위치의 값과 동일
    index = (b-1) % len(cycle)

    print(cycle[index])