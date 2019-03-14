def calc_sum(id):
    str(id)
    sum_For_checkDigit = 0
    more_than_nine=0
    #sum of the digits exept check digit
    for i in range(len(id)-1):
        if i%2==0:
            sum_For_checkDigit=sum_For_checkDigit + int(id[i])
        else:
            if int(id[i])>4:
                more_than_nine=int(id[i])*2
                more_than_nine=more_than_nine%10+more_than_nine/10
            sum_For_checkDigit=sum_For_checkDigit+ more_than_nine

    return 10-sum_For_checkDigit%10

idNumber=input("Enter an ID and I wil tell if it is correct!")
if calc_sum(idNumber)==str(id[9]):
    print("The idNum is correct")
else:
    print("The id num is not correct")