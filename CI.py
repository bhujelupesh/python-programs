p = float(input("Enter the principle amount: "))
t = float(input("Enter the time in year: "))
r = float(input("Enter the rate of the intrest: ")) 
n = int(input("Enter the no of time the intrest is compound in a year: "))
ci = p * (1 + r/(n*100))**(n*t)

print(f"The Compound Intrest of Principle {p}, time {t} and rate {r} is {ci}")

#amount = principal * (1 + rate/(n*100))**(n*time)