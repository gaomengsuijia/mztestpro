<<<<<<< HEAD
import os


#得到最新的报告文件
def lis(file_path):
    files = os.listdir(file_path)
    f_time = []
    for f in files:
        kuo = os.path.splitext(f)[1]
        if kuo == ".html":
            fil = file_path + f
            f_times = os.path.getctime(fil)
            f_time.append((f_times,f))
            f_time = sorted(f_time,key=lambda f_time : f_time[0])
    return f_time[-1][1]
=======
#coding:utf-8
import  os
def open_report(file_path):
    files = os.listdir(file_path)
    #t = os.path.getctime(file_path)
    files.sort(key=lambda fn: os.path.getmtime(file_path,"\\", + fn))
    file_new = os.path.join(file_path,files[-1])
    print(file_new)
def lis(t):
    print(t[1])
    return t[1]
>>>>>>> 5245c69034ec5aa43914843cccde423ad17c5c78




if __name__ == "__main__":
<<<<<<< HEAD
    file_path = './report/'
    new_file = lis(file_path)
    print(new_file)
=======
    file_path = os.path.dirname(__file__)
    file_path = file_path + '/report/'
    #open_report(file_path)
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    mn = sorted(L,key=lis,reverse=True)
    print(mn)
>>>>>>> 5245c69034ec5aa43914843cccde423ad17c5c78
