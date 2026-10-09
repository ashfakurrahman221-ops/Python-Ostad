print(10%3)
a = [1,10,23,24,26,90]
result = []
for i in a:
    if i%2 ==0:
        result.append(i)
print(result)
#list comprehension
result2 = [i for i in a if i%2==0]
print(result2)
b =[1,2,3,4,5,6,7,8,9,10]
b_new = [i**2 if i%2 == 0 else i for i in b]
print(b_new)
c = [i*j for i in range(1,4) for j in range(1,4)]
print(c)

nums = list(range(0,11))
result ={i: "Even" if i%2 ==0 else "Odd" for i in nums}
print(result)