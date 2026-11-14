# find all two numbers eual to twice the sum of their digits and multiped by 3

n = 10
total = 0

while n <= 100:
    total = (n // 10) + (n % 10)
    if n == 2*total*3:
        print(n)
        break
    else:
        n = n + 1


# # # find all number between 100 and 999 whose digits are increasing order 

# n = 100

while n <= 1000:
    a = n // 100
    b = (n // 10) % 10
    c = n % 10

    if a < b < c:
        print(n,end=" ")
    
    n += 1


# # find a number that becomes 4 times itself when its digita are reversed

for i in range(1000,10000):
    res = int(str(i)[::-1])

    if res == i * 4 :
        print(res)

# # check wheather a number is a harshad number(divisibe the sum of its digit)

n = int(input("enter a number = "))
temp = n
total = 0
while n > 0:
    total += (n%10)
    n = n // 10
if temp > 0 and temp % total == 0:
    print("harshad number")
else:
    print("not harshad number")

# # # find all pair of numbers between 1 and 100 whose sum equals their product

i = 1

while i <= 100:
    j = 1

    while j <= 100:
        if i + j == i * j:
            print(i, j)
        j += 1
    i += 1
    





