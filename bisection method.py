orgnum = int(input("Enter your number: "))
high = orgnum
low = 0
epsilon = 0.1
x = (high+low)/2
count = 0

while abs(orgnum-(x**2)) > epsilon:
    count += 1
    if x**2 < orgnum:
        low = x
    elif x**2 > orgnum:
        high = x
    x = (high+low)/2

print(x)
print(count)

        