#coding=utf-8
import time
#EAN A电梯的当前层数， EBN B电梯的当前层数
#targetA    A的目标层数      targetB    B的目标层数


'''
def TA(targetA,EAN):
    if targetA>EAN:         #电梯上升
        while EAN != targetA:
            time.sleep(1)
            EAN = EAN + 1
            print("电梯A的当前层数：%d↑" % EAN)

    elif targetA<EAN:        #电梯下降
        while EAN != targetA:
            time.sleep(1)
            print("电梯A的当前层数：%d↓" % EAN)
            EAN = EAN - 1
    print("电梯已到达%d" % EAN)
    return EAN


def TB(targetB,EBN):
    if targetB>EBN:         #电梯上升
        while EBN != targetB:
            time.sleep(1)
            EBN = EBN + 1
            print("电梯B的当前层数：%d↑" % EBN)

    elif targetB<EBN:       #电梯下降
        while EBN != targetB:
            time.sleep(1)
            print("电梯B的当前层数：%d↓" % EBN)
            EBN = EBN - 1
    print("电梯已到达%d" % EBN)
    return EBN
'''

def chooseAB(To,EAN,EBN):       #选择电梯˚    if  abs(To-EAN)>abs(To-EBN):    #选择B电梯
        if To > EBN:  # 电梯上升
            while EBN != To:
                time.sleep(1)
                EBN = EBN + 1
                print("电梯B的当前层数：%d↑" % EBN)

        elif To < EBN:  # 电梯下降
            while EBN != To:
                time.sleep(1)
                EBN = EBN - 1
                print("电梯B的当前层数：%d↓" % EBN)
        print("电梯已到达%d" % EBN)
        return EBN

    elif    abs(To-EAN)<=abs(To-EBN):       #选择A电梯
        if To > EAN:  # 电梯上升
            while EAN != To:
                time.sleep(1)
                EAN = EAN + 1
                print("电梯A的当前层数：%d↑" % EAN)

        elif To < EAN:  # 电梯下降
            while EAN != To:
                time.sleep(1)
                EAN = EAN - 1
                print("电梯A的当前层数：%d↓" % EAN)
        print("电梯已到达%d" % EAN)
        return EAN

EAN=6
EBN=1

while True:
    To=int(input("输入到达层数："))#输入要到达的层数
    EAN = chooseAB(To,EAN,EBN)







