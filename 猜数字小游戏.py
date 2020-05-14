import random

number = random.randrange(1,100)
runing = True

while runing:
    guess = int(input("数字是(1~100):"))

    if guess == number:
        print("猜对了!!")
        runing = False

    elif guess < number:
        print("猜小了")

    else:
        print("猜大了")