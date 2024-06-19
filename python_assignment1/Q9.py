#Write a python program that checks if a substring is present in a given string.
#Method-1
main_str = "Hello World"
sub_str = "World"
print(sub_str in main_str)

#Method-2
Main_str = input("Enter the main string:")
Sub_str = input("Enter the string:")
if(Sub_str in Main_str):
    print("The sub-string is present")
else:
    print("The sub-string is not present")