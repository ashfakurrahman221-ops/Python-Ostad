a = [1, 2, 3, 4, "a", 5, 6, 7]
print(type("a"))
for i in a:
    if type(i) == str:
        break #stop the loop
    else:
        print(i)
print("------------------")
for j in a:
    if type(j) == str:
        continue #skip the current iteration
    else:
        print(j)
