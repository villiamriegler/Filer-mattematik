def solvePolyNR(a,b,c,d,e, q, epsilon = 0.001):
    #a*x**4+b*x**3+c*x**2+d*x+e
    #(4*a*x**3)+(3*b*x**2)+(2*c*x)+d
    
    x = q
    
    while abs(a*x**4+b*x**3+c*x**2+d*x+e) > epsilon:
        x = x-((a*x**4+b*x**3+c*x**2+d*x+e)/((4*a*x**3)+(3*b*x**2)+(2*c*x)+d))
        
    return x

print(solvePolyNR(0,0,2,-4,0,))