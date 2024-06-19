#Write a program that takes a string input from the user and writes it to a text file.
str = input("Enter a string:")
File1 = open("C:\IGDTUW\Python & ML internship\Python practice\python_assignment1\My_File.txt", 'w')

print(str, file = File1)            