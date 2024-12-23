
n=int(input("enter number of modules"))
marks=[]
for i in range(n*2):
    e=int(input("Enter marks"))
    marks.append(e)
print(marks)

t=0
for j in range(0,n*2,2):
    if marks[j] >= marks[j+1]:
        t=t+marks[j]
    else:
        t=t+marks[j+1]
print("total mark=",t)
