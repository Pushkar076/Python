#WAp to find out whether a student is pass or fail, if it requires total 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
s= int(input("enter mark sof science:"))
m= int(input("enter mark sof maths:"))
e= int(input("enter mark sof english:"))
total = s+m+e
if (s>33 and m>33 and e>33):
    if total >= 40:
        print("pass")
    else:
        print("fail") 
