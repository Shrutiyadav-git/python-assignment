#Write a program in python that counts the frequency of each character in a string.
Str1=input("Enter String:")
L1=list(Str1)
for i in L1:
    print("Frequency of",i,":",L1.count(i))
