
rows = int(input())
num = 1
for row in range(1, rows+2):
    for j in range(rows+2, 0, -1):
        if j >= row:
            print(" ", end=' ')
        else:
            print(num, end=' ')
            num += 1
    print("")
