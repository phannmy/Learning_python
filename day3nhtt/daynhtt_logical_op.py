num = int(input())
if num > 50 and num < 60:
    print("This number is between 50 and 60")
elif num == 50 or num == 60:
    print("This number is equal to 50 or 60")
elif not(num == 100 or num == 0):
    print("This number is not equal to 0 or 100")
else:
    print("This number is equal to 0 or 100")