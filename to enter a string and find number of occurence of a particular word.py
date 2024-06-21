#program to enter string and find the number of occurance of any word
line=input("enter the line : ")
sub=input("enter the substring : ")
length=len(line)
lensub=len(sub)
start=count=0
end=length
while True:
    pos=line.find(sub,start,end)
    if pos!=-1:
        count+=1
        start=start+pos+lensub
    else:
        break
    if start>=end:
        break
print("\n Number of occurence of",sub,':',count)
