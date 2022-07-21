#Task:Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements and range() function.

fibonacci = [1, 1]
for i in range(1,56):
    if i == fibonacci[-1] + fibonacci[-2]:
        fibonacci.append(i)
print(fibonacci)