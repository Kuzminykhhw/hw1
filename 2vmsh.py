def f(a):
    c=0
    for i in a:
        c=c+int(i)
    return c/len(a)
def g(a):
    d=1
    for i in a:
        d=d*int(i)
    return d**(0.5)
def k(a):
    m=0
    for i in a:
        m=m+int(i)**2
    return m**(0.5)
def j(a):
    print(f(a), g(a) , k(a))
a=input().split()
print(j(a))
    
