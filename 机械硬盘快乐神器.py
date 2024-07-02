import os
n=0
while True:
    name = './新建文件夹/'+str(n)
    print(name)
    try:
        os.makedirs(name)
    except:
        print('在创建',name,'时发生错误！')
    n+=1