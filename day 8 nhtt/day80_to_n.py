# hãy tạo ra một chương trình chấp nhận một số từ người dùng
# rồi sau đó sử dụng for loop để in từ số đó đến 0
num = int(input("number: "))
for i in range(num, -1,-1): #(start, stop, step)
    print(i)