str1=input("Enter string: \n")
str1out=""
count=0
j=0
first = str1[0]
for i in range(len(str1)):
    if str1[i]==first:
        count+=1
    else:
        str1out += first+str(count)
        count = 1
        first=str1[i]
str1out += first+str(count)

print(str1out)