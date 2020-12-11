sampleq=['a','b','b','c','a']
def convert_to_Hex(num):
    n=""
    while num>0:
        n=( chr(64+num%16-9) if num %16>9 else chr(48+num%16))+n
        num=int(num/16)
    return int(n)
def pal(ar,cop=[]):
    if(len(ar)==1 or len(ar)==0):
        return True
    elif (not ar[0]==ar[-1]):
        return False
    else:
        return pal(ar[1:-1],cop)
def task(ar):
    if pal(ar):
        print( [convert_to_Hex(ord(x)) for x in ar])
    else:
        for i in range(len(ar)):
            for j in range(len(ar)-i-1,0,-1):
                print(" ", end="")
            for j in range(i+1):
                print(ar[j],end="")
            for j in range(i):
                print(ar[j],end="")
            print()
        for i in range(len(ar)-2,-1,-1):
            for j in range(len(ar)-i-1,0,-1):
                print(" ", end="")
            for j in range(i+1):
                print(ar[j],end="")
            for j in range(i):
                print(ar[j],end="")
            print()
task(['F','M','D'])
task(sampleq)
task(['a','b','a'])