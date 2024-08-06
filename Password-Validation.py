#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Cracking program:
    
import hashlib
from urllib.request import urlopen
def wordlist(url):
    try:
        wordfile = urlopen(url).read()
    except Exception as a:
        print("error reading the wordlist:", a)
        exit()
    return wordfile

def hash(wordlistpassword):
    result = hashlib.sha1(wordlistpassword.encode())
    return result.hexdigest()

def bruteforce(guesspassword, actualpasswordhash):
    for guess_password in guesspasswordlist:
        if hash(guess_password) == actualpasswordhash:
            print("Your password is:", guess_password, "\n please change it is easy to crack")
            global find
            find = 1
            break

url = 'https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt'
actualpassword = 'dragon'
actualpasswordhash = hash(actualpassword)
find = 0
wordlist = wordlist(url).decode('UTF-8')
guesspasswordlist = wordlist.split('\n')

bruteforce(guesspasswordlist, actualpasswordhash)
if find == 0:
    print("Cannot find password")


# In[5]:


# Defense Program:
    
import re
a= input("Insert password:")
b = True

while a: 
    if (len(a)<8 or len(a)>30):
        break
    elif not re.search("[A-Z]",a):
        break
    elif not re.search("[0-9]",a):
        break
    elif not re.search("[a-z]",a):
        break
    elif re.search("\s",a):
        break
    elif not re.search("[`~!$#@%^&*(){}\|/?><.;:”’]",a):
        break
    else:
        print("Strong Password")
        b=False
        break
if b:
    print("Not a Strong Password")

