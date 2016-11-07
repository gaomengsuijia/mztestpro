#coding:utf-8
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


if __name__ == "__main__":
    file_path = './report/'
    new_file = lis(file_path)
    print(new_file)

