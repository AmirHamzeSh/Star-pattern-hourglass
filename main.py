import os
num = 19

for i in range(0, int(num / 2)):
    for j in range(i, 0, -1):
        print(" ", end="")
    for z in range(num - (i * 2), 0, -1):
        print("*", end="")
    print(" ")

if(num % 2 == 0):
    for i in range(int(num / 2), 0, -1):
        print(" ", end="")
    print(" ")

for i in range(int(num / 2), 0, -1):
    for j in range(0, i):
        print(" ", end="")
    for z in range(0, num - (i * 2)):
        print("*", end="")
    print(" ")

os.system("pause")