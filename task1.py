import sys
import argparse

parser = argparse.ArgumentParser() #Читаем данные с командной строки
parser.add_argument("n")
parser.add_argument("m") 
args = parser.parse_args()
n = int(args.n)
x = int(args.n)
m = int(args.m)

n = list(range(1,n+1)) #Создаем круговой список
n=n*m

n=n[::m-1] #Определяем путь
n=n[:x]
print(''.join(str(i) for i in n))
