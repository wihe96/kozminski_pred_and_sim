#Print First 10 natural numbers using while loop
a = 1
while a < 11:
    print(a)
    a += 1

#Exercise 2: Print the following pattern
b = []
c = 1
for i in range(5):
    b.append(c)
    c += 1
    print(b)

#Exercise 3: Calculate the sum of all numbers from 1 to a given number
number = int(input("Enter a number "))  
s = []
for i in range(number+1):
 s.append(i)

print("sum is", sum(s))   

#Exercise 4: Write a program to print multiplication table of a given number
number = int(input("Enter a number "))  
m = []
for i in range(1,11,1):
    m.append(number*i)
print(m)

