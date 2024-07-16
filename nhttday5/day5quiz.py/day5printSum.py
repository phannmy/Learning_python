# hãy tạo một chương trình nhận các số, đến khi nào người dùng input 0, sau đó in ra tổng các số vừa nhập

num =int(input())
sum = 0 
while num != 0:
    sum  = num + sum
    num = int(input())
print(sum)
