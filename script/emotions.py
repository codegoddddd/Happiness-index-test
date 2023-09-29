#Quick sort
def partition(a,start,end):
    pivot=a[end]
    pindex=start
    
    for i in range(start,end):
        if a[i]<pivot:
            a[i],a[pindex]=a[pindex],a[i]
            pindex=pindex+1            
    a[end],a[pindex]=a[pindex],a[end]
    return pindex       
    
def qs(a,start,end):
    if start<=end:
        pindex=partition(a,start,end)
        qs(a,start,pindex-1)
        qs(a,pindex+1,end)
    
A=input("Enter the percentages:\n")
a=A.split(",")
start=0
end=len(a)-1
qs(a,start,end)
print("Sorted percentages : ")
print(a)
print("Top five percentages : ")
for i in range(len(a)-1,len(a)-6,-1):
    print(a[i])