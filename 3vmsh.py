def f(x1, y1, x2, y2, x3, y3):
    a=((x1-x2)**2+(y1-y2)**2)**(0.5)
    b=((x1-x3)**2+(y1-y3)**2)**(0.5)
    c=((x3-x2)**2+(y3-y2)**2)**(0.5)
    if a+b>c and a+c>b and b+c>a:
        print("Да")
    else:
        print("нет")

x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
x3=int(input())
y3=int(input())
print(f(x1, y1, x2, y2, x3, y3))
