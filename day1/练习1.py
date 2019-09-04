#输入姓名，年龄，工资，猜年龄，如果大于实际年龄，则lesson smill，如果小于实际年龄
#则lessonbigge

#!/usr/bin/env python
#_*_ coding:utf_8 _*_

info = 'This var will be printed out ...'
name = input('Please input your name:')
#age = int (input('age:'))
job = input('Job:')
salary = input('Salary:')

real_age = 29

for i in range(10):
    age = int(input('age:'))
    if age > 29:
        print ("think smaller!")
    elif age == 29:
        print ("GOOD! 10 RMB!")
        
        break
    else:
        print ('think bigger!')
    print ('You still got %s shots!' % (9 - i))

print ('''
Personal information of %s:
        Name: %s
        Age : %d 
        Job : %s 
      Salary: %s 
----------------------------
''' % (name, name, age, job, salary))