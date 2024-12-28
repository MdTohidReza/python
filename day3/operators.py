# Arithematic operator
a=2
b=2
print(a+b)
print(a-b)
print(a*b)
# division
print(a/b)
# modulus
print(a%b)
# exponentiation
print(a**b)
# floor division
print(a//b)

#assignment operator

x=5
x+=3
print(x)

x-=3
print(x)

x*=3
print(x)


#  comparision operator

a=5
b='5'
c=7
print(a==b)
print(a==int(b))
print(a!=b)
print(a>c)
print(a<c)
print(a>=c)
print(a<=c)


# logical operator
x=2
print(x>3 and x<20)
print(x>3 or x<20)
print (not(x>3 and x<20))

# conditional operator

age = int(input('enter your age'))
if age<=18:
    print('you are eligible for vote')
elif age>=30:
    print('you are too old for vote')
else:
    print('you are too young for vote')


