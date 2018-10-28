#coding=utf-8


import os
import sys

'''
一共有个数字1，2，3，4，能组成多少个互不相同的三位数，各是多少
'''

def main(argc, argv, envp):
    for i in [1,2,3,4]:
        for j in [1,2,3,4]:
            for k in [1,2,3,4]:
                if i != j and i != k and j != k:
                    print(i,j,k)
            else:
                pass
        else:
            pass
    else:
        pass


if __name__ == "__main__":
    main(len(sys.argv), sys.argv, os.environ)