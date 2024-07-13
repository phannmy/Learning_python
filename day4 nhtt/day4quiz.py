# viết một chương trình yêu cầu người dùng nhập tuổi.
# nếu như độ tuổi bé hơn 8 thì in ra là trẻ con, 
# bé hơn 18 và lớn hớn 8 thì sẽ là thiếu niên, 
# lớn hơn 18 thì sẽ là người lớn.

tuoi = int(input("how old are you?"))

if tuoi < 8:
    print("you are a child")
elif tuoi >=8 and tuoi <18:
    print("you are a teenager")
elif tuoi >= 18:
    print("you are a adult")
 