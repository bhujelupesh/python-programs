def factor(n):
    print(f"The factore of {n} are:")
    for i in range(1,n+1):
        if n % i == 0:
            print(i)

number = int(input("Enter the number whose factor you want to find: "))
factor(number)