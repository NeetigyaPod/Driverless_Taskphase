ar=(1,2,3,5,6,7,8,9,8,7,6,5,4,3,2,1)
def duplicateremoval(ar):
    end=[]
    duplicate=[]
    for i in range(len(ar)):
        f=0
        for j in range(i+1,len(ar)):
            if(ar[i]==ar[j]):
                duplicate.append(ar[i])
                break
        if(ar[i] not in duplicate):
            end.append(ar[i])
    return tuple(end)
def sum(ar,i=0,ret=0):
    ar=duplicateremoval(ar)
    if i==len(ar):
        return ret
    else:
        return sum(ar,i+1,ret+ar[i])
print(duplicateremoval(ar))
print(sum(ar))