rows = int(input("Please enter your rows: "))
colums = int(input("Please eneter your columns: "))
for i in range(1, rows+1):
    for j in range(1, colums + 1):
        #print(end = "10")
        if(j % 2 != 1):
            print(end = "1")
        else:
            print(end = "0")
    print()