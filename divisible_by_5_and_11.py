num = int(input("Enter the number you want to check: "))

if num % 5 == 0 and num % 11 == 0 :
    print("Number is divisible by both 5 and 11")

elif num % 5 == 0 :
    print("Number is divisible by 5 only but not of 11")

elif num % 11 == 0 :
    print("Number is divisible by 11 only but not of 5")
    
else:
    print("Number is not divisible by any of the number ")