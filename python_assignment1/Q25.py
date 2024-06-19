# Write a program that copies the contents of one text file to another.
File1 = open("C:\IGDTUW\Python & ML internship\Python practice\python_assignment1\My_File.txt" , 'r')
c = File1.read()

samplefile = open("C:\IGDTUW\Python & ML internship\Python practice\demo.txt",'w')
print(c, file = samplefile)

