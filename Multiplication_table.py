#99乘法口诀表，参考网上写法
for i in range(1,10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(i, j, i*j), end='')
    print()   