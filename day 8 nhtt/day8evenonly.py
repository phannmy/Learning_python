#hãy tạo một chương trình chấp nhận một số rồi sau đó in các số chẵn 
# từ 0 đến số đó phải sử dụng for loop và làm 2 trường hợp 
# có if và không có if
#dấu chia để tìm số dư 
#là %
#num = int(input("number: "))


#for i in range(1,num+1,2): #(start,end,step)
  # print(i)
 

num = int(input("Number: "))

for i in range(num+1):
    if i % 2 == 1:
        print(i)