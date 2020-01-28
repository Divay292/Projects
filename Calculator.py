def add(x,y):
 return x+y

def sub(x,y):
 return x-y

def product(x,y):
 return x*y
 
def divide(x,y):
 try:
  return x/y
 except ZeroDivisionError:
  print("Undefined")
  
  
print("Welcome.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

ch = input("Enter your choice")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if ch == '1':
 print(num1,"+",num2, "=", add(num1, num2))

elif ch == '2':
 print(num1,"-",num2, "=", sub(num1, num2))

elif ch == '3':
 print(num1,"*",num2, "=", product(num1, num2))

elif ch == '4':
 print(num1,"/",num2, "=", divide(num1, num2))

else:
 print("INVALID CHOICE")