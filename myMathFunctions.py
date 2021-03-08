def sqrt_exhaust(a, step, epsilon):
    #local variables 
    x = 0
    count = 0
    
    #loop for stepping thru values
    while abs(a-(x*x)) > epsilon and x*x < a + epsilon:
        x += step
        count += 1
    
    return (x,count)

def sqrt_bisect(a, epsilon):
    #local variables 
    high = a
    low = 0
    x = (high+low)/2
    count = 0

    #loop for stepping thru values 
    while abs(a-(x**2)) > epsilon:
        #shifting high and low points 
        if x**2 < a:
            low = x
        elif x**2 > a:
            high = x
        #updating the return value and counting iterations
        x = (high+low)/2
        count += 1
        
    return (x,count)

def sqrt_NR(a, epsilon):
    