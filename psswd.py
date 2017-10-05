"""A simple password generator that outputs a
a random password of a selected length as required
by the user"""
import random
import string
letters=string.ascii_letters
num=string.digits
mark=string.punctuation
#char concatnates the values of letters,num and mark variables
char=letters+num+mark
#password length is converted to an interger type to be used later by random.randint
pswd_len=int(input("Enter the number of characters for your password >>>"))
#join method is used to join the values of the char variable with a string separator 
password="".join(random.choice(char)for p in range(random.randint(0,pswd_len+1)))
print (password)
