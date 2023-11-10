rows = int(input("Please Enter your rows: "))
columns = int(input("Please Enter your columns: "))
for i in range(1, rows+ 1):
    for j in range(1, columns+1):
        if i % 2 == 1:
            print(end="1")
        else:
            print(end = "0")
    print()