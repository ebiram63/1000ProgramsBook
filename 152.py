rows = int(input("Enter your rows"));
for i in range (rows // 2 , rows + 1, 2):
    for j in range(1, rows - i, 2):
        print(end = " ")
    for j in range(1, i + 1):
        print(end = "*")
    for  j in range(1, rows - i+1):
        print(end = " ")
    for  j in range(1, i + 1):
        print(end="*")
    print()
for i in range(rows, 0 , -1):
    for j in range(i, rows+1):
        print(end=" ")
    for j in range(1, (i * 2)):
        print(end = "*")
    print()