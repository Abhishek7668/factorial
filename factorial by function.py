def factorial(a):
    c = 1
    for i in range(1,a+1):
        c*=i
    return(c)
a = 5
print(factorial(a))
