a = [1,2,3,4,5]
result = 0

i = 0
n = len(a)
while i < n:
    result += a[i]
    i += 1  
print(result)

a = [10,2,19,-3,-5]

i = 0
while i < len(a):
    if a[i] < 0:
        break
    print(a[i])
    i += 1
    print(a)


