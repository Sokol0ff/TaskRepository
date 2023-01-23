import math
import argparse

parser = argparse.ArgumentParser() #Читаем данные с командной строки
parser.add_argument("a")
parser.add_argument("b") 
args = parser.parse_args()
a=args.a
b=args.b


data1 =[] 
with open(a, 'r') as f1:
    for line in f1:
        data1.append([int(x) for x in line.split()])
    xy = data1[0]
    radius = data1[1]
    r = radius[0]
    x1=-xy[0]
    y1=-xy[1]


data2 = []
with open (b, 'r') as f2:
    for line in f2:
        data2.append([int(x) for x in line.split()])
 

i=0
data3 = []
while i!=len(data2):
    x=data2[i]
    x2=x[0]
    y2=x[1]
    x2+=x1
    y2+=y1
    gipot = math.sqrt(x2**2 + y2**2)
    if gipot < r:
        data3.append('1')
    elif gipot > r:
        data3.append('2')
    else:
        data3.append('0')
    i+=1
    
print('\n'.join(str(i) for i in data3))

