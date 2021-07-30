# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 11:15:15 2021

@author: nitac
"""

dic={'apple':'蘋果','bread':'麵包','celebrate':'慶祝','docter':'醫生','elevator':'電梯','feather':'羽毛','gorgeous':'華麗的','harness':'馬具','igloo':'冰屋','judge':'法官'}
print('單字:')
print('1.apple','2.bread','3.celebrate','4.docter','5.elevator','6.feather','7.gorgeous','8.harness','9.igloo','10.judge')
x=dic['apple']
x2=dic['bread']
x3=dic['celebrate']
x4=dic['docter']
x5=dic['elevator']
x6=dic['feather']
x7=dic['gorgeous']
x8=dic['harness']
x9=dic['igloo']
x10=dic['judge']

y=('功能')
while y!='c':
    print('----------------------')
    print('(a)查單字')
    print('(b)測驗')
    print('(c)離開系統')
    y=input('請選擇功能:')
    print('----------------------')
    if y=='a':
        print('1.apple','2.bread','3.celebrate','4.docter','5.elevator','6.feather','7.gorgeous','8.harness','9.igloo','10.judge')
        z=input('輸入英文單字')
        if z =='apple':
            print(x)
        elif z =='bread':
            print(x2)
        elif z=='celebrate':
            print(x3)
        elif z=='docter':
            print(x4)
        elif z=='elevator':
            print(x5)
        elif z=='feather':
            print(x6)
        elif z=='gorgeous':
            print(x7)
        elif z=='harness':
            print(x8)
        elif z=='igloo':
            print(x9)
        elif z=='judge':
            print(x10)
        else:
            print('沒有此單字')
    elif y=='b':
        print('開始測驗(若在答案中加上其他案件，答案將列為錯誤!')
        
        apple=input('apple(n.):')
        if apple=='蘋果': 
            print('correct!')
        else:
            print('incorrect!')
            print('蘋果')
            
        bread=input('bread(n.):')
        if bread=='麵包': 
            print('correct!')
        else:
            print('incorrect!')
            print('麵包')
        
        celebrate=input('celebrate(v.):')
        if celebrate=='慶祝': 
            print('correct!')
        else:
            print('incorrect!')
            print('慶祝')
        
        docter=input('docter(n.):')
        if docter=='醫生': 
            print('correct!')
        else:
            print('incorrect!')
            print('醫生')
            
        elevator=input('elevator(n.):')
        if elevator=='電梯': 
            print('correct!')
        else:
            print('incorrect!')
            print('電梯')
        
        feather=input('feather(n.):')
        if feather=='羽毛': 
            print('correct!')
        else:
            print('incorrect!')
            print('羽毛')
        
        gorgeous=input('gorgeous(adj.):')
        if gorgeous=='華麗的': 
            print('correct!')
        else:
            print('incorrect!')
            print('華麗的')
        
        harness=input('harness(n.):')
        if harness=='馬具': 
            print('correct!')
        else:
            print('incorrect!')
            print('馬具')
        
        igloo=input('igloo(n.):')
        if igloo=='冰屋': 
            print('correct!')
        else:
            print('incorrect!')
            print('冰屋')
        
        judge=input('judge(n.):')
        if judge=='法官': 
            print('correct!')
        else:
            print('incorrect!')
            print('法官')
        
        w=input('請輸入對了幾題(只寫數字):')
        if w=='10':
            print('10/10，超級棒!')
        elif w=='9':
            print('9/10，非常厲害!')
        elif w=='8':
            print('8/10，很棒!')
        elif w=='7':
            print('7/10，很好!')
        elif w=='6':
            print('6/10，OK!')
        elif w=='5':
            print('5/10，可以更棒!')
        elif w=='4':
            print('4/10，再加油喔!')
        elif w=='3':
            print('3/10，再加油喔!')
        elif w=='2':
            print('2/10，再加油喔!')
        elif w=='1':
            print('1/10，再加油喔!')
        else:
            print('0/10，再加油喔!')
         


    elif y=='c':
        print('即將離開系統')
    else:
        print('發生錯誤')
        


