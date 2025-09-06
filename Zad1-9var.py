import math

a,b=map(int,input().split())
a1=math.radians(a)
b1=math.radians(b)
z1=(math.cos(a)-math.cos(b))**2-(math.sin(a)-math.sin(b))**2
a2=math.radians((a-b)/2)
b2=math.radians(a+b)
z2=(-4)*(math.sin(a2))**2*math.cos(b2)
print(format(z1,'.2f'),format(z2,'.2f'))