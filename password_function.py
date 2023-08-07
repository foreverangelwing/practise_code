import time
password = '123456'
YES = 'YES'
NO = 'NO'
i = 3
x = 3
while i > 0:
    i = i - 1
    pwd = input('輸入密碼：')
    if pwd == password:
        print('登入成功')
        break
    else: 
        print('密碼錯誤', '還有剩下', i, '次')
        if i == 0:
            while x > 0:
                retry = input('請問要離開還是等待10秒(YES/NO)：')
                retry = retry.upper()
                if retry == YES:
                    print('重需要等待10秒才能再次登入')                    
                    time_left = 10
                    i = i + 3
                    x = 0
                    while time_left > 0:
                        print('倒計時(s):', time_left)
                        time.sleep(1)
                        time_left = time_left - 1                    
                elif retry == NO:
                    break
                else:
                    while x > 0:
                        x = x - 1
                        print('只能輸入YES/NO!')
                        print('還剩', x, '次機會程式就會離開')
                        break
