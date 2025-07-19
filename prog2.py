'''check if the num is pos , neg or zero'''
def check_number(num):
    if num>0:
        print("positive")
    elif num<0:
        print("negative")
    else:
        print("zero")
check_number(8)


'''print 1-10 using while loop'''
i=1
while i<=10:
    print(i)
    i=i+1


'''take a list of numbers and print only the even numbs'''
numbers=[1,2,3,4,5,6,7]
for num in numbers:
    if num %2==0:
        print(num)

'''fun that return the square of a num'''
def square(num):
    return num*num
result=square(7)
print("square is:",result)


'''sum from 1-100'''
sum=0
for i in range(1,101):
    sum +=i
print(sum)

