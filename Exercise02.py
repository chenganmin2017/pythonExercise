#coding=utf-8


import sys
import os

'''
企业发放的奖金根据利润提成，利润低于或等于10万元时，奖金可提成10%，利润高于10万元，低于20万元时，
低于10万的部分按10%提取，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万的部分，可提成
5%；40万到60万之间高于40万元的部分，可提成3%；60万到100万之间的，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润，求应发放奖金总额？
'''

arr = [1000000, 600000, 400000, 200000, 100000, 0]
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
Commission = 0

def main(argc, argv, envp):

    global Commission
    try:
        profit = int(input("输入你的利润:"))
        for idx in range(0,6):
            if profit > arr[idx]:
                Commission += ((profit -arr[idx]) * rat[idx])
                profit = arr[idx]
        else:
            pass
    except ValueError:
        print("您输入的利润有错误")

    print("您的提成为: ", Commission)


if __name__ == "__main__":
    main(len(sys.argv), sys.argv, os.environ)