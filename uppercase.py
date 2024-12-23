

txt=input("Enter Text")
s=''
x=txt.split()
for i in x:
  if i !='and' and i!='or' and i!='of':
    s+=i[0].upper()
print(s)
