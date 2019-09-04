#_*_ coding:utf-8 _*_

'''
print_num = input('Which loop do you want it to be printed out?')
count = 0
while count < 100000000:
    if count == print_num:
        choice = input("Do you want to continue the loop?(y/n)")
        if choice == 'n':
            break
        else:
            while print_num <= count:
                print_num = input("Which loop do you want it to be printed out?")
                print("已经过了")
    else:
        print ("Loop:", count)
        count += 1
else:
    print ("loop:", count)
'''  
    
    

count = 0
a = input("一个数:")
while count < 100:
    count += 1
    if count == a:
        print("Loop:", count)
        count += 1
    else:
        count += 1