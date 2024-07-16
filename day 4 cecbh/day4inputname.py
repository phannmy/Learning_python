# yêu cầu người dùng nhập tên, nếu ko nhập gì sẽ bắt người 
# dùng nhập lại

name = input("your name is: ")

while name == "":
    name = input("please enter your name: ")
    
print("your name is "+ name)