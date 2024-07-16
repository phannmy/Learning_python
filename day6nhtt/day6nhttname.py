name = input("Tên: ")
while name == "":
    print("Bạn quên nhập")
    name = input("Hãy nhập lại: ")
print("Chào " + name)