while True:
    w = input()
    if w == "#":
        exit()
    print(w[0], w[1:].count(w[0]) + w[1:].count(w[0].upper()))