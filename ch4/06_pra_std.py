t1 = int(input ("enter marks of sutdent 1 :"))
t2 = int(input ("enter marks of sutdent 2 :"))
t3 = int(input ("enter marks of sutdent 3 :"))
t4 = int(input ("enter marks of sutdent 4 :"))
t5 = int(input ("enter marks of sutdent 5 :"))

mylist = [t1,t2,t3,t4,t5]

mylist.sort()

print(mylist)
sum = t1+t2+t3+t4+t5
print ("the total sum is",sum)
per = (sum/500)*100
print(per)
