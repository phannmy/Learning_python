# Hãy tạo một chương trình nhận một số và in từ số 0 đến
# số đó và in tổng các số vừa in
n = int(input("Hayx nhập một số: "))
index = 0
sum = 0
while index <= n:
    sum= sum + index
    print(index)
    index= index + 1
print(sum)