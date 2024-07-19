# hãy tạo một chương trình nhận 1 số,in từ 0 đến 
# số đó và tổng các số đã in
num = int(input("N = "))
sum = 0

for i in range(0,num+1):
    print(i)
    sum += i
print(sum)