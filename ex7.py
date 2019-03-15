decorator_cache={}
def fibbonaci(n):
    if n < 2:
        return n
    if n in decorator_cache:
        return decorator_cache[n]
    temp=fibbonaci(n-1) + fibbonaci(n-2)
    decorator_cache[n]=temp
    return temp


print(fibbonaci(12))
print(decorator_cache)

