#viết một chương trình với một biến, và so sánh biến đấy với 
# 60(so sánh lớn hơn, bé hơn, hoặc là bằng 60)

num = int(input("What number: "))

if num > 60:
    print("this number is larger than 60")
elif num < 60:
    print("this number is smaller 60")
elif num == 60:
    print("this number is equal to 60")
else: 
    print("this variable does not fit the requirement")