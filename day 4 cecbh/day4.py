truepass = input("set a passwork: ") #đặt mật khẩu
checkpass = input("please enter a password")#nhập mật khẩu

while checkpass != truepass:    # while điều kiện:
    print("wrong password")     #nếu điều kiện vẫn còn đúng thì
    checkpass = input("please retry:") #nó sẽ chạy rồi lặp lại
                                        #đến khi nào điều kiện
                                        #sai thì thôi    
print("access granted")


#yêu cầu người dùng đặt tên, tuổi, và một mật khẩu.
# sau đó cho họ nhập lại một lần nữa rồi kiểm tra xem
# 2 thông tin này có giống nhau không, khi nào có thì 
# in ra là đúng

#biết rằng dấu != là dấu kiểm tra xem 2 số có khác nhau không