import os ,os.path ,time

curpath = os.getcwd()

def rename(file,oldName,newName):
    ''' file--文件路径    oldName--包含的关键字    newName--改为 '''
    #start = time.clock()
    os.chdir(file)
    items = os.listdir(file)
    print(os.getcwd())
    for name in items :
        print(name)
        # 遍历所有文件
        if not os.path.isdir(name):
            if oldName in name :
                new_name = name.replace(oldName,newName)
                os.renames(name,new_name)
        else:
            rename(file + '\\' + name, oldName)
            os.chdir('...')      
    print('-----------------------分界线------------------------')
    items = os.listdir(file)
    for name in items:
        print(name)
 
rename(curpath,'264','265')
