# yêu cầu người dùng đặt tên, tuổi, và một mật khẩu.
# sau đó cho họ nhập lại một lần nữa rồi kiểm tra xem
# 2 thông tin này có giống nhau không, khi nào có thì
# in ra là đúng

# biết rằng dấu != là dấu kiểm tra xem 2 số có khác nhau không


set_name = input("Set name: ")
set_age = int(input("Set age: "))
set_password = input("Set password: ")

name = input("retype name: ")
age = int(input("retype age: "))
password = input("retype password: ")
while name != set_name or age != set_age or password != set_password:
    print("Retry")
    name = input("retype name: ")
    age = int(input("retype age: "))
    password = input("retype password: ")
print("Access granted!")