#  while loop

while True:
    print("enter your name")
    name = (input())
    if name =='stop':
        break



i=0
while i<=10:
    print(f" {i}Hello")
    if i==5:
        break
    i+=1
    
    
# for loop

fruits=['apple','banana','mango','orange',123,1.2]
print("apples" in fruits)
for index ,fruit in enumerate(fruits):
    print(index+1,fruit)


# range function

print(type(range(10)))

numbers = list(range(1,10,2))
print(numbers)


for i in range(10):
    print(i)
    if i==3:
        break