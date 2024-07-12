# hãy tạo ra một chương trình chấp nhận 1 biến, kiểm tra xem các biến này có lớn hơn 100, bé hơn 100, hay bằng 100
num1 = int(input("number?"))

if num1 > 100:
    print("this number is larger than 100")
elif num1 < 100:
    print("this number is smaller than 100")
else:
    print("this number is equal to 100")
