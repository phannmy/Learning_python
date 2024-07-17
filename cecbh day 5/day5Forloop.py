# hãy tạo ra một chương trình chấp nhận một 
# số từ người dùng rồi sau đó sử dụng for loop 
# để in từ 0 đến số đó và tổng của các số này


num = int(input("number: "))
sum = 0
for i in range(0,num+1):
    print(i)
    sum = sum+i
print(sum)