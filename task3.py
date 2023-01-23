import argparse
parser = argparse.ArgumentParser() #Читаем данные с командной строки
parser.add_argument("tests")
parser.add_argument("value") 
args = parser.parse_args()
tests=args.tests
value=args.value

file1=[]
data1=[]
with open(value,'r') as f1:
    for line in f1:
        file1 = [line.rstrip() for line in f1]
with open(value,'r') as f1:
    for line in f1:    
        data1.append([x for x in line.split() if '"id"' in line])


file2=[]
data2=[]
with open(tests,'r') as f2:
    for line in f2:
        file2 = [line.rstrip() for line in f2]
with open(tests,'r') as f2:
    for line in f2:    
        data2.append([x for x in line.split() if '"id"' in line])

i=0 #Находим индекс строк id
idindex1=[]
idindex2=[]
while i<len(data2):
    if data2[i] in data1:
        idindex1.append(data1.index(data2[i]))
        idindex2.append(data2.index(data2[i]))
    i+=1
idindex1= list(filter(None,idindex1))
idindex2= list(filter(None,idindex2))

with open('report.txt', 'w+') as f2: #Запись результатов в файл
    i=0
    x=0
    y=0
    while i<len(file2):
        try:
            xid=int(idindex2[x]-1)
            yid=int(idindex1[y]-1)
        except:
            pass
        if i == xid:
            if data2[xid] == data1[yid]:
                fix_p=len(file2[i+2])-len(file2[i+2].lstrip(' '))-4 #Устанавливаем правильное кол-во пробелов
                f2.write(file2[i]+'\n'+file2[i+1]+'\n'+' '*fix_p+file1[yid+1]+'\n')
                y+=1
                x+=1
                i+=3
            else:
                f2.write(file2[i]+'\n')
                i+=1
        else:
            f2.write(file2[i]+'\n')
            i+=1 
