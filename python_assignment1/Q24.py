# Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.
num_1 = int(input("Enter first number:"))
num_2 = int(input("Enter second number: "))
op = input("Enter the operator:")
if(op=="+"):
    res = num_1+num_2
    print(res)
elif(op=="-"):
    res = num_1-num_2
    print(res)
elif(op=="*"):
    res = num_1*num_2
    print(res)
elif(op=="/"):
    res = num_1/num_2
    print(res)
else:
    print("Invalid operation")
print(num_1," ",op," ",num_2," = ",res)
