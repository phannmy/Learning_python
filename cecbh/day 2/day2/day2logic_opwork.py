# viết một chương trình yêu cầu người dùng nhập 2 biến. 
# sau đó check xem 2 biến này có bằng 100 không,
# có bé hơn 100 không, và một trong 2 biến có bằng 100 không?
num1 = int(input("first number: "))
num2 = int(input("second number:"))

if num1 > 100 and num2 >100:
    print("both number is larger than 100")
elif num1 < 100 and num2 <100:
    print("both number is smaller 100")
elif num1 == 100 or num2 ==100:
    print("one of the 2 number is equal to 100")
else:
    print("these variable do not fit the requirement")
