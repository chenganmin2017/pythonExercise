#coding=utf-8

import sys
import os


'''
水仙花数：
  指一个三位数，其各位数字立方和等于该数本身，
  例如：153是一个'水仙花数', 153=1³ + 5³ + 3³ = 153
'''

def funStyle_1()->None:
    '''
    方式1
    '''
    for i in range(1, 10):
        for j in range(0, 100):
            for k in range(0, 100):
                if pow(i,3) + pow(j,3) + pow(k,3) == i * 100 + j * 10 + k:
                    print("The data is {}{}{}".format(i, j, k))
            else:
                pass
        else:
            pass
    else:
        pass


def funStyle_2()->None:
    '''
    方式2
    '''
    for date in range(100,1000):
        bai = date // 100
        shi = date % 100 // 10
        ge = date % 10
        if pow(bai,3) + pow(shi,3) + pow(ge,3) == date:
            print("The data is {}".format(date))
    else:
        pass



def main(argc, argv, envp):
    funStyle_1()
    print('---------------')
    funStyle_2()



if __name__ == "__main__":
    sys.exit(main(len(sys.argv), sys.argv, os.environ))
