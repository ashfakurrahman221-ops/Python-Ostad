# {} → dictionary
# key-value pair
# indexing er sujog nai
# key gulo obossoi immutable

a = {
    'rahim': 12,
    'karim': 15,
    'jamal': 10,
    1: [1, 2, 3, 4],
    2: [3, 4, 5]
}

print(type(a))

# print only keys
for i in a:
    print(i)

print("------------------")

# print only values
for i in a.values():
    print(i)

print("------------------")

# print key and value together
for k, v in a.items():
    print(f"key name: {k}, value: {v}")

print("------------------")

# zip example
a = [1, 2, 3]
b = ["mango", "banana", "orange"]

print(dict(zip(a, b)))
