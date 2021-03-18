import random
print("1-100数字猜谜游戏")
num = random.randint(1, 100)
guess = "guess"
i = 0
while guess != num:
    i += 1
    guess = int(input("请输入你猜的数字:"))

    if guess == num:
        print("恭喜，你猜对了！")
    elif guess > num:
        print("你猜的数大了")
    else:
        print("你猜的数小了")
print("你一共猜了%d" % i + "次，快和你的朋友比试一下吧！！")
