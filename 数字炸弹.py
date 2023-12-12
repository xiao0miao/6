import time
import random
#print("欢迎使用本程序！这是xiao0miao在家里不想学习原神无聊随便写的")
for w in range(114514):
    q = int(input("请输入炸弹最小值："))
    p = int(input("请输入炸弹最大值："))
    boow = random.randint(q,p)
    #print(boow)
    for n in range(114514):
        print(q,"到",p)
        i = int(input())
        if i>=q and i<=p:
            if i == boow:
                print("哎！别碰那个炸弹！我可不爆炸他不会爆炸！")
                print("3秒后进入下一局")
                time.sleep(3)
                break
            else:
                if i>=q and i<boow:
                    q = i
                else:
                    if i<=p and i>boow:
                        p = i
        else:
            print("你™故意找茬是不是啊")
            print(q,"到",p)
