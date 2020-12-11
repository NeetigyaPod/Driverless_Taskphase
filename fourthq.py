import csv
import operator
text=csv.reader(open('names.csv'),delimiter=',')
temp=next(text,None)
sort=sorted(text,key=operator.itemgetter(0))
print(sort)
#ls is final file names list
ls=[]
with open('Sortednames.csv','w',newline='') as new:
    filewr=csv.writer(new)
    filewr.writerow(temp)
    for i in zip(range(len(sort)),sort):
        if(i[0]%2==0):
            filewr.writerow(i[1])
            ls.append(i[1][1])
print(ls)
nameconc=''
dif=1e8
for st in ls:
    nameconc=nameconc+st
for i in range(len(nameconc)):
    for j in range(i+1,len(nameconc)):
        if(nameconc[i].isalpha() and nameconc[j].isalpha() and nameconc[i]!=nameconc[j]):
            dif=min(dif,abs(ord(nameconc[i])-ord(nameconc[j])))
print(dif)

# with open('names.csv','w') as names:
#     columns=['number','name']
#     writer=csv.DictWriter(names,fieldnames=columns)
#     writer.writeheader()
#     writer.writerow({'name':'Neetigya','number':2})
#     writer.writerow({'name':'Katy Perry','number':1})