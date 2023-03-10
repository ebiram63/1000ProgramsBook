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

string = []

while(True): 
    word = input("Please enter your str: ")
    if word.lower() == 'break':
        break
    else:
        string.append(word)
print(string)

print("==============tamrin 3 =================")

num_list = []
for i in range(10):
    num_list.append(input("Please enter a number: "))

num_list.sort()

print(num_list)

print("==============tamrin 4 =================")