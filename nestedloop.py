
# Multiplication Table Generator
# Write a function multiplication_table(n: int) -> List[List[int]] 
# that returns a two‑dimensional list representing an n × n multiplication table.
# Each inner list corresponds to a row, where the element at column j (0‑based) equals (i+1) * (j+1).


n = int(input("Enter a value = "))
res = []
for i in range(n):
    row = []
    for j in range(n):
        total = (i+1) * (j+1)
        row.append((total))
    res.append(row)
print(res)

# Pattern Printing – Right‑Aligned Triangle
# Implement a function right_aligned_triangle(height: int) -> List[str] 
# that returns a list of strings, each string representing 
# a line of a right‑aligned triangle made of asterisk (*) characters. 
# The first line contains one asterisk right‑aligned to the width height,
#  the second line contains two, and so on until height asterisks.

n =int(input("Enter a value = "))

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()
    

# Unique Pair Sum Finder
# Create a function pair_sums(nums: List[int]) -> Set[Tuple[int, int]] 
# that returns a set of all unique ordered pairs (a, b) from nums 
# where a < b and a + b is an even number. 
# Use nested loops to examine each combination of two distinct elements.

def pair_sums(nums: List[int]) -> Set[Tuple[int, int]]:
    res = set()
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            a = nums[i]
            b = nums[j]
            if a < b and (a + b) % 2 == 0:
                res.add((a,b))
    return res

nums = list(map(int, input("Enter values: ").split()))
res = pair_sums(nums)
print(set(res))

# Matrix Diagonal Difference
# Develop a function diagonal_difference(matrix: List[List[int]]) -> int 
# that computes the absolute difference between the sums of the primary diagonal (top‑left to bottom‑right) and 
# the secondary diagonal (top‑right to bottom‑left) of a square matrix. 
# Use nested loops to traverse the matrix and accumulate the two sums.

def diagonal_difference(matrix: List[List[int]]) -> int:
    n = len(matrix)
    primary_sum = 0
    secondary_sum = 0

    for i in range(n):
        for j in range(n):
            if i == j:
                primary_sum += matrix[i][j]
            if i + j == n - 1:
                secondary_sum += matrix[i][j]
    return abs(primary_sum - secondary_sum)

matrix = [[11, 72, 73],
          [43, 65, 56],
          [79, 38, 19]
          ]

print(diagonal_difference(matrix))










