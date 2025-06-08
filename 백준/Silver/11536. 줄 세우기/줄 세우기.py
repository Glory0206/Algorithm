num = int(input())

names = [input() for _ in range(num)]

inc = sorted(names)
dec = sorted(names, reverse=True)

if names == inc:
    print("INCREASING")
elif names == dec:
    print("DECREASING")
else:
    print("NEITHER")