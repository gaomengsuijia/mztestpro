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




if __name__ == "__main__":
    file_path = os.path.dirname(__file__)
    file_path = file_path + '/report/'
    #open_report(file_path)
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    mn = sorted(L,key=lis,reverse=True)
    print(mn)
