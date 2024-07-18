# hãy tạo một chương trình nhận 1 số,in từ 0 đến số đó
# và tổng các số đã in
num = int(input("num = "))
sum = 0

for i in range(num+1):
    print(i)
    sum = sum+i
print(sum)