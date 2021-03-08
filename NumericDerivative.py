def derivative(f,x,h = 0.001):
    df = (f(x+h)-f(x))/h
    
    return df

inf = input('Ange funktion: ')
x = int(input("Ange en punkt: "))
f = lambda x: eval(inf)

print(derivative(f,x))