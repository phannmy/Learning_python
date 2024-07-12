#đặt 1 biến bất kì. hãy viết một đoạn code cho ta biết số này có lớn hơn 20 hay nhỏ hơn 20 
#hoặc là bằng 20
import random
num1 = random.randint(0,100)
print(num1)
if num1 >20:
    print("this number is larger than 20")
elif num1 <20:
    print("this number is smaller than 20")
else:
    print("this number is equal to 20")
    