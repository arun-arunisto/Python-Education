"""
    *
   * *
  * * *
 * * * *
* * * * * 
Q1: Pattern program 
"""
#solution 1
def pyramidPattern(n):
    for i in range(n): #<- rows
        #loop for the space
        for j in range(1, n-i): #<- columns
            print(" ", end="")
        #loop for the star with a space
        for s in range(i+1): #<- columns
            print("*", end=" ")
        #for splitting columns
        print()

pyramidPattern(5)
"""
* * * * *
 * * * *
  * * *
   * *
    *
Q2: Reverse pattern
"""
#solution2
def reversePyramid(n):
    for i in range(n): #<- rows
        for j in range(i): #<- space columns
            print(" ", end="")
        for s in range(n-i): #<- star columns with one space
            print("*", end=" ")
        print() #<- splitting columns

reversePyramid(5)

"""
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
Q3: Card pattern
"""
#solution3
def cardPattern(n):
    """
    code for the first half pattern
    **********
    ****  ****
    ***    ***
    **      **
    *        *
    """
    for i in range(n):
        for j in range(n-i):
            print("*", end="")
        for s in range(i):
            print(" ", end=" ")
        for p in range(n-i):
            print("*", end="")
        print()
    """
    Again code for another half
    *        *
    **      **
    ***    ***
    ****  ****
    **********
    """
    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        for s in range(1, n-i):
            print(" ",end=" ")
        for p in range(i+1):
            print("*", end="")
        print()
cardPattern(5)
"""
    0
   1 2
  3 4 5
 6 7 8 9
Q4: numeric pattern
"""
#solution4
def numericPattern(n):
    no = 0
    for i in range(n):
        for j in range(1, n-i):
            print(" ", end="")
        for s in range(i+1):
            print(no, end=" ")
            no+=1
        print()
numericPattern(4)
"""
str = "arunisto"
rev = "otsinura"
Q5: Reverse a string using for loop
"""
#solution5
def reverse(str):
    s = "".join(
        list(
            str[i] for i in range(len(str)-1, -1, -1)
            )
        )
    return s
print(reverse("arunisto"))
"""
li = ["arun", "arunisto", "python"]
reverse = ["python", "arunisto", "arunisto"]
Q6: Reversing a list using for loop
"""
#solution6
def reverseList(list):
    new_li = [list[i] for i in range(len(list)-1, -1, -1)]
    return new_li
print(reverseList(["arun", "arunisto", "python"]))
"""
Function for converting integer to binary
"""
def binaryNumber(num):
    bin_li = []
    half = num
    while half > 0:
        temp = half
        half//=2
        bin_li.insert(0, str(temp%2))
    return "".join(bin_li)
"""
Fibonacci number function
"""
def fibonacciNum(num):
    fib_li = []
    num1 = 0
    num2 = 1
    for i in range(num):
        fib_li.append(num1)
        temp = num1
        num1 = num2
        num2+=temp
    print(*fib_li)
"""
Primenumber or not
"""
def isPrime(num):
    if num < 2:
        return False
    if num > 2:
        for i in range(2, (num//2)+1):
            if num%i == 0:
                return False
    return True
"""
Function for converting binary to integer
"""
def binary2Integer(binary):
    bin_li = []
    for i in range(len(str(binary))-1, -1, -1):
        bin_li.append(str(binary)[i])
    result = 0
    for i in range(len(bin_li)):
        result+=(int(bin_li[i])*(2**i))
    return result
"""
HackerRank day 11: 2D Arrays
"""
li = [[1, 1, 1, 0, 0, 0],
      [0, 1, 0, 0, 0, 0],
      [1, 1, 1, 0, 0, 0],
      [0, 0, 2, 4, 4, 0],
      [0, 0, 0, 2, 0, 0],
      [0, 0, 1, 2, 4, 0]]
#print(li)
sum = 0
tarr = []
r = 0
for l in range(0, 4):
    for k in range(0, 4):
        for i in range(l, l+3):
            #print(f"i:{i}", end="")
            for j in range(k,k+3):
                if i == l+1 and (j == k or j == k+2):
                    #print("i",i,"j",j,"l",l,"k",k)
                    continue
                else:
                    sum+=li[i][j]
        tarr.append(sum)
        sum = 0
print(max(tarr))




