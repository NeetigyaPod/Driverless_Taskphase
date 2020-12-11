ar=[[1,2,3],[4,5,6]]
ar2=[[9,7],[6,5],[4,3]]
def display(ar):
    for i in range(len(ar)):
        for j in range(len(ar[0])):
            print(ar[i][j],end=' ')
        print()
def multiply(ar, ar2):
    result=[]
    r1=len(ar)
    r2=len(ar2)
    c1=len(ar[0])
    c2=len(ar2[0])
    for i in range(r1):
        temp=[]
        for seccol in range(c2):
            sum=0
            for col in range(c1):
                sum+=ar[i][col]*ar2[col][seccol]
            temp.append(sum)
        result.append(temp)
    return result
def transpose(ar):
    result=[]
    for i in range(len(ar[0])):
        temp=[]
        for j in range(len(ar)):
            temp.append(ar[j][i])
        result.append(temp)
    return result
def verification(ar,ar2):
    lhs=transpose(multiply(ar,ar2))
    rhs=multiply(transpose(ar2),transpose(ar))
    display(lhs)
    print('=')
    display(rhs)

multiply(ar,ar2)
transpose(ar)
verification(ar,ar2)

