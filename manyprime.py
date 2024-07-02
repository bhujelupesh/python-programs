n = int(input("Enter the no upto which you want to find prime number: "))

for i in range (n):
    if i > 1:
        for j in range (2,i):
            if i % j == 0:
                break
        else:
            print(i)
            