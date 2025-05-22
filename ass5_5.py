string = input("Enter a string : ")

if(string == string[::-1]):
    print(string, "is Palindrome")
else:
    print(string, "is not Palindrome")

'''
OUTPUT:
Enter a string : radar
radar is Palindrome
'''