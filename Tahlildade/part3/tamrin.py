print("==============tamrin 1 =================")

num = int(input("Please enter your number: "))

for i in range(3):
    print("*" * num)
    if i == 2:
        break
    else:
        for j in range(num-1):
            print("*")

print("==============tamrin 2 =================")