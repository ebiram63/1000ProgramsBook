rows = int(input("Enter your rows"));
for i in range (rows // 2 , rows + 1, 2):
    for j in range(1, rows - i, 2):
        print(end = "1")
    for j in range(1, i + 1):
        print(end = "2")
    for  j in range(1, rows - i+1):
        print(end = "3")
    for  j in range(1, i + 1):
        print(end="4")
    print()
for i in range(rows, 0 , -1):
    for j in range(i, rows+1):
        print(end="5")
    for j in range(1, (i * 2)):
        print(end = "6")
    print()