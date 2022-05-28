import os ,os.path ,time

curpath = os.getcwd()

def rename(file,keyword):
    ''' file: 文件路径    keyWord: 需要修改的文件中所包含的关键字 '''
    start = time.clock()
    os.chdir(file)
    items = os.listdir(file)
    print(os.getcwd())
    for name in items :
        print(name)
        # 遍历所有文件
        if not os.path.isdir(name):
            if keyword in name :
                new_name = name.replace(keyword,'')
                os.renames(name,new_name)
        else:
            rename(file + '\\' + name, keyword)
            os.chdir('...')      
    print('-----------------------分界线------------------------')
    items = os.listdir(file)
    for name in items:
        print(name)
 
rename(curpath,'4K 杰克逊 30 年御用鼓手 Jonathan Moffett 神级律动演绎完整版 人肉节拍器-')