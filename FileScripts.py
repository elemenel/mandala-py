"""FileScripts.py contains file manipulation scripts
critical to successful functioning of the  master_mandala_maker.py module.
It creates and manipulates all folders and files, and is a fully functioning video creator.
Copyright(c) by Leon R. Hatton, 2017 -2024
"""
import os
import sys
import platform
import time
import random
from PIL import Image #module for converting python output to image
import PIL.ImageGrab
import numpy as np
import cv2
import pyautogui
import datetime as datetime
import sys
import shutil
from shutil import copytree
import pathlib
from pathlib import Path
import moviepy.editor as mp
from natsort import humansorted as hs
import glob
# from glob import glob, iglob
import imageio
from moviepy.editor import AudioFileClip, ImageClip, VideoFileClip, CompositeAudioClip
from pydub import *
from turtle import Screen as sc
from functools import lru_cache
from pathlib import Path
from moviepy.video.io.VideoFileClip import VideoFileClip
from dirsync import sync
import dirsync
from timeit import default_timer as timer
# Custom modules listed below
import my_angles as a
import Timer as Tm
import My_template as t
import audio_clips as au
from My_template import my_key
import My_logger as Lg

#Global declarations
global no_audio_vids, my_video_path_av, my_thumbs_path, clip_path, full_vid_path, Lg

#Assign correct system path for cross-platform capability; need to edit paths accordingly
if sys.platform.startswith('linux'):
    my_home_dir = '/home/sels/'
    my_work_dir = '/home/sels/Modules/MandalaMaker/'
    my_log_dir = '/home/sels/Modules/MandalaMaker/Logs/'
    my_video_path = '/home/sels/Videos/'
    no_audio_vids = '/home/sels/Videos/no_audio/'
    my_full_vids = '/home/sels/Videos/Full_Vids/'
    my_audio_path = '/home/sels/Music/Audio Clips for Python/'
    my_git_path = '/home/sels/Git/elemenel/'
    my_mandala_pics_path = '/mnt/fe9f7833-9c10-449c-bf09-a8dfa3d54adc/Videos/Pictures/Mandala Final Thumbs/'
    my_thumbs = '/home/sels/Thumbs/'
    final_thumbs = '/home/sels/Pictures/Final_Thumbs/'
    my_shared_drive = '/home/sels/sambashare/'
    my_backup_drive = '/mnt/fe9f7833-9c10-449c-bf09-a8dfa3d54adc/'
    my_audio_backup_folder = '/mnt/fe9f7833-9c10-449c-bf09-a8dfa3d54adc/AudioClipsPython/'
    concatenate_candidates = '/home/sels/Videos/concatenate_candidates/'
    do_concatenate_folder = '/home/sels/Videos/do_concatenate/'
    
else:
    my_work_dir = 'D:/'
    no_audio_vids = 'D:/'
    my_full_vids = 'D:/Videos/Full_Vids/'
    my_audio_path = 'D:/Music/Audio Clips for Python/'
    my_git_path = 'D:/Git/'
    my_home_dir = 'C:/'
    my_log_dir = 'D:/Logs/'
    my_video_path = '/D:/Videos/'
    no_audio_vids = 'D:/Videos/no_audio/'
    my_mandala_pics_path = 'D:/Pictures/Mandala Final Thumbs/'
    my_thumbs = 'D:/Pictures/Thumbs/'
    my_shared_drive = 'Y:/sambashare/'

'*********************************************************************************************************'
'''--------------------------------------------------------Mandala Maker Section-----------------------------------------------------
---------------------------Every script that Mandala Maker calls reside here, in Section One-------------------------------
'''
'''-----------------------------------Make Folders section--------------------------------------------------------------
'''
global png_folder
png_folder = ' '

def make_reverse_png_folder():
    reverse_png_folder = f'{my_thumbs}{t.folder_name}/'
    os.makedirs(reverse_png_folder, exist_ok=True)
    os.chdir(reverse_png_folder)
    my_project = reverse_png_folder
    Lg.logger.info(f'FileScripts:New folder:  {reverse_png_folder} has been created @ {Tm.my_time}')
    Lg.logger.info(f'FileScripts:{reverse_png_folder} has been emptied. The folder is now ready for new content @ {Tm.my_time}.')
# Empties the folder where the .png files are stored for video processing.


def make_png_folder():
    png_folder = f'{my_thumbs}{t.folder_name}/'
    os.makedirs(png_folder, exist_ok=True)
    os.chdir(png_folder)
    my_project = png_folder
    Lg.logger.info(f'FileScripts:New folder: {png_folder} has been created @ {Tm.my_time} ')
    Lg.logger.info(f'FileScripts:{png_folder} has been emptied. The folder is now ready for new content @ {Tm.my_time}.')
# make_png_folder()

folder_name = 'novanno_archive'
'''Create a folder to store new mandala along with a copy of the current python module version'''
def make_archive_folder():
    archive_folder = '/mnt/fe9f7833-9c10-449c-bf09-a8dfa3d54adc/MandalaScriptsBackup/'
    os.makedirs(archive_folder + t.folder_name, exist_ok=True)
    my_archive_folder = archive_folder + t.folder_name
    endswith_ = '.py'
    origin = my_work_dir
    destination = my_archive_folder
    [shutil.copy(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
    return archive_folder
    
# make_archive_folder()




'''-----------------------------------Screenshot Functions Section--------------------------------------------------------------
'''
#  This creates a png of each loop. Master MandalaMaker needs this.
def save_thumb():
    image = PIL.ImageGrab.grab()
#     image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    Tm.set_time()
    cv2.imwrite(f'{my_thumbs}{t.folder_name}/{Tm.iterable_time}.png',image)
#     cv2.imwrite(f'{my_thumbs}{t.folder_name}.png',image)

# This creates  png and jpg files of the final image, to be saved out to the Pictures/Mandalas folder. Master MandalaMaker uses this.
def save_final_thumb():
    global my_last_png, my_last_jpg
    image = PIL.ImageGrab.grab()
#     image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    Tm.set_time()
    cv2.imwrite(f'{my_mandala_pics_path}{t.folder_name}-{Tm.iterable_time}.png', image)
    cv2.imwrite(f'{final_thumbs}{t.folder_name}_final.jpeg', image)
#     cv2.imwrite(f'{my_mandala_pics_path}/{t.folder_name}_{Tm.iterable_time}.jpg', image)


# Function to get the current working directory   
def current_path():
    import os
    Lg.logger.info(f'FileScripts:Current working directory is:')
    Lg.logger.info(os.getcwd())

'''-----------------------------------Video Processing Functions Section--------------------------------------------------------------
'''

# Used by Master Mandala maker Module to create videos from looped .png files
def set_reverse_vid_env():
    Lg.logger.info(f'FileScripts:Starting set_vid_env() @ {Tm.my_time}')
    current_path()
    os.chdir(f'{my_thumbs}{t.folder_name}')
    Lg.logger.info(f'FileScripts:The current folder is: {my_thumbs}{t.folder_name}')
    make_reversed_video()
    os.chdir(my_work_dir)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
# Used by Master Mandala maker Module to create videos from looped .png files
def set_vid_env():
    Lg.logger.info(f'FileScripts:Starting set_vid_env() @ {Tm.my_time}')
    current_path()
    os.chdir   (f'{my_thumbs}{t.folder_name}')  #(my_thumbs + t.folder_name)
    Lg.logger.info(f'FileScripts:The current folder is: {my_thumbs}{t.folder_name}')  #+ my_thumbs + t.folder_name)
    make_video()
    os.chdir(my_work_dir)





# Master MandalaMaker depends on the 'make_video' function to create videos from the hundreds of .png files.
# This works using moviepy on a single folder. Does not loop. Optional codecs are 'mpeg4', libx264(.mp4), 'rawvideo'(.avi),\
 # libvpx(webm)-HTML5 and browser videos.
# Partially copied from Geeks for Geeks ('https://www.geeksforgeeks.org/moviepy-fps-of-video-file-clip/?ref=rp')
def make_video():
    make_video_start_time = timer()
    Lg.logger.info(f'FileScripts:Starting make_video() @ {Tm.this_time}')
    import os
    from pathlib import Path
    import moviepy.video.io.ImageSequenceClip
    import moviepy.editor as mp 
    fps = 60 # to speed up use higher numbers
    Lg.logger.info(f'FileScripts:Setting Frame Rate at {fps} frames per second')
    # Start sort of png files  
    Lg.logger.info(f'FileScripts:The directory to be sorted is {my_thumbs}{t.folder_name}')
    # Make images directory current
    os.chdir(f'{my_thumbs}{t.folder_name}/')
    png_count = len(glob.glob(f'{my_thumbs}{t.folder_name}/*.png'))
    Lg.logger.info(f'FileScripts:Total png files to be processed: {png_count}')
    print(f'FileScripts:Total png files to be processed: {png_count}')               
    Lg.logger.info(f'FileScripts:Starting sort of screenshot files @ {Tm.this_time}...')
    begin_sort_start_time = timer()
    sorted_files = sorted(os.listdir('.'), key = os.path.getctime) #Collect and sort .png files
    Lg.logger.info(f'FileScripts:Sorting process has completed @ {Tm.this_time}')
    Lg.logger.info(f'FileScripts:Starting video generation from sorted screenshot files @ {Tm.this_time}')
    stop_sort_end_time = timer()
    elapsed_sort_time = (stop_sort_end_time - begin_sort_start_time)
    print(f'FileScripts:Elapsed time: {elapsed_sort_time:.2f} seconds')
    total_png_count = len(sorted_files)
    Lg.logger.info(f'FileScripts:Total Files to be processed into a clip: {total_png_count}')
    clip_estimated_run_time = (total_png_count /100) * 2.90 # From most recent benchmark; actual time can vary
    Lg.logger.info(f'FileScripts:Estimated time to process the pngs into a video is {clip_estimated_run_time:.2f} seconds, or {clip_estimated_run_time/60:.2f} minutes')
    print(f'FileScripts: Total Files to be processed into a clip: {total_png_count}')
    estimated_video_clip_duration = total_png_count / fps
    Lg.logger.info(f'FileScripts: Estimated Video Duration: {estimated_video_clip_duration:.2f} seconds, or {estimated_video_clip_duration/60:.2f} minutes')
    my_clip =  moviepy.video.io.ImageSequenceClip.ImageSequenceClip(sorted_files, fps=fps)
    Lg.logger.info (f'FilesScripts:Total time to sort the image files is {elapsed_sort_time/60.:2f} minutes ')
    # Write sequenced png files to a single .mp4 file normally less than 10 mb, quality as good as much larger .avi file
    Lg.logger.info(f'FileScripts:Starting to write video file @ {Tm.my_time}')
    begin_clip_creation_start_time = timer()
    # This determines frame speed and movie length   Industry standard is 24; for shorter length and faster speed use 60-120
    my_clip.write_videofile(f'{no_audio_vids}{t.folder_name}.mp4', fps = fps,  
                            codec = 'libx264', bitrate = None, audio = False, audio_fps = 44100, preset='ultrafast', audio_nbytes=4,
                            audio_codec= 'mp3', audio_bitrate= None, audio_bufsize=8000, temp_audiofile = my_work_dir + '/temp',
                            remove_temp= True, write_logfile= True, threads=4,
                            ffmpeg_params= None, logger='bar') #'bar'
    my_vidClip = f'{no_audio_vids}{t.folder_name}.mp4'
    end_clip_creation_start_time = timer()
    clip_creation_time = end_clip_creation_start_time - begin_clip_creation_start_time
    print(f'FileScripts:Total time to create video from sorted files is {clip_creation_time:.2f} seconds')
    Lg.logger.info(f'FileScripts:Total time to create video from sorted files is {clip_creation_time:.2f} seconds, or {clip_creation_time /60:.2f} minutes ')
    clip = VideoFileClip(my_vidClip).subclip(0, 10)    
    # getting frame rate of the clip
    rate = clip.fps
    # printing the fps
    Lg.logger.info(f'FileScripts:FPS: {rate}')
    Lg.logger.info(f'FileScripts:mp4 no_audio duration: {my_clip.duration / 60.:2f} minutes')
    # Calculate elapsed time
    make_video_end_time = timer()
    make_video_elapsed_time = (make_video_end_time - make_video_start_time)
    Lg.logger.info (f'FileScripts:Total time to run the make_video is {make_video_elapsed_time/3600.:2f} hours')
    Lg.logger.info(f'FileScripts:Screenshot images conversion to audio-less mp4 video file completed @ {Tm.this_time}')
'=================================================================================================='
# Partially copied from Geeks for Geeks ('https://www.geeksforgeeks.org/moviepy-fps-of-video-file-clip/?ref=rp')
def make_reversed_video():
    make_reversed_video_start_time = timer()
    Lg.logger.info(f'FileScripts:Starting make_reversed_video() @ {Tm.this_time}')
    import os
    from pathlib import Path
    import moviepy.video.io.ImageSequenceClip
    import moviepy.editor as mp 
    fps = 240 # to speed up use higher numbers
    Lg.logger.info(f'FileScripts:Setting Frame Rate at {fps} frames per second')
    # Start sort of png files  
    Lg.logger.info(f'FileScripts:The directory to be sorted is {my_thumbs}{t.folder_name}')
    # Make images directory current
    os.chdir(f'{my_thumbs}{t.folder_name}/')
    png_count = len(glob.glob(f'{my_thumbs}{t.folder_name}/*.png'))
    Lg.logger.info(f'FileScripts:Total png files to be processed: {png_count}')
    print(f'FileScripts:Total png files to be processed: {png_count}')               
    Lg.logger.info(f'FileScripts:Starting sort of screenshot files @ {Tm.this_time}...')
    begin_sort_start_time = timer()
    sorted_files = sorted(os.listdir('.'), key = os.path.getctime) #Collect and sort .png files
    reverse_sorted_files = sorted(os.listdir('.'), key = os.path.getctime, reverse = True)
    Lg.logger.info(f'FileScripts:Sorting process has completed @ {Tm.this_time}')
    Lg.logger.info(f'FileScripts:Starting video generation from sorted screenshot files @ {Tm.this_time}')
    stop_sort_end_time = timer()
    elapsed_sort_time = (stop_sort_end_time - begin_sort_start_time)
    print(f'FileScripts:Elapsed time: {elapsed_sort_time:.2f} seconds')
    total_png_count = len(sorted_files + reverse_sorted_files)
    Lg.logger.info(f'FileScripts:Total Files to be processed into a clip: {total_png_count}')
    clip_estimated_run_time = (total_png_count /100) * 2.90
    Lg.logger.info(f'FileScripts:Estimated time to process the pngs into a video is {clip_estimated_run_time:.2f} seconds, or {clip_estimated_run_time/60:.2f} minutes')
    print(f'FileScripts: Total Files to be processed into a clip: {total_png_count}')
    estimated_video_clip_duration = total_png_count / fps
    Lg.logger.info(f'FileScripts: Estimated Video Duration: {estimated_video_clip_duration:.2f} seconds, or {estimated_video_clip_duration/60:.2f} minutes')
    my_clip =  moviepy.video.io.ImageSequenceClip.ImageSequenceClip(sorted_files + reverse_sorted_files, fps=fps)
    Lg.logger.info (f'FilesScripts:Total time to sort the image files is {elapsed_sort_time/60.:2f} minutes ')
    # Write sequenced png files to a single .mp4 file normally less than 10 mb, quality as good as much larger .avi file
    Lg.logger.info(f'FileScripts:Starting to write video file @ {Tm.my_time}')
    begin_clip_creation_start_time = timer()
    # This determines frame speed and movie length   Industry standard is 24; for shorter length and faster speed use 60-120
#     ffmpeg -f image2 -r 25 -pattern_type glob -i 'img/*.png' -vcodec libx264 -crf 22 f'{no_audio_vids}{t.folder_name}.mp4'
    my_clip.write_videofile(f'{no_audio_vids}{t.folder_name}.mp4', fps = fps,  
                            codec = 'libx264', bitrate = None, audio = False, audio_fps =None, preset='fast', audio_nbytes=None,
                            audio_codec= None, audio_bitrate= None, audio_bufsize=None, temp_audiofile = my_work_dir + '/temp',
                            remove_temp= True, write_logfile= True, threads=8,
                            ffmpeg_params= None, logger='bar') #'bar'
    my_vidClip = f'{no_audio_vids}{t.folder_name}.mp4'
    end_clip_creation_start_time = timer()
    clip_creation_time = end_clip_creation_start_time - begin_clip_creation_start_time
    print(f'FileScripts:Total time to create video from sorted files is {clip_creation_time:.2f} seconds')
    Lg.logger.info(f'FileScripts:Total time to create video from sorted files is {clip_creation_time:.2f} seconds, or {clip_creation_time /60:.2f} minutes ')
    clip = VideoFileClip(my_vidClip).subclip(0, 10)    
    # getting frame rate of the clip
    rate = clip.fps
    # printing the fps
    Lg.logger.info(f'FileScripts:FPS: {rate}')
    Lg.logger.info(f'FileScripts:mp4 no_audio duration: {my_clip.duration / 60.:2f} minutes')
    # Calculate elapsed time
    make_reversed_video_end_time = timer()
    make_reversed_video_elapsed_time = (make_reversed_video_end_time - make_reversed_video_start_time)
    Lg.logger.info (f'FileScripts:Total time to run the make_reversed_video is {make_reversed_video_elapsed_time/3600.:2f} hours')
    Lg.logger.info(f'FileScripts:Screenshot images conversion to audio-less mp4 video file completed @ {Tm.this_time}')
    

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
#  https://www.geeksforgeeks.org/moviepy-assigning-audio-clip-to-video-file/
# Used by Master Mandala maker to generate videos with sound by merging audio clips to video clips
def sync_av():
    av_start_time = timer()
    Lg.logger.info(f'FileScripts:Starting sync_av() @ {Tm.this_time}')
    Lg.logger.info(f'FileScripts:Merging Video with Audio...')
    os.chdir(my_video_path)
    new_video = '__temp__.mp4'
    Lg.logger.info(f'FileScripts:Folder name is {t.folder_name}')
    my_file = t.folder_name
    Lg.logger.info(f'FileScripts:File Name is {my_file}')
    videoclip = VideoFileClip(f'{my_video_path}/no_audio/{my_file}.mp4')
    audioclip = AudioFileClip(au.my_audio_clip)
    audioclip = audioclip.set_duration(videoclip.duration + 1) # Adjust the audio duration here '+6' is default
    Lg.logger.info(f'FileScripts:The duration of this audio clip is {audioclip.duration / 60:.2f} minutes')
    new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip
    videoclip.write_videofile(f'{my_full_vids}{t.folder_name}.mp4')
#     Tm.set_time()
#     shutil.copyfile(f'{my_full_vids}{t.folder_name}.mp4', f'{concatenate_candidates}{t.folder_name}-{Tm.project_time}.mp4')
#     Lg.logger.info(f'FileScripts:The video {t.folder_name}-{Tm.project_time}.mp4 has been copied to the concatenate_candidates folder')
#     copy_video_file(src, dst)
#     videoclip.write_videofile(f'{concatenate_candidates}{t.folder_name}.mp4')
    Lg.logger.info(f'FileScripts:The duration of the new composite video is {videoclip.duration / 60:.2f} minutes')
    Lg.logger.info(f'FileScripts:The new composite video has been renamed to {t.folder_name}.mp4')
    os.chdir(my_work_dir)
    av_end_time = timer()
    av_elapsed_time = av_end_time - av_start_time
    Lg.logger.info(f'FileScripts:Execution time to run the sync_av module was {av_elapsed_time/60.:2f} minutes')
    Lg.logger.info('====================================================================')


def get_duration():
    from moviepy.editor import VideoFileClip
    clip = VideoFileClip(my_clip)
    Lg.logger.info(f'FileScripts:Duration: {my_clip.duration}')
    

'''-----------------------------------Archiving and Closeout Section--------------------------------------------------------------
'''

# Moves images to their respective locations from the code file and leaving .py files only
# Master MandalaMaker depends on this. Using list comprehension syntax.
def move_pngs():
    origin = my_work_dir
    destination = f'{my_thumbs}{t.folder_name}'
    endswith_ = '.png'
    [shutil.move(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
    Lg.logger.info(f'FileScripts:Image .png files have been moved to {my_thumbs} @ {Tm.my_time}')

def move_jpegs():
    # Get the path to the current directory
    current_directory = my_work_dir  #.getcwd()

    # Get the path to the directory where the files will be moved
    destination_directory = os.path.join(final_thumbs)

    # Get a list of all the files in the current directory
    files = os.listdir(current_directory)

    # Create a list of all the files ending with `jpeg`
    jpeg_files = [file for file in files if file.endswith('.jpeg')]

    # Move the jpeg files to the destination directory
    for file in jpeg_files:
        shutil.move(file, destination_directory)

    # Print a message to confirm that the files were moved
    Lg.logger.info(f'FileScripts:The jpeg files were successfully moved to {final_thumbs} @ {Tm.my_time} .')

# move_jpegs()

def copy_video_file(src, dst):
    shutil.copyfile(f'{my_full_vids}{t.folder_name}.mp4,{concatenate_candidates}{t.folder_name}.mp4')


# Due to their immense sizes, snapshots of running videos are created and stored at a dedicated location.
# Video files are compilations of Thumbs that are sorted and processed. They are converted and stored at '/media/sels/My_Media/Videos/no_audio'.
# Moves images to their respective locations from the code file and leaving .py files only, then to larger size drive(Container)
# Runs best with Master MandalaMaker. Using list comprehension syntax.

def move_all():
    origin = my_thumbs
    destination = my_video_path
    endswith_ = '.avi'
    [shutil.move(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
    Lg.logger.info(f'FileScripts:Video .avi files have been moved to /Videos/@ {Tm.my_time} ')
    
    origin = my_thumbs
    destination = no_audio_vids
    endswith_ = '.mp4'
    [shutil.move(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
    Lg.logger.info(f'FileScripts:Video .mp4 files have been moved to /Videos/@ {Tm.my_time} ')
    
    origin = my_thumbs
    destination = my_video_path
    endswith_ = '.webm'
    [shutil.move(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
    Lg.logger.info(f'FileScripts:Video .webm files have been moved to /Videos/@ {Tm.my_time} ')
    
    origin = my_work_dir
    destination = my_thumbs # + t.folder_name
    endswith_ = '.png'
    [shutil.move(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
    Lg.logger.info(f'FileScripts:Image .png files have been moved to /Thumbs/@ {Tm.my_time} ')
    
    origin = my_work_dir
    destination = final_thumbs
    endswith_ = '.jpeg'
    [shutil.move(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
    Lg.logger.info(f'FileScripts:Image .png files have been moved to /Thumbs/@ {Tm.my_time} ')
    
    origin = my_thumbs # + t.folder_name
    destination = final_thumbs
    endswith_ = '.jpeg'
    [shutil.move(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
    Lg.logger.info(f'FileScripts:Image .jpeg files have been moved to /home/sels/Pictures/Mandala Final Thumbs/@ {Tm.my_time} ')
    Lg.logger.info('================================================================================')
# move_all()


def clear_thumbs():
    Lg.logger.info(f'FileScripts:Preparing to empty the Thumbs folder @ {Tm.my_time} .......')
    shutil.rmtree(my_thumbs)
    os.makedirs(my_thumbs)
    Lg.logger.info(f'FileScripts:Thumbs folder has been emptied @ {Tm.my_time} ')
# clear_thumbs()



#  Sync two folders from https://stackoverflow.com/questions/54688687/how-to-synchronize-two-folders-using-python-script
#dirsync.sync(target_path, source_path, 'sync', create=True) #for syncing the opposite way
#dirsync.sync(target_path_a, source_path_a, 'sync', create=True) #for syncing the opposite way
def sync_full_vids():
     #Sync Videos
    Lg.logger.info(f'FileScripts:Working on sync of MandalaMaker Full Vids folders @ {Tm.my_time}')
    source_path_videos = '/home/sels/Videos/Full_Vids/'
    target_path = '/home/sels/MandalaBackup/Full_Vids/'
    target_path_shared_videos = f'{my_shared_drive}/MandalaMaker Full Vids/'
    target_path_usb_ssd_no_audio = '/media/sels/2TB-Linux/Backup/no_audio/'
    target_path_usb_ssd_full_vids = '/media/sels/2TB-Linux/Backup/Full_Vids/'
    target_path_media = '/mnt/fe9f7833-9c10-449c-bf09-a8dfa3d54adc/Mandala Videos_Backup/'
    dirsync.sync(source_path_videos, target_path, "sync")
    Lg.logger.info(f'FileScripts: Finished Sync of MandalaMaker Full Vids folders to {target_path} completed @ {Tm.this_time}')
    dirsync.sync(source_path_videos, target_path_shared_videos, 'sync', create=True)
    Lg.logger.info(f'FileScripts: Finished Sync of MandalaMaker Full Vids folders to {target_path_shared_videos} completed @ {Tm.this_time}')
    dirsync.sync(source_path_videos, target_path_media, 'sync', create=True)
    Lg.logger.info(f'FileScripts: Finished Sync of MandalaMaker Full Vids folders to {target_path_media} completed @ {Tm.this_time}')
    dirsync.sync(source_path_videos, target_path_usb_ssd_no_audio, 'sync', create=True)
    Lg.logger.info(f'FileScripts: Finished Sync of MandalaMaker Full Vids folders to {target_path_usb_ssd_no_audio} completed @ {Tm.this_time}')
    dirsync.sync(source_path_videos, target_path_usb_ssd_full_vids, 'sync', create=True)
    Lg.logger.info(f'FileScripts: Finished Sync of MandalaMaker Full Vids folders to {target_path_usb_ssd_full_vids} @ {Tm.this_time}')
    Lg.logger.info(f'FileScripts:Sync of Mandala Video folders completed successfully @ {Tm.this_time}')
# sync_full_vids()    
    
def sync_module_folders():
     #Sync Modules
    Lg.logger.info(f'FileScripts: Begin processing sync of MandalaMaker Module folders....')
    source_path_a = my_home_dir + 'Modules/'
    target_path_a = '/home/sels/MandalaBackup/Modules/'
    target_path_b = '/home/sels/Git/elemenel/mandala-py/Modules/MandalaMaker/'
    target_path_u = '/mnt/fe9f7833-9c10-449c-bf09-a8dfa3d54adc/Modules - MandalaMaker/'    
    target_path_shared_modules = my_shared_drive + 'MandalaMaker Modules/'   
    dirsync.sync(source_path_a, target_path_a, 'sync', create=True)
    Lg.logger.info(f'FileScripts: Finished Sync of Modules folders to {target_path_a} @ {Tm.my_time}')
    dirsync.sync(source_path_a, target_path_shared_modules, 'sync', create=True)
    Lg.logger.info(f'FileScripts: Finished Sync of Modules folders to {target_path_shared_modules} @ {Tm.my_time}')
    dirsync.sync(source_path_a, target_path_b, 'sync', create=True)
    Lg.logger.info(f'FileScripts: Finished Sync of Modules folders to {target_path_b} @ {Tm.my_time}')
    dirsync.sync(source_path_a, target_path_u, 'sync', create=True)
    Lg.logger.info(f'FileScripts: Finished Sync of Modules folders to {target_path_u} @ {Tm.my_time}')
    Lg.logger.info(f'FileScripts:Sync of MandalaMaker Module folders completed successfully @ {Tm.this_time}')
# sync_module_folders()

def sync_audio_clips():
    #Sync Audio Clips
    Lg.logger.info(f'FileScripts:Begin processing sync of MandalaMaker Audio folders....')
    source_path_audio = my_audio_path
    target_path_shared_audio = my_shared_drive + 'MandalaMaker Audio Clips/'
    target_path_back_up_audio = my_audio_backup_folder
    target_path_u = '/mnt/fe9f7833-9c10-449c-bf09-a8dfa3d54adc/' 
    dirsync.sync(source_path_audio, target_path_shared_audio, 'sync', create=True)
    Lg.logger.info(f'FileScripts: Finished  Sync of Audio Clips folders to {target_path_shared_audio} @ {Tm.my_time}')
    dirsync.sync(source_path_audio, target_path_back_up_audio, 'sync', create=True)
    Lg.logger.info(f'FileScripts: Finished Sync of Audio Clips folders to {target_path_back_up_audio} @ {Tm.my_time}')
    dirsync.sync(source_path_audio, target_path_u, 'sync', create=True)
    Lg.logger.info(f'FileScripts: Finished Sync of Audio Clips folders to {target_path_u} @ {Tm.my_time}')
    Lg.logger.info(f'FileScripts:Sync of MandalaMaker Audio folders completed successfully @ {Tm.this_time}')
# sync_audio_clips()

def sync_images():
     #Sync Images
    Lg.logger.info(f'FileScripts:Working on sync of MandalaMaker Image folders....')
    source_path_images = final_thumbs
    target_path_shared_images = my_shared_drive + 'MandalaMaker Final Images/'
    dirsync.sync(source_path_images, target_path_shared_images, 'sync', create=True)
    Lg.logger.info(f'FileScripts: Finished Sync of Image folders to {target_path_shared_images} @ {Tm.my_time}')
    Lg.logger.info(f'FileScripts:Sync of MandalaMaker Image  folders completed successfully @ {Tm.this_time}')
# sync_images()    


def sync_mandala_folders():
    #Sync All Folders
    sync_full_vids()
    sync_module_folders()
    sync_audio_clips()
    sync_images()
    
# sync_mandala_folders()
'''---------------------------------------------------The Above Sections are used by the Master MandalaMaker---------------------------------------
----------------------------------------------------- Scripts below have no current dependencies for MasterMandalaMaker----------------------------------------------
'''

# Start time
start_time = timer()
# End time
end_time = timer()
# Calculate elapsed time
elapsed_time = end_time - start_time

def format_my_time():
    global formatted_time, elapsed_time, end_time, start_time
    # Format the output
    hours, remainder = divmod(elapsed_time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = elapsed_time.microseconds // 1000
    formatted_time = "{:02}:{:02}:{:02}.{:03}".format(hours, minutes, seconds, milliseconds)



# Copies completed videos to /home/sels/Videos/Full_Vids for Plex access on Linux
def copy_videos():
#      if my_os == 'Linux':
     try:
         origin = '/home/sels/Videos/Full_Vids/'
         destination = '/media/sels/2TB-Linux/Backup/Full_Vids/'
         endswith_ = '.mp4'
         [shutil.copy2(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
         Lg.logger.info(f'FileScripts:Copying videos @ {Tm.my_time}.....')
     except shutil.SameFileError as e:
         pass 
     else:
         pass
     Lg.logger.info(f'FileScripts:Full_Vids directory has been copied @ {Tm.my_time}')   
# copy_videos()
'**********************************************************************************************************'
# Backs up the code to current. Does not archive yet.
# @lru_cache(maxsize = 128)
def code_backup():
    Lg.logger.info(f'FileScripts:Starting code backup @ {Tm.my_time}...........')
#     shutil.rmtree(my_work_dir +'/Code_Backup/')
    shutil.rmtree('/mnt/fe9f7833-9c10-449c-bf09-a8dfa3d54adc/Modules - MandalaMaker/') #file:///media/sels/USB DISK/Modules - MandalaMaker
#     src =  my_work_dir +'/Python Code/'
    m_src = my_work_dir +'/Make_Mandalas/'
#     dest = my_work_dir +'/Code_Backup/'
    m_dest = 'media/sels/Backup/Modules - MandalaMaker/'
#     destination = shutil.copytree(src, dest)
    destination = shutil.copytree(m_src, m_dest)
    Lg.logger.info(f'FileScripts:Python Code files have been backed up to MandalaMakerBackup pendrive @ {Tm.my_time}')
#Default is to leave commented. Uncomment to run from here.    
# code_backup()                                                           

def make_daily_activities_log():
    Lg.logger.info(f'FileScripts:FileScripts:Creating activity log file @ {Tm.my_time}')
    def create_log_folder():
        """Creates a log folder if it doesn't exist."""
        log_folder_path = os.path.join(os.getcwd(), 'Daily_Logs')
        if not os.path.exists(log_folder_path):
            os.mkdir(log_folder_path)
    def create_log_file(module_name):
        """Creates a log file in the log folder and sets the module name."""
        log_file_path = os.path.join(os.getcwd(), f'/home/sels/Modules/MandalaMaker/Daily_Logs, {t.folder_name}.log')
#         Lg.logging.basicConfig(filename=log_file_path, filemode='w')
#         Lg.logger = logging.getLogger()
#         Lg.logger.setLevel(logging.INFO)
  
    def main():
      create_log_folder()
      create_log_file('t.folder_name')
      Lg.logger = Lg.logging.getLogger('t.folder_name')
      Lg.logger.info(f'FileScripts:This is a log message from my_module.')
  
    if __name__ == '__main__':
        main()
  
 
#     log_folder = f'{my_log_dir}{Tm.my_date}'
#     os.makedirs(log_folder, exist_ok=True)
#     os.chdir(log_folder)
#     Lg.logger.info(f'FileScripts:FileScripts:Logging Module {t.folder_name}')
# make_daily_activities_log()    

      
def display_image():
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.IMREAD_ANYCOLOR(image)
    cv2.imshow(image)

# def report_run():
#     image = pyautogui.screenshot()
# #     image.save(t.my_project + '_' + str(Tm.iterable_time) +'.png')
#     image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
#     cv2.imwrite(/home/documents/run_reports/ +'.png', image)
    
    

def move_thumbs():
    # Get the path to the current directory
    source_directory = my_thumbs_path  # os.getcwd()

    # Get the path to the directory where the files will be moved
    destination_directory = os.path.join('/media/sels/USB_2TB/Thumbs', 'Thumbs')

    # Get a list of all the files in the current directory
    files = os.listdir(source_directory)

    # Create a list of all the files ending with `png`
    Thumbs = [file for file in files if file.endswith('.png')]

    # Move the Thumbs to the destination directory
    for file in Thumbs:
        shutil.move(file, destination_directory)

    # Print a message to confirm that the files were moved
    Lg.logger.info(f'FileScripts:The Thumb files were successfully moved to the destination directory @ {Tm.my_time}.')
# move_thumbs()



"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
# def get_most_recent_thumb(directory):
#     '''Returns the most recent image file in the specified directory'''
#     most_recent_thumb = None
#     for file in os.listdir(directory):
#         if file.endswith('.jpg' or '.png'):
#             if most_recent_thumb is None or os.path.getmtime(file) > os.path.getmtime(most_recent_thumb):
#                 most_recent_thumb = file
#     return most_recent_thumb
# 
# def append_image_to_video(video_file, image_file):
#     '''Appends the specified image file to the end of the specified video file'''
#     video_clip = mp.VideoFileClip(video_file)
#     image_clip = mp.ImageClip(image_file)
#     video_clip.append(image)
#     video_clip.write_videofile(video_file)
#     
# if __name__ == '__main__':
#     video_file =  # !!!Enter path of video file here!!!
#     image_file = get_most_recent_thumb( # !!!Enter path of image file here!!!)
#     append_image_to_video(video_file, image_file)
    
"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"    
    
                                                   
    
def move_pics():
    move_thumbs()
    move_jpgs()
    Lg.logger.info(f'FileScripts:Image .png files have been moved to /Thumbs/Output/@ {Tm.my_time} ')
    Lg.logger.info(f'FileScripts:Image .jpg files have been moved to /Mandala Final Thumbs/@ {Tm.my_time} ')
# move_pics()    




# Empties the Pictures folder where final jpgs are stored. Default is to leave commented to avoid accidental purging.
# def clear_pics_mandalas():
#     file = pathlib.Path('/home/sels/Pictures/Mandalas/')
#     if file.exists ():
#         shutil.rmtree('/home/sels/Pictures/Mandalas/') #       os.makedirs('/home/sels/Pictures/Mandalas/')
#     else:
#         os.makedirs('/home/sels/Pictures/Mandalas/')
#     Lg.logger.info(f'FileScripts:Pictures/Mandalas/ folder has been emptied. All files therein were permanently deleted.')

   

   

# Run this to ensure Dropbox is updated with current python modules
def update_all():
    import os
    current_path()
    move_pics()
    current_path()
    code_backup()
    current_path()
    os.chdir(my_work_dir)
    current_path()
    Lg.logger.info(f'FileScripts:Pics have been moved to Pictures folder and Dropbox has been updated @ {Tm.my_time} ')



# RUN THIS TO RESET THUMBS AND PICS FOLDERS. LEAVE COMMENTED TO AVOID ACCIDENTAL PURGING OF ALL FILES!
# def reset_images():
#     move_pics()
#     clear_Thumbs()
#     clear_pics_mandalas()
#     Lg.logger.info(str('Current time is    ' + str(Tm.this_time)))

# Empties the folder where the .png files are stored for video processing

def make_file_folder():
    Lg.logger.info(f'FileScripts:Starting make_file_folder() @ {Tm.my_time} ...................')
#     t.folder_name = t.my_project
    delete_characters(t.splash,"'[]'")
    shutil.rmtree(my_thumbs + t.folder_name + '/')
    os.makedirs(my_thumbs + t.folder_name + '/')
    Lg.logger.info(f'FileScripts:New temp directory /Looped_Pics/Thumbs/{t.folder_name} has been created @ {Tm.my_time}')



'^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'

      
    
    

  
# showing final clip
#clip.ipython_display()
'====================================================================================='
# make_video()
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'




    
'''Use this to manually match a video clip to an audio clip to create a composite.'''
# Long Duration mp4 to be stripped of shorter audio and then mated with a longer audio
# '/home/sels/Videos/Mandalas/Mystical Mandala by Leon Hatton v.230783807 -r.48002    featuring   680.5    Degree Angles,   with   396 and 852 Hz-FadeBell-7.83sec-42x.mp4' #9.59 minutes
# '/home/sels/Videos/Mandalas/Mystical Mandala by Leon Hatton v.230775214 -r.48002    featuring   408.29999999999995    Degree Angles,   with   Solfeggio_174_bell.mp4' # 9.59 minutes
# '/home/sels/Videos/Mandalas/Mystical Mandala by Leon Hatton v.230763759 -r.48002    featuring   136.1    Degree Angles,   with   396 and 963 Hz-FadeBell-7.83sec-42x.mp4' # 9.59 minutes

#  Long Duration clips with no audio and need long audio to be added, using  make_my_movie script
# A. '/media/sels/My_Media/Videos/no_audio/Brave Mandala Extended v.230645327_308.57142699999997_528 and 852 Hz-FadeBell-7p83sec-42x.mp4' # Successfuly completed and published to YouTube on 3/17/2023
# B = '/media/sels/My_Media/Videos/no_audio/Mystical Mandala by Leon Hatton v.230783807 -r.48002_680.5_396 and 852 Hz-FadeBell-7.83sec-42x.mp4' # Composite created with # 1 on 3/20/2023
# C '/media/sels/My_Media/Videos/no_audio/Mystical Mandala by Leon Hatton v.230775214 -r.48002_408.29999999999995_Solfeggio_174_bell.mp4'
# D. '/media/sels/My_Media/Videos/no_audio/Mystical Mandala by Leon Hatton v.230763759 -r.48002_136.1_396 and 963 Hz-FadeBell-7.83sec-42x.mp4'
# 03-23-2023
# D = '/media/sels/My_Media/Videos/no_audio/Majestic Mandala Extended v.230825258_300.0_639 Hz-bell-6sec120x.mp4'
# C = '/media/sels/My_Media/Videos/no_audio/Majestic Mandala Extended v.230825413_1188.0_741 Hz-bell-6sec120x.mp4'
# A ='/media/sels/My_Media/Videos/no_audio/Majestic Mandala Extended v.230825033_792.0_417 Hz-bell-6sec120x.mp4'
# B = '/media/sels/My_Media/Videos/no_audio/Majestic Mandala Extended v.230820642_396.0_396 Hz-bell-6sec120x.mp4'
#   Y = '/media/sels/My_Media/Videos/no_audio/Joyous Mandala v.231423327-r.67128_150.0_285hz-bell-6sec60x-stereo.mp4'
# F = '/home/sels/Videos/no_audio/Awesome Mandala-(7)1124, 2248, 3372, 4496, 5620, 6744, 7868 angles-Audio-396Hz-fadebell-18min-232755617.mp4'
G = '/home/sels/Videos/no_audio/Random Mandalas-(4)135, 270, 405, 675 degrees angles-Audio-F Project- Crown Chakra Tones-1726, 344.12, 688.24, 1376.48-36min-232825430.mp4'
#Long Duration Audio Clips
# '/home/sels/Music/Solfeggio Tones/174hz-bell-6sec-fade-240x.mp3'
# '/home/sels/Music/Solfeggio Tones/285 Hz-bell-6sec-fade-240x.mp3'
# # Z = '/home/sels/Music/Solfeggio Tones/396 Hz-bell-6sec-fade-240x.mp3'
# # Y = '/home/sels/Music/Solfeggio Tones/417 Hz-bell-6sec-fade-240x.mp3'
# M = '/home/sels/Music/Solfeggio Tones/639 Hz-bell-6sec-fade-240x.mp3'
# '/home/sels/Music/Solfeggio Tones/741 Hz-bell-6sec240x.mp3'
# '/home/sels/Music/Solfeggio Tones/852 Hz-bell-6sec240x.mp3'
# '/home/sels/Music/Solfeggio Tones/963 Hz-bell-6sec240x.mp3'
# H = '/home/sels/Music/Solfeggio Tones/Solfeggio_528_bell_6sec-fade-240x.mp3'
# M = '/home/sels/Music/Audio Clips for Python/Earth Tones/194.18-388.36-1165.08-earthtones-6secbellx180.mp3' 
N = '/home/sels/Music/Audio Clips for Python/SevenChakraTones-144-432-528-639-741-852-1296 Hz.mp3'
def make_my_movie():
    global my_video, my_audio
    t.turtle.bye()
    my_key = str(Tm.this_time)
    my_title = 'Random Mandalas-(4)135, 270, 405, 675 degrees angles-Audio-SevenChakraTones-144-432-528-639-741-852-1296 Hz' # Enter Title
    my_str = f'{my_title}-{Tm.project_time}'
    folder_name = f'/home/sels/Videos/Special/{my_title}'
    os.makedirs(f'{folder_name}',  exist_ok=True)
    Lg.logger.info(f'FileScripts:Folder name is: {folder_name}')
    Lg.logger.info(f'FileScripts:File Name is: {my_str}')
    #Paste full video path (from no_audio library)
    my_video =  G #F #C #A # B
    #Paste full audio path
    my_audio =  N #H #Y #Z # '/home/sels/Music/Solfeggio Tones/Solfeggio_528  Hz_bell_6sec_*120.mp3'
    Lg.logger.info(f'FileScripts:Starting make_my_movie() @ {Tm.this_time}')
    os.chdir(f'{folder_name}')
    new_video = '__temp__.mp4'
    videoclip = VideoFileClip(my_video)
    Lg.logger.info(f'FileScripts:The duration of this video clip is {videoclip.duration / 60:.2f} minutes')
    audioclip = AudioFileClip(my_audio)
    audioclip = audioclip.set_duration(videoclip.duration + 6)
    Lg.logger.info(f'FileScripts:The duration of this audio clip is {audioclip.duration / 60:.2f} minutes')
    new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip
    videoclip.write_videofile(f'{folder_name}/{my_title}.mp4')
    Lg.logger.info(f'FileScripts:The duration of this new video is {videoclip.duration / 60:.2f} minutes')
    Lg.logger.info(f'FileScripts:This new video has been renamed to {my_title}.mp4')
    Lg.logger.info(f'FileScripts:The running of this module, make_my_movie, has successfully completed @ {Tm.this_time}')
    os.chdir(my_work_dir)
    time.sleep(3)
    Lg.logger.info('=========================================================================================================')
    
# make_my_movie()    
    
''' Future - set audio clip to match video and vice versa as needed
    clip_duration = videoclip.duration+6
    audioclip = AudioFileClip("huru.wav").set_duration(clip_duration)
    new_audioclip = CompositeAudioClip([audioclip])
    clip = clip.set_audio(new_audioclip)
    video = CompositeVideoClip([clip, txt_clip]).set_duration(clip_duration)

'''    
    
# sync_av()






def append_to_text():
    import sys
    filename.txt = str(t.my_project + 'ran on' + str(Tm.datetime))
    Lg.logger.info(f'FileScripts:This message will be displayed on the screen.')
    Lg.logger.info( 'This, too!')
   

    with open('filename.txt', 'a') as f:
        sys.stdout = f # Change the standard output to the file we created.
        Lg.logger.info(f'FileScripts:This message will be written to a file.')
        Lg.logger.info(f'FileScripts:This, too! ')
        Lg.logger.info( 'And this too?')
        
    
# Change File Permissions to read/write
def change_file_mode():
    import subprocess
    my_directory = 'media/sels/Backup/'
    subprocess.call[('chown', 'sels', 'my_directory')]
    subprocess.call(['chmod', '-R', '+w', my_directory]) #Change the directory path as needed
# change_file_mode()



# Make multiple copies of a file
def copy_pics():
    for num in range(300):
        src = my_work_dir + 'Images/An Awesome Polygram Mandala featuring 1512  Degree Angles_999_.jpg'  
        dest = my_work_dir + 'An Awesome Polygram Mandala featuring 1512  Degree Angles' + str(num) + '.jpg'
        destination  = shutil.copyfile(src, dest)
    Lg.logger.info(f'FileScripts:Files have been copied')   
# copy_pics()   


'**************************************************************************************************************************************'
this_file = my_work_dir +'/Make_Mandalas/my_angles.py'

def log_info_to_file():
    my_file = open(this_file)
    for line in my_file:
        Lg.logger.info(line)
#  logger_f.info_to_file()        



# Pause routine, wait for mouse click. if not, continue. if click, stop. Run at end of each angle loop.
def keep_on():
    
    Lg.logger.info(f'FileScripts:Terminate? Type "y" to Quit')
    Lg.logger.info(f'FileScripts:Waiting 5 seconds. If no response, will continue')
    answer = sc.textinput('Your choice:   ', 'n')
    time.sleep(5)
    
    if(str(answer) == "y"):
        quit()
    else:
        pass
       
    
def copy_mp3s():
     if my_os == 'Linux':
         try:
             origin = r'/home/sels/Music/ripped/wav//'
             destination = r'/home/sels/Music/truncated//'
             endswith_ = '.mp3'
             [shutil.copy(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
             Lg.logger.info(f'FileScripts:Copying music from ripped/wav to truncated.....')
         except shutil.SameFileError as e:
             pass 
     else:
         pass
     Lg.logger.info(f'FileScripts:Copying Completed!')


 
 
#  def copy_script_to_win():
#      if my_os == 'Linux':
#          try:
#          origin = 
#          destination = r'/home/sels/Music/truncated//'
#          endswith_ = '.mp3'
#          [shutil.copy(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
#          Lg.logger.info(f'FileScripts:Copying music from ripped/wav to truncated.....')
#      except shutil.SameFileError as e:
#          pass 
#  else:
#      pass
# Lg.logger.info(f'FileScripts:Copying Completed!')   
# copy_mp3s()    

# import os
# import shutil
# 
# source_folder = r"E:\demos\files\reports\\"
# destination_folder = r"E:\demos\files\account\\"
# 
# # fetch all files
# source_folder = my_work_dir + r'Audio Clips for Python'
# destination_folder = my_work_dir + TBD
# for file_name in os.listdir(source_folder):
#     # construct full file path
#     source = source_folder + file_name
#     destination = destination_folder + file_name
#     # copy only files
#     if os.path.isfile(source):
#         shutil.copy(source, destination)
#         Lg.logger.info(f'FileScripts:copied from   ' + source + '   to   ' + destination)        
#
# Needs a lot of work as of 8/14/2022 when first tried
def pause_option():
    answer = input('Stop? Enter y or n')
    if answer == 'y':
       exit
    elif answer == 'n':
       pass
    else:
        Lg.logger.info(f'FileScripts:Enter y or n')
        time.sleep(10)
        pass
# pause_option()    



#Utility to clear screen and reset to sequence next screen drawing
def reset_all():
    import time
    t.turtle.reset()
    t.my_pen.reset()
    t.le.reset()
    t.me.reset()
    t.lb.reset()
    t.la.reset()
    t.lg.reset()
    t.ld.reset()
    t.lr.reset()
    t.lc.reset()
    t.ll.reset()
    t.lu.reset()
    t.lm.reset()
    t.lu.reset()
    t.li.reset()
    time.sleep(5)
    
    Lg.logger.info('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    
def get_video_duration():
#     my_work_dir = no_audio_vids
    my_work_dir = my_full_vids
    for filename in Path(my_work_dir).glob('*.mp4'):
            clip = (VideoFileClip(filename.as_posix())) #filename.as_posix(), ))
            Lg.logger.info('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            Lg.logger.info(str(filename) + ': ' + str(round(clip.duration /60)) + ' minutes')   
# get_video_duration()    
    
    
    
    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def purge_thumbs():
    #Get the current time
    now = time.time()
    
    # Get the directory containung the thumbs
    dir_path = '/home/sels/Thumbs/'
    
    # Get all the png files in the directory
    png_files = [f for f in os.listdir(dir_path) if f.endswith('.png')]
    
    # For each PNG file, check if it was created more than a week ago
    for png_file in png_files:
        file_creation_time = os.path.getctime(os.path.join(dir_path, png_file))
        if now - file_creation_time > 1: #604800: # use 1 for immediate run; #604800:  # 1 week in seconds; default
            #Delete the file
            os.remove(os.path.join(dir_path, png_file))
# purge_thumbs()

# def remove_chars:
#     global t.folder_name
#     translation_table = {ord("["): None, ord("]"): None, ord("'" None}
# 
#     t.folder_name = string.translate(translation_table)
# 
#     print(t.folder_name)










# def delete_characters(string, characters):
#     """Deletes the specified characters from the string.
# 
#     Args:
#     string: The string to delete characters from.
#     characters: The characters to delete.
# 
#     Returns:
#     The string with the specified characters deleted.
#     """
# 
#     new_string = t.my_project
# 
#     for character in characters:
#     t.my_filename = new_string.replace(character, "")
# 
#     return new_string
# 
# 
# if __name__ == "__main__":
#   string = "This is a test string"
#   characters = "ab"
# 
#   new_string = delete_characters(string, characters)
# 
#   print(new_string)
# 





# import os
# 
# def get_system_user_id():
#   """Get the system user ID.
# 
#   Returns:
#     The system user ID.
#   """
# 
#   return os.getuid()
#    
#   
# 
# if __name__ == "__main__":
#   print(get_system_user_id())
#   print('The system user id is:  ' + str((get_system_user_id())))
#   print(get_system_user_id())
#   print('The system user id is:  ' + str((get_system_user_id())))  
# 
# def change_ownership_and_permissions(path, user):
#     """Change the ownership of the file or directory at `path` to `user` and give
#       the user write, create, and modify permissions.
# 
#       Args:
#         path: The path to the file or directory.
#         user: The username of the user to give ownership to.
#       """
#     uid = os.getuid()
#     gid = os.getgid()
#     os.chown(path, uid, gid)
#     os.chmod(path, 0o777)
#   
#     os.chown(path, user, -1)  # -1 means don't change the group.
#     os.chmod(path, 0o664)  # Give user write, create, and modify permissions.
# 
# if __name__ == "__main__":
#   path = '/media/sels/LINWINSWAP/' 
#   user = 'sels'
#   change_ownership_and_permissions(path, user)
# 
# # get_system_user_id()
# # change_ownership_and_permissions(path, user)
# 





  

    

