#hãy tạo một trương trình chấp nhận một số rồi sau đó in các số chẵn từ 0 đến số đó 
#phải sử dụng for loop và làm 2 trường hợp có if và không có if
#dấu chia để tìm số dư là %

a = int(input("a = "))
for i in range(0,a+1):
    if i % 2 == 0:
        print(i)
        