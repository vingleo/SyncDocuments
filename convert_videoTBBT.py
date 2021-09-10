

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
    ffmpeg_command = ("ffmpeg -i %s%s%s -c:a aac -ac 2 -c:v libx265 -y %s%s%s.mp4" % (
        input_dir, os.sep, each_video, output_dir, os.sep, video_name))
    print(ffmpeg_command)
    os.system(ffmpeg_command)

os.system("pause")