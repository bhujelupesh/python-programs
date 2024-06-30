#this program find the reverse, sum and no of digit of the number you inserted
number = int(input("Enter the number of your choice : "))
reverse = 0
count = 0
total = 0
while number > 0:
    remainder = number % 10
    reverse = reverse * 10 + remainder
    number = number // 10
    count += 1
    total += remainder
print("Reverse of the number is : ", reverse)
print("Total of the number is : ", total)
print("Count of the number is : ", count)
