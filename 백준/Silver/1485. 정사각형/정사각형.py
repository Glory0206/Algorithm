from collections import Counter

T = int(input())

def distance(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

for _ in range(T):
    dots = []
    distances = []

    for _ in range(4):
        x, y = map(int, input().split())
        dots.append((x, y))

    for i in range(4):
        for j in range(i+1, 4):
            dist = distance(dots[i], dots[j])
            distances.append(dist)

    distance_counts = Counter(distances)

    if len(distance_counts) == 2:
        keys = list(distance_counts.keys())
        counts = list(distance_counts.values())

        if(counts[0] == 4 and counts[1] == 2) or (counts[0] == 2 and counts[1] == 4):
            print(1)
        else:
            print(0)
    else:
        print(0)