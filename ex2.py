sum=0
print("Which Question?")
question=input()

if question=='1':
    while True:
        list_input = input("Enter number until stop:")
        if list_input == 'stop':
            break
        else:
            sum = int(sum) + int(list_input)
    print("The sum of the list is:" + str(sum))

if question=='2':
    list_input = input("Enter numbers with comma:")
    withoutcomma=list_input.split(",")
    for num in withoutcomma:
        if num!=',':
            sum=sum+int(num)
print("The sum of the list is:" + str(sum))
