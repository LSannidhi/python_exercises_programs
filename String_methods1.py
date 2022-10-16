a="jai Sriram"
b=a.capitalize()
print(b)
b=a.title()
print(b)
a="SRIRAM IS A GOOD BOY"
b=a.casefold()
print(b)
b=a.center(50)
print(b)
a="I love Daddy, Dad love me and my brother"
b=a.count("love")
print(b)
a="Is Sriram a good boy?"
b=a.endswith("?")
print(b)
a="L\ta\tk\ts\th\tm\ti"
b=a.expandtabs(5)
print(b)
a="Sriam and Murari are good boys. Sriram is 9years"
b=a.index("Sriram")
print(b)
a="Sriram10"
b=a.isalnum()
print(b)
a="SriMurari"
b=a.isalpha()
print(b)
a="12345"
b=a.isascii()
print(b)
b=a.isdecimal()
print(b)
b=a.isdigit()
print(b)
a="12.00"
b=a.isdecimal()
print(b)
a="Sriram_Murari"
c="Murari$"
b=a.isidentifier()
print(b)
d=c.isidentifier()
print(d)
a="Hello Amma Nana"
b=a.maketrans("Amma", "Mumm")
print(a.translate(b)) 
a="  "
b=a.isspace()
print(b)
