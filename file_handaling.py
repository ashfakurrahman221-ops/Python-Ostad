import os.path
# # file = open('name.txt','r')
# # content =file.read()
# # print(content)
# # file.close()
# with open('name.txt','r') as f:
#  content = f.read()
#  print(content)
#  with open('name.txt','a') as f:
#     f.write('hello world\n')
#     f.write("i am learning python\n")

# lines = ['hello moon world\n','i am new to learning python\n']
# with open('name.txt','a') as f:
#     f.writelines(lines)
if os.path.exists('name.txt'):
    with open('name.txt','r') as f:
        content = f.read()
        print(content)