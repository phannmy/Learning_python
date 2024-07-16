# hãy viết một chương trình nhận hai số và in ra tổng của hai số đến khi nào nhập hai số bang 0

number1 = int(input("Number: "))
number2 = int(input("Number: "))
while number1 != 0 and number2 != 0:
    print("Sum: " + str(number1 + number2))
    number1 = int(input("Number: "))
    number2 = int(input("Number: "))
