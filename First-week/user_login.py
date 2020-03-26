#2019-03-26 by wangjun 
#用户登录验证尝试三次
user = 'u1'
password = 'pwd1'
#u = input('用户：')
#p = input('密码')
for i in range(3):
    if input('user:') == user:
        if input('password:') == password:
            print('登录成功')
            break
    else:
        print('用户名或密码错误')