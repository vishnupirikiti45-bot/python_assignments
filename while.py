# find all two numbers eual to twice the sum of their digits and multiped by 3

for i in range(10,100):

    total = (i//10) + (i%10)

    if total * 2 * 3 == i :
        print(i)

# # find all number between 100 and 999 whose digits are increasing order 

for i in range(100,1000):
    a = i // 100
    b = (i // 10) % 10
    c = i % 10

    if a < b < c:
        print(i)

# find a number that becomes 4 times itself when its digita are reversed

for i in range(1000,10000):
    res = int(str(i)[::-1])

    if res == i * 4 :
        print(res)

# check wheather a number is a harshad number(divisibe the sum of its digit)

n = int(input("enter a number = "))
temp = n
total = 0
while n > 0:
    total += (n%10)
    n = n // 10
if temp % total == 0:
    print("harshad number")
else:
    print("not harshad number")

# # find all pair of numbers between 1 and 100 whose sum equals their product

for i in range(1,101):
    for j in range(1,101):
        if i + j == i * j:
            print(i,j)
    





