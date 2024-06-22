n = int(input("Enter the no of elements: "))
numbers = []
for i in range(n):
    num = float(input(f"Enter the {i+1} number: "))
    numbers.append(num)
    
sumofnum = sum(numbers)
length = len(numbers)

average = sumofnum/length

print(f"The average is {average}")