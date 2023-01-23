import argparse
import statistics

parser = argparse.ArgumentParser() #Читаем данные с командной строки
parser.add_argument("a") 
args = parser.parse_args()
a=args.a

nums=[] 
with open(a,'r') as f: #Читаем данные из текстового файла
    contents = f.read()
nums = [int(x) for x in contents.split()] 


x = int(statistics.median(nums)) #Находим значение к которому будем приравнивать
i=0
y=0

while i<len(nums):
    res = int(nums[i])
    while res!=x:
        if res > x:
            res-=1
            y+=1
        elif res<x:
            res+=1
            y+=1
    i+=1
print(y)

