
print("welcome to 4'th sem GPA calculator")
sub_name=["ALG","AIML","TOC","IOS","DBMS","EVS","IOS LAB","DBMS LAB"]
grade={"o":10,"A+":9,"A":8,"B+":7,"B":6,"u":0}
print("Grades & credits are ",grade)
print()
credit=[4,4,3,3,3,2,1.5,1.5]
get_credit=[]
get_grade=[]
tot_cred=0
for i in range(0,len(sub_name)):
        s=input("Enter Your "+sub_name[i]+" grade:")
        get_grade.append(s)
        get_credit.append(grade[s])
for i in range(len(sub_name)):
    tot_cred+=get_credit[i]*credit[i]
a=tot_cred/(sum(credit))
print("You got ",round(a,2),"GPA") 
if(a>=8.5):
    print("you are eligible for distinction")
elif(a>=6.5 and a<8.5):
    print("you are eligible for first class")
else:
    print("second class")
        

