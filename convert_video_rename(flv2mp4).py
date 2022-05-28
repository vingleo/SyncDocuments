import os
# coding=utf-8
#NEW_RESOLUTION_SD = "640x480"  # 目标分辨率，普清
#NEW_RESOLUTION_HD = "1280x720" # 目标分辨率，高清
#NEW_RESOLUTION_FHD = "1920x1080" # 目标分辨率，全高清
#NEW_RESOLUTION_4K = "4096"
#NEW_FPS = 23.976 # 目标帧率
#VIDEO_CODEC_FORMAT = libx265 #使用x265编码
#AUDIO_CODEC_FORMAT = aac


curpath = os.getcwd()  # 获取当前路径
input_dir = os.path.join(curpath, "Input_Video")
output_dir = os.path.join(curpath, "Output_Video")
input_video_list = os.listdir(input_dir)  # 获取视频列表

# 如果没有Output_Video这个文件夹，则创建这个文件夹
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

# 开始批量二次编码压缩视频转码
for each_video in input_video_list:
    video_name, _ = os.path.splitext(each_video)  # _是没意义，就只是一个无用代号，占个坑而已
# 注意文件名或者路径中空格，需要用转移符将引号包括在内
    ffmpeg_command = ("ffmpeg -i \"%s%s%s\" -c:a copy  -c:v copy \"%s%s%s\".mp4" % (
        input_dir, os.sep, each_video, output_dir, os.sep, video_name))
    print(ffmpeg_command)
    os.system(ffmpeg_command)


print('-----------------------分界线------------------------')

def rename(file,keyword):
    ''' file: 文件路径    keyWord: 需要修改的文件中所包含的关键字 '''
    #start = time.clock()
    os.chdir(file)
    items = os.listdir(file)
    print(os.getcwd())
    for name in items :
        print(name)
        # 遍历所有文件
        if not os.path.isdir(name):
            if keyword in name :
                new_name = name.replace(keyword,' ')
                os.renames(name,new_name)
        else:
            rename(file + '\\' + name, keyword)
            os.chdir('...')      
    print('-----------------------分界线------------------------')
    items = os.listdir(file)
    for name in items:
        print(name)
 
rename(output_dir,'_')

os.system("pause")

