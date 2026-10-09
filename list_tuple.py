a = [1,2,3, 'Naim', 'fahim',8.9,3.4]
a[0] = 100
print(a)
print(a[-1])
print(len(a))
#s = "Hello"--> ["H","e","l","l","o"]
s = "Hello"
print(list(s))
a.append(['Ishtiak'])
print(a.index(3))
a.reverse()
print(a)
#tuple ---> immutable
t=(1,2,3,'Naim','fahim',8.9,3.4)
#t[0] = 100
t_r = tuple(reversed(t))
print(t_r)
print(t)



