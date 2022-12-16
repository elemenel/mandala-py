#FileScripts.py contains file manipulation scripts associated with master_mandala_maker.py
             # by LeonRHatton

import os
import sys
import platform
import random
import dirsync
from PIL import Image #module for converting python output to image
import numpy as np
import cv2
import pyautogui
import datetime as datetime
import sys
import shutil
import Timer as Tm
import My_template as t
import time
from shutil import copytree
import pathlib
from pathlib import Path
import moviepy.editor as mp
import natsort
from natsort import humansorted as hs
import glob
# from glob import glob, iglob
import imageio
import my_angles as a
from moviepy.editor import *
import audio_clips as au
from moviepy.editor import AudioFileClip, ImageClip, VideoFileClip
from pydub import *
from turtle import Screen as sc
from functools import lru_cache
from pathlib import Path
from moviepy.video.io.VideoFileClip import VideoFileClip

#Assign correct system path for cross-platform capability
global my_work_dir
if sys.platform.startswith('linux'):
    my_home_dir = '/home/elemen'
    my_work_dir = '/media/elemen/Inland SSD1'
    my_no_audio_video_path = '/media/elemen/Inland SSD1/no_audio/'
    my_full_vids_video_path = '/media/elemen/Inland SSD1/Full_Vids/'
    my_audio_path = '/media/elemen/Inland SSD1/'
    my_git_path = '/home/elemen/Git/'
    
    
else:
    my_work_dir = 'M:'
    my_no_audio_video_path = 'N:/'
    my_full_vids_video_path = 'Z:/'
    my_audio_path = 'M:/'
    my_git_path = 'B:/'
    
print(my_work_dir) 
'*********************************************************************************************************'
# Create path variables
global loc_code
loc_code = my_work_dir +'/Make_Mandalas/'

global folder_name
folder_name = 'Images_TBD'

global loc_pic
loc_pic = '/home/elemen/Pictures/Mandala Final Thumbs/' # Store Mandala jpg files here


global con_vid
con_vid = my_work_dir + '/Videos/'

global con_vid_no_audio
con_vid_no_audio = my_work_dir + '/Videos/no_audio/' # Store non audio Mandala videos here

global con_vid_av
con_vid_av = my_work_dir +'/Mandalas/'

global loc_thumb
loc_thumb = my_work_dir + '/Thumbs/Output/' # Store Mandala Thumbs here

global clip_path
clip_path = my_work_dir +'/Audio Clips for Python/'

global full_vid_path
full_vid_path = my_work_dir + '/Videos/no_audio/' + folder_name +'.mp4'








#********************************************************************************************************'
# Copies completed videos to /home/elemen/Videos/Full_Vids for Plex access on Linux
def copy_videos():
     if my_os == 'Linux':
         try:
             origin = '/media/elemen/Inland SSD/Videos/Full_Vids/'
             destination = '/media/elemen/USB SSD-1/Plex/'
             endswith_ = '.mp4'
             [shutil.copy2(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
             print('Copying videos from Inland SSD directory to Plex directory.....')
         except shutil.SameFileError as e:
             pass 
     else:
         pass
     print('Completed videos have been copied to the Plex directory!')   
# copy_videos()
'**********************************************************************************************************'
# Backs up the code to current. Does not archive yet.
# @lru_cache(maxsize = 128)
def code_backup():
    print('Starting code backup...........')
#     shutil.rmtree(my_work_dir +'/Code_Backup/')
    shutil.rmtree('/media/elemen/MANDALABKUP/')
#     src =  my_work_dir +'/Python Code/'
    m_src = my_work_dir +'/Make_Mandalas/'
#     dest = my_work_dir +'/Code_Backup/'
    m_dest = '/media/elemen/MANDALABKUP/'
#     destination = shutil.copytree(src, dest)
    destination = shutil.copytree(m_src, m_dest)
    print('Python Code files have been backed up to MandalaMakerBackup pendrive')
#Default is to leave commented. Uncomment to run from here.    
# code_backup()                                                           



# Empties the folder where the .png files are stored for video processing.
def make_png_folder():
    print('Starting make_png_folder()....................')
    png_folder = pathlib.Path(loc_thumb + folder_name)
    Path(png_folder).mkdir(parents=True, exist_ok=True)
    os.chdir(png_folder)
    print('New folder:  ' + str(png_folder) + '  has been created')
    print(str(png_folder) +'  has been emptied. The folder is now ready for new content.')
# make_png_folder()
    
    
#  This creates a png of each loop. Master Mandala Maker needs this.
def save_thumb():
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite(t.my_str + '_' + str(t.iterable) +'.png', image)

# This creates  png and jpg files of the final image, to be saved out to the Pictures/Mandalas folder. Master Mandala Maker uses this.
def save_final_thumb():
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite(loc_pic + t.my_str +'_' + '999' + '_' +'.jpg', image)
    cv2.imwrite(loc_pic + t.my_str +'_' + '998' + '_' + '.png', image)
    time.sleep(3)


def save_undo():
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite(t.my_str + '+' + str(t.iterable) + '_undo_ ' + '.png', image)
    
def save_final_undo():
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite(t.my_str +'_' + '999' + '_undo_' +'.jpg', image)
    cv2.imwrite(t.my_str +'_' + '998' + '_undo_' + '.png', image)    

# def report_run():
#     image = pyautogui.screenshot()
# #     image.save(t.my_str + '_' + str(t.iterable) +'.png')
#     image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
#     cv2.imwrite(/home/documents/run_reports/ +'.png', image)
    
    
# Moves images to their respective locations from the code file and leaving .py files only
# Master Mandala Maker depends on this. Using list comprehension syntax.
def move_pngs():
    origin = loc_code
    destination = loc_thumb + folder_name
    endswith_ = '.png'
    [shutil.move(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
    print('Image .png files have been moved to /Thumbs/Output/')

def move_jpgs():
    origin = loc_code
    destination = loc_pic #+ folder_name
    endswith_ = '.jpg'
    [shutil.move(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
    print('Jpg files have been moved to ' + str(destination))
# move_jpgs()

def move_pics():
    move_pngs()
    move_jpgs()
#     print('Image .png files have been moved to /Thumbs/Output/')
#     print('Image .jpg files have been moved to /Mandala Final Thumbs/')
# move_pics()    

# Video files originate in the /media/elemen/Thumbs/Output folder. This will move them to the /media/elemen/Container/Videos folder.
# Moves images to their respective locations from the code file and leaving .py files only, then to larger size drive(Container)
# Runs best with Master Mandala Maker. Using list comprehension syntax.

def move_all():
    origin = loc_thumb
    destination = con_vid
    endswith_ = '.avi'
    [shutil.move(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
    print('Video .avi files have been moved to /Videos/')
    
    origin = loc_thumb
    destination = con_vid_no_audio
    endswith_ = '.mp4'
    [shutil.move(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
    print('Video .mp4 files have been moved to /Videos/')
    
    origin = loc_thumb
    destination = con_vid
    endswith_ = '.webm'
    [shutil.move(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
    print('Video .webm files have been moved to /Videos/')
    
    origin = loc_code
    destination = loc_thumb + folder_name
    endswith_ = '.png'
    [shutil.move(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
    print('Image .png files have been moved to /Thumbs/Output/')
    
    origin = loc_thumb + folder_name
    destination = loc_pic
    endswith_ = '.jpg'
    [shutil.move(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
    print('Image .jpg files have been moved to /home/elemen/Pictures/Mandala Final Thumbs/')
    print('================================================================================')
# move_all()



# Empties the Pictures folder where final jpgs are stored. Default is to leave commented to avoid accidental purging.
# def clear_pics_mandalas():
#     file = pathlib.Path('/home/elemen/Pictures/Mandalas/')
#     if file.exists ():
#         shutil.rmtree('/home/elemen/Pictures/Mandalas/') #       os.makedirs('/home/elemen/Pictures/Mandalas/')
#     else:
#         os.makedirs('/home/elemen/Pictures/Mandalas/')
#     print('Pictures/Mandalas/ folder has been emptied. All files therein were permanently deleted.')

   
# Function to get the current working directory   
def current_path():
    import os
    print('Current working directory is:')
    print(os.getcwd())
    print()

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
    print('Pics have been moved to Pictures folder and Dropbox has been updated')

def clear_thumbs():
    print('Preparing to empty the Thumbs folder.......')
    shutil.rmtree(loc_thumb)
    os.makedirs(loc_thumb)
    print('Thumbs folder has been emptied')
# clear_thumbs()

# RUN THIS TO RESET THUMBS AND PICS FOLDERS. LEAVE COMMENTED TO AVOID ACCIDENTAL PURGING OF ALL FILES!
# def reset_images():
#     move_pics()
#     clear_Thumbs()
#     clear_pics_mandalas()
#     print(str('Current time is    ' + str(tm.my_time)))

# Empties the folder where the .png files are stored for video processing

def make_file_folder():
    print('Staring make_file_folder()...................')
#     folder_name = t.my_str
    shutil.rmtree(loc_thumb + folder_name + '/')
    os.makedirs(loc_thumb + folder_name + '/')
    print('New temp directory /Looped_Pics/Thumbs/' + folder_name + '   has been created')



'^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'
# Master Mandala Maker depends on the 'make_video' function to create videos from the 255+ .png files.
# This works using moviepy on a single folder. Does not loop. Optional codecs are 'mpeg4', libx264(.mp4), 'rawvideo'(.avi),\
 # libvpx(webm)-HTML5 and browser videos.

def make_video():
    print('Starting make_video()..................')
    import os
    import moviepy.video.io.ImageSequenceClip
    import moviepy.editor as mp
    import natsort
    from natsort import humansorted
    import my_angles as a
    fps = 3.0 #2.0 1.5
    # Make images directory current
#     os.chdir(loc_thumb + folder_name)
    image_files = humansorted(os.listdir('.')) #Collect and sort .png files
    my_clip =  moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
    my_clip.set_duration(600)
    # Write sequenced png files to a single .mp4 file normally less than 10 mb, quality as good as much larger .avi file
    my_clip.write_videofile( con_vid_no_audio + folder_name + '.mp4', fps = 40, #24
                            codec = 'libx264', bitrate = None, audio = False, audio_fps = 44100, preset='medium', audio_nbytes=4,
                            audio_codec= 'mp3', audio_bitrate= None, audio_bufsize=4000, temp_audiofile = my_work_dir + '/temp',
                            remove_temp= True, write_logfile= True, threads=None,
                            ffmpeg_params= None, logger= 'bar')
    print('mp4 vid-only duration: ' + str(my_clip.duration / 60) + '  minutes')
    
    print('Thumb images conversion to audio-less mp4 video file completed!')
  
# make_video()
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
def get_duration():
    from moviepy.editor import VideoFileClip
    clip = VideoFileClip(my_clip)
    print('Duration: ' + my_clip.duration )
    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
# Used by Master Mandala maker Module to create videos from looped .png files
def set_vid_env():
    print('Starting set_vid_env().............')
    current_path()
#     os.chdir(loc_thumb + folder_name)
#     print('The current folder is:  ' + loc_thumb + folder_name)
    make_video()
    os.chdir(my_work_dir + '/Make_Mandalas/')

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
#  https://www.geeksforgeeks.org/moviepy-assigning-audio-clip-to-video-file/
# Used by Master Mandala maker to generate videos with sound by merging audio clips to video clips
def sync_av():
    print('Starting sync_av()......................')
    os.chdir(con_vid)
    new_video = '__temp__.mp4'
    print('Folder name is:  ' + str(folder_name))
    my_file = folder_name
    print('File Name is  ' + my_file)
    videoclip = VideoFileClip(my_audio_path + 'Videos/no_audio/' + my_file +'.mp4')
    audioclip = AudioFileClip(au.my_audio_clip)
    print('The duration of this clip is   ' + str(audioclip.duration / 60) + '  minutes')
#     full_vid_path = my_work_dir + str('/Videos/Full_Vids/' + folder_name + '.mp4')
    new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip
    videoclip.write_videofile(my_audio_path + str('Videos/Full_Vids/' + t.my_str + '.mp4'))
    print('The duration of the new video is ' + str(videoclip.duration / 60) + '  minutes')
    print('The new video has been renamed to    ' + t.my_str + '.mp4')
    os.chdir(loc_code)
    time.sleep(12)
    print('====================================================================')    
    
# sync_av()





def append_to_text():
    import sys
    filename.txt = str(t.my_str + 'ran on' + str(Tm.datetime))
    print('This message will be displayed on the screen.')
    print( 'This, too!')
    original_stdout = sys.stdout # Save a reference to the original standard output

    with open('filename.txt', 'a') as f:
        sys.stdout = f # Change the standard output to the file we created.
        print('This message will be written to a file.')
        print('This, too! ')
        print( 'And this too?')
        sys.stdout = original_stdout # Reset the standard output to its original value    
    
# Change File Permissions to read/write
def change_file_mode():
    import subprocess
    subprocess.call(['chmod', '-R', '+w', png_folder]) #Change the directory path as needed
    
# change_file_mode()

def return_print_to_console():
    sys.stdout.close()
    sys.stdout=stdoutOrigin
# return_print_to_console()

# Make multiple copies of a file

def copy_pics():
    for num in range(300):
        src = my_work_dir + 'Images/An Awesome Polygram Mandala featuring 1512  Degree Angles_999_.jpg'  
        dest = my_work_dir + 'An Awesome Polygram Mandala featuring 1512  Degree Angles' + str(num) + '.jpg'
        destination  = shutil.copyfile(src, dest)
    print('Files have been copied')   
        
# copy_pics()   


'**************************************************************************************************************************************'
this_file = my_work_dir +'/Make_Mandalas/my_angles.py'

def print_to_file():
    my_file = open(this_file)
    for line in my_file:
        print(line)
# print_to_file()        



# Pause routine, wait for mouse click. if not, continue. if click, stop. Run at end of each angle loop.
def keep_on():
    
    print('Terminate? Type "y" to Quit')
    print('Waiting 5 seconds. If no response, will continue')
    answer = sc.textinput('Your choice:   ', 'n')
    time.sleep(5)
    
    if(str(answer) == "y"):
        quit()
    else:
        pass
       
    
def copy_mp3s():
     if my_os == 'Linux':
         try:
             origin = r'/home/elemen/Music/ripped/wav//'
             destination = r'/home/elemen/Music/truncated//'
             endswith_ = '.mp3'
             [shutil.copy(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
             print('Copying music from ripped/wav to truncated.....')
         except shutil.SameFileError as e:
             pass 
     else:
         pass
     print('Copying Completed!')
     
#  def copy_script_to_win():
#      if my_os == 'Linux':
#          try:
#          origin = 
#          destination = r'/home/elemen/Music/truncated//'
#          endswith_ = '.mp3'
#          [shutil.copy(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
#          print('Copying music from ripped/wav to truncated.....')
#      except shutil.SameFileError as e:
#          pass 
#  else:
#      pass
#  print('Copying Completed!')   
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
#         print('copied from   ' + source + '   to   ' + destination)        
#
# Needs a lot of work as of 8/14/2022 when first tried
def pause_option():
    answer = input('Stop? Enter y or n')
    if answer == 'y':
       exit
    elif answer == 'n':
       pass
    else:
        print('Enter y or n')
        time.sleep(10)
        pass
# pause_option()    


# shutil.rmtree('/home/elemen/Videos/Mandala_Vids/')

#  Sync two folders from https://stackoverflow.com/questions/54688687/how-to-synchronize-two-folders-using-python-script
def sync_mandala_folders():
    from dirsync import sync
    source_path = my_work_dir + '/Videos/Full_Vids/'
    target_path = '/home/elemen/Videos/Mandalas/'
    
    source_path_a = my_work_dir + '/Make_Mandalas/'
    target_path_a = '/home/elemen/Git/mandala-py/'
#     target_path_b = '/media/elemen/MANDALABKUP/'
    

    sync(source_path, target_path, 'sync') #for syncing one way
    sync(source_path_a, target_path_a, 'sync')
#     sync(source_path_a, target_path_b, 'sync')
    
    
    #sync(target_path, source_path, 'sync') #for syncing the opposite way
    #sync(target_path_a, source_path_a, 'sync') #for syncing the opposite way
    print('Sync of Mandala folders completed successfully!')
    print('Sync of Mandala Maker python script files for Git completed successfully!')
#     print('Sync of Mandala Maker python script files to MANDALABKUP pendrive completed successfully!')
    
sync_mandala_folders()


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
    
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    
def get_video_duration():
#     my_work_dir = my_no_audio_video_path
    my_work_dir = my_full_vids_video_path
    for filename in Path(my_work_dir).glob('*.mp4'):
            clip = (VideoFileClip(filename.as_posix())) #filename.as_posix(), ))
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            print(str(filename) + ': ' + str(round(clip.duration /60)) + ' minutes')   
# get_video_duration()    
    
    
