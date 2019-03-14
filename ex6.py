def map(function,list):
    for i in range(len(list)):
        list[i]=function(list[i])
    return list

def multi(num):
    return num*2


x=[1,2,3]
print(map(multi,x))