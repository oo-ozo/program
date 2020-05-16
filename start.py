import sys
import os

print("making files.....")
os.system("man python >> python_help.txt")
os.system("man ruby >> ruby_help.txt")
os.system("man php >> php_help.txt")
print("done")

print("checking system.......")
os.system("sleep 3")

print("you can see help file")
print("[1]ruby")
print("[2]python")
print("[3]php")
print("[99]exit")
print(" ")
q = input("enter your choice :")

def ruby():
    f = open('ruby_help.txt', 'r')
    h = f.read()
    print(h)

def python():
    u = open('python_help.txt','r')
    l = u.read()
    print(l)

def php():
    a = open('php_help.txt', 'r')
    o = a.read()
    print(o)

if q == '1':
    ruby()
elif q == '2':
    python()
elif q == '3':
    php()
elif q == '99':
    sys.exit()
else:
    print("wrong error")

    








