import os ,os.path ,time

curpath = os.getcwd()

def rename(file,oldName,newName):
    ''' file--�ļ�·��    oldName--�����Ĺؼ���    newName--��Ϊ '''
    #start = time.clock()
    os.chdir(file)
    items = os.listdir(file)
    print(os.getcwd())
    for name in items :
        print(name)
        # ���������ļ�
        if not os.path.isdir(name):
            if oldName in name :
                new_name = name.replace(oldName,newName)
                os.renames(name,new_name)
        else:
            rename(file + '\\' + name, oldName)
            os.chdir('...')      
    print('-----------------------�ֽ���------------------------')
    items = os.listdir(file)
    for name in items:
        print(name)
 
rename(curpath,'264','265')
