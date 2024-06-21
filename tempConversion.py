x = float(input("Enter the temperature in celsius: "))
y = float(input("Enter the temperature in fahrenheite: "))

print(f"{x} degree = {x * 9/5 + 32} degree fahrenheite")    # C to F formula C*9/5 + 32
print(f"{y} pahrenheite = {(y - 32) * 5/9} degree celsius") # F to C formula (f-32)*5/9