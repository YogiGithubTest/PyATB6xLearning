# Given a Number a number you need to calculate the factorial of that number
# n = 5
# Fact = 5×4×3*2*1 = 120
# Fact = 0 → 1,
num = int(input("Enter a number which fact you want to get!"))
# 5
fact = 1

if num < 0:
    print("Fact is not defined!")

if num == 0:
    print("FACT = ", fact)
else:
    for i in range(1, num + 1):
        fact = fact * i

print("Factorial of : ", fact)