import random
import numpy as np


def randomcreatematrix(row, col, lower, upper):  # 随机生成指定行数，列数的矩阵，数值范围在[lower，upper]范围内
    a = np.zeros(shape=(row, col))  # 先建立空矩阵
    for i in range(row):
        for j in range(col):  # 逐个元素生成
            a[i, j] = random.randint(lower, upper)  # 生成数值范围在[lower，upper]内的整数
            # a[i, j] = random.random()*(upper - lower)+lower  # 生成数值范围在[lower，upper]内的实数

    # print(a)
    return a


def randomverificamatrixmultiply(cnt, row, col1, col2, lower, upper):  # 验证矩阵的乘法
    # cnt是验证矩阵相乘的个数 row是第一个矩阵的行，col1是第一个矩阵的列，也是第二个矩阵的行，col2是第二个矩阵的列，
    # lower和upper是矩阵内随机元素的数值范围
    cnt1 = 0  # 通过验证的个数
    cnt2 = 0  # 未通过验证的个数
    for i in range(cnt):
        a = randomcreatematrix(row, col1, lower, upper)  # 随机生成矩阵A
        b = randomcreatematrix(col1, col2, lower, upper)  # 随机生成矩阵B
        c = randomcreatematrix(row, col2, lower, upper)  # 随机生成矩阵C
        # c = np.dot(a, b)
        r = np.random.randint(0, 2, col2).reshape(col2, 1)  # 随机生成col2 x 1的r矩阵，里面的元素是0或1
        # r = np.random.random(col2).reshape(col2, 1)  # 随机生成col2 x 1的r矩阵，里面的元素是[0,1]之间的实数
        # print(r)
        t1 = np.dot(a, np.dot(b, r))  # 先将A，B，r矩阵乘起来
        t2 = np.dot(c, r)  # 再将C，r矩阵乘起来
        if (t1 == t2).all() and ~(c == np.dot(a, b)).all():  # 如果两边矩阵相乘r矩阵后相等，本身相乘并不相等，则通过验证
            cnt1 += 1
            print("通过验证"+str(cnt1))
            # print(a, b, c, r)
        else:  # 没通过验证
            cnt2 += 1
            print("未通过验证"+str(cnt2))
    print("通过验证的个数为"+str(cnt1))
    print("总验证个数为" + str(cnt))
    return

if __name__ == '__main__':
    cnt = 30000  # 总验证个数
    row = 5  # 矩阵A的行
    col1 = 4  # 矩阵A的列和B的行
    col2 = 5   # 矩阵B的列
    lower = 0  # 随机数的下界
    upper = 10  # 随机数的上界
    randomverificamatrixmultiply(cnt, row, col1, col2, lower, upper)

# a = randomcreatematrix(2, 3, 10, 100)
# b = randomcreatematrix(2, 3, 10, 100)
# print(a)
# print(b)
# print((a == b).all())  # 用来比较两个matrix是否相等
