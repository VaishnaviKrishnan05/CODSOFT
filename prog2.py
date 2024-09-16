print('*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!PYTHON CALCULATOR*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*')
print()
print('THE OPERATIONS THAT COULD BE PERFORMED BY THE CALCULATOR ARE GIVEN BELOW :')
print()
print('1.Addition(+)')
print('2.Subtraction(-)')
print('3.Multiplication(*)')
print('4.Division(/)')
print('5.Remainder(%)')
print()
num1=float(input('Enter the first number :'))
op=input('Enter your operator :')
num2=float(input('Enter the second number :'))

if op == '+':
    print(num1+num2)
elif op == '-':
    print(num1-num2)
elif op == '*':
    print(num1*num2)
elif op == '/':
    print(num1/num2)

elif op == '%':
    print(num1%num2)
else:
    print('Invalid!')
