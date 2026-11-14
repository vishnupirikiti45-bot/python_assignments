# Write a function that receives an integer n and prints all its factors (including 1 and n).

n = int(input("Enter a number = "))
for i in range(1,n+1):
    if n % i == 0:
        print(i,end=",")

# Write a function that receives two integers n and m (n ≤ m) and 
# prints the count of even numbers in the inclusive range [n, m].

n = int(input("Enter a value = "))
m = int(input("Enter a value = "))
count = 0
if n <= m:
    for i in range(n,m):
        if i % 2 == 0:
            count += 1
    print(count)
else:
    print("Enter a valid numbers")

# Write a function that receives an integer n and 
# prints all odd numbers from 1 up to n (inclusive).

n = int(input("Enter a value = "))
for i in range(1,n):
    if i % 2 == 1:
        print(i,end=",")


# Write a function that receives two integers n and m (n ≤ m) and prints two counts:
# the number of integers in the range [n, m] that are divisible by 2,
# the number of integers in the same range that are divisible by 3.

n = int(input("Enter a value = "))
m = int(input("Enter a valu = "))
count = 0
res = 0
if n <= m:
    for i in range(n,m):
        if i % 2 == 0:
            count += 1
        elif i % 2 == 1:
            res += 1
    print("divisible by 2 count = ",count)
    print("divisible by 3 count = ",res)
else:
    print("Enter a vaild numbers")