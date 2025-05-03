#logical operators and if/elif statements
a = 1
b = 2
c = 3

if a < c and b < c:
    print("c is bigger")
elif b > a or b > c:
    print("b is bigger than a")
    
p = 22
q = 12
r = 12

if p != q:
    print("p is not equal to q")
elif q != r:
    print("this is false, they are equal")
    
s1 = "coding"
s2 = "python"

if s1 != s2:
    print(f"{s1} and {s2} are different!")
    
a = 4
b = 5

if (a == 1) != (b == 5):
    print("Hello")
    
n = int(input("Enter a number: "))

if n % 2 == 0:
    print(f"{n} is an even number")
if n % 2 != 0:
    print(f"{n} is an odd number")
    
#BMI calculator
height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

BMI = weight / (height/100)**2

print("your bmi is", BMI)
if BMI <= 18.4:
    print("You are underweight")
elif BMI <= 24.9:
    print("You are healthy")
elif BMI <= 29.9:
    print("You are overweight")
elif BMI <= 34.9:
    print("You are severely overweight")
elif BMI <= 39.9:
    print("You are obese")
else :
    print("You are severely obese")