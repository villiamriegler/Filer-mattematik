orgnum = int(input("Enter your number: "))
step = 0.01
epsilon = 0.1
x = 0
count = 0

while abs(orgnum-(x*x)) > epsilon:
    x += step
    count += 1
    
print(x)
print(count)

        