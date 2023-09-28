"""FileScripts.py contains file manipulation scripts
critical to successful functioning of the  master_mandala_maker.py module.
It creates and manipulates all files, and is a fully functioning video creator.
by Leon Hatton
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
# Custom modules listed below
import my_angles as a
import Timer as Tm
import My_template as t
import audio_clips as au
from My_template import my_key
import My_logger as Lg



#Assign correct system path for cross-platform capability
# global my_work_dir
if sys.platform.startswith('linux'):
    my_home_dir = '/home/sels/'
    my_work_dir = '/home/sels/Modules/MandalaMaker/'
    my_log_dir = '/home/sels/Modules/MandalaMaker/Logs/'
    my_video_path = '/home/sels/Videos/'
    my_no_audio_video_path = my_video_path +'no_audio/'
    my_full_vids_video_path = my_video_path + 'Full_Vids/'
    my_audio_path = '/home/sels/Music/Audio Clips for Python/'
    my_git_path = '/home/sels/Git/'
    my_mandala_pics_path = '/media/sels/My_Media/Videos/Pictures/Mandala Final Thumbs/'
    my_thumbs_path = '/home/sels/Thumbs/'
    my_server_folder = my_home_dir + 'Videos/Full_Vids/'
    my_final_thumbs_path = '/home/sels/Pictures/Final Thumbs/'
    my_shared_drive = '/home/sels/sambashare/'
    
    
else:
    my_work_dir = 'D:/'
    my_no_audio_video_path = 'D:/'
    my_full_vids_video_path = 'D:/'
    my_audio_path = 'D:/'
    my_git_path = 'D:/'
    my_home_dir = 'C:/'
    

'*********************************************************************************************************'
# Create path variables

global loc_code
loc_code = my_work_dir

global loc_pic
loc_pic = '/home/sels/Pictures/Final Thumbs/' # Store Mandala jpg files here


global con_vid
con_vid = my_video_path

global con_vid_no_audio
con_vid_no_audio = f'{my_video_path}no_audio/' # Store non audio Mandala videos here

global con_vid_av
con_vid_av = my_work_dir +'Mandalas/'

global loc_thumb
loc_thumb = my_thumbs_path # Store Mandala Thumbs here

global clip_path
clip_path = my_work_dir +'Audio Clips for Python/'

global full_vid_path
full_vid_path = my_video_path + 'Full_Vids/' + t.folder_name +'.mp4'

# global my_rand
# def get_rand():
#     this_rand = random.randint(1,999)
#     my_rand = str(this_rand)
#     print('The value of my_rand is: ' + my_rand)
#     return my_rand
# get_rand()

# global logger
# global formatter, fileHandler, consoleHandler
# logger = Lg.logging.getLogger(t.my_project) # Initialize global logger
# fileHandler = Lg.logging.FileHandler(t.my_logfile)
# fileHandler.setLevel(Lg.logging.INFO)
# consoleHandler = Lg.logging.StreamHandler()
# consoleHandler.setLevel(Lg.logging.INFO)
# logger.setLevel(Lg.logging.INFO)
# logger.addHandler(Lg.fileHandler)
# logger.addHandler(Lg.consoleHandler)
# Lg.logger.info('Logger source: FileScripts.py')

#********************************************************************************************************'
# Copies completed videos to /home/sels/Videos/Full_Vids for Plex access on Linux
def copy_videos():
     if my_os == 'Linux':
         try:
             origin = '/media/sels/My_Media/Videos/Full_Vids/'
             destination = '/media/sels/Media_EXFat/Archived Mandala Videos/'
             endswith_ = '.mp4'
             [shutil.copy2(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
             Lg.logger.info('Copying videos from Inland SSD directory to Plex directory.....')
         except shutil.SameFileError as e:
             pass 
     else:
         pass
     Lg.logger.info('Completed videos have been copied to the Plex directory!')   
# copy_videos()
'**********************************************************************************************************'
# Backs up the code to current. Does not archive yet.
# @lru_cache(maxsize = 128)
def code_backup():
    Lg.logger.info('Starting code backup...........')
#     shutil.rmtree(my_work_dir +'/Code_Backup/')
    shutil.rmtree('/media/sels/USB DISK/Modules - MandalaMaker/') #file:///media/sels/USB DISK/Modules - MandalaMaker
#     src =  my_work_dir +'/Python Code/'
    m_src = my_work_dir +'/Make_Mandalas/'
#     dest = my_work_dir +'/Code_Backup/'
    m_dest = 'media/sels/USB DISK/Modules - MandalaMaker/'
#     destination = shutil.copytree(src, dest)
    destination = shutil.copytree(m_src, m_dest)
    Lg.logger.info('Python Code files have been backed up to MandalaMakerBackup pendrive')
#Default is to leave commented. Uncomment to run from here.    
# code_backup()                                                           

def make_daily_activities_log():
    Lg.logger.info(f'Creating today\'s activity log file')
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
      Lg.logger.info('This is a log message from my_module.')
  
    if __name__ == '__main__':
        main()
  
 
#     log_folder = f'{my_log_dir}{Tm.my_date}'
#     os.makedirs(log_folder, exist_ok=True)
#     os.chdir(log_folder)
#     Lg.logger.info(f'Logging Module {t.folder_name}')
# make_daily_activities_log()    

# Empties the folder where the .png files are stored for video processing.
global png_folder
png_folder = ' '
def make_png_folder():
    png_folder = loc_thumb + t.folder_name
    os.makedirs(png_folder, exist_ok=True)
    os.chdir(png_folder)
    return png_folder
    my_project = png_folder
    Lg.logger.info('New folder:  ' + str(png_folder) + '  has been created')
    Lg.logger.info(str(png_folder) +'  has been emptied. The folder is now ready for new content.')
# make_png_folder()


folder_name = 'novanno_archive'
'''Create a folder to store new mandala along with a copy of the current python module version'''
def make_archive_folder():
    archive_folder = '/media/sels/Backup/MandalaScriptsBackup/'
    os.makedirs(archive_folder + t.folder_name, exist_ok=True)
    my_archive_folder = archive_folder + t.folder_name
    endswith_ = '.py'
    origin = my_work_dir
    destination = my_archive_folder
    [shutil.copy(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
    return archive_folder
    
# make_archive_folder()

def make_reverse_png_folder():
    reverse_png_folder = f'{loc_thumb}{t.folder_name}'
    os.makedirs(reverse_png_folder, exist_ok=True)
    os.chdir(reverse_png_folder)
    return reverse_png_folder
    my_project = reverse_png_folder
    Lg.logger.info(f'New folder:  {reverse_png_folder} has been created')
    Lg.logger.info(f'{reverse_png_folder} has been emptied. The folder is now ready for new content.')
    

# # Empties the folder where the .png files are stored for video processing.
# global png_folder
# png_folder = ' '
# def make_png_folder():
#     png_folder = loc_thumb + t.folder_name
#     os.makedirs(png_folder, exist_ok=True)
#     os.chdir(png_folder)
#     return png_folder
#     my_project = png_folder
#     Lg.logger.info('New folder:  ' + str(png_folder) + '  has been created')
#     Lg.logger.info(str(png_folder) +'  has been emptied. The folder is now ready for new content.')
# # make_png_folder()
# 
# 
# folder_name = 'novanno_archive'
# '''Create a folder to store new mandala along with a copy of the current python module version'''
# def make_archive_folder():
#     archive_directory = '/media/sels/USB_ARK/MandalaMakerArchive/'
#     os.makedirs(archive_directory + t.folder_name + '/', exist_ok=True)
# #     os.makedirs((archive_directory + t.folder_name.replace('[', ''), 
#     my_archive_folder = archive_directory + t.folder_name + '/'
#     endswith_ = '.py'
#     origin = my_work_dir
#     destination = my_archive_folder
#     [shutil.copy(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
#     return my_archive_folder
#     
# # make_archive_folder()
# 
# def make_reverse_png_folder():
#     reverse_png_folder = loc_thumb + 'reverse-' + t.folder_name
#     os.makedirs(png_folder, exist_ok=True)
#     os.chdir(reverse_png_folder)
#     return reverse_png_folder
#     my_project = png_folder
#     Lg.logger.info('New folder:  ' + str(reverse_png_folder) + '  has been created')
#     Lg.logger.info(str(reverse_png_folder) +'  has been emptied. The folder is now ready for new content.')
#     
#  This creates a png of each loop. Master MandalaMaker needs this.
def save_thumb():
    image = PIL.ImageGrab.grab()
#     image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    Tm.set_time()
    cv2.imwrite(f'{loc_thumb}/{t.folder_name}/{Tm.iterable_time}.png',image)

# This creates  png and jpg files of the final image, to be saved out to the Pictures/Mandalas folder. Master MandalaMaker uses this.
def save_final_thumb():
    global my_last_png, my_last_jpg
    image = PIL.ImageGrab.grab()
#     image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    Tm.set_time()
    cv2.imwrite(f'{my_mandala_pics_path}/{t.folder_name}-{Tm.iterable_time}.png', image)
    cv2.imwrite(f'{my_final_thumbs_path}/{t.folder_name}_final.jpeg', image)
#     cv2.imwrite(f'{my_mandala_pics_path}/{t.folder_name}_{Tm.iterable_time}.jpg', image)
 
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
    
    
# Moves images to their respective locations from the code file and leaving .py files only
# Master MandalaMaker depends on this. Using list comprehension syntax.
def move_pngs():
    origin = loc_code
    destination = loc_thumb + t.folder_name
    endswith_ = '.png'
    [shutil.move(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
    Lg.logger.info('Image .png files have been moved to /Thumbs/Output/')

def move_jpegs():
    # Get the path to the current directory
    current_directory = loc_code  #.getcwd()

    # Get the path to the directory where the files will be moved
    destination_directory = os.path.join(loc_pic)

    # Get a list of all the files in the current directory
    files = os.listdir(current_directory)

    # Create a list of all the files ending with `jpeg`
    jpeg_files = [file for file in files if file.endswith('.jpeg')]

    # Move the jpeg files to the destination directory
    for file in jpeg_files:
        shutil.move(file, destination_directory)

    # Print a message to confirm that the files were moved
    Lg.logger.info(f'The jpeg files were successfully moved to {loc_pic}.')

# move_jpegs()

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
    Lg.logger.info('The Thumb files were successfully moved to the destination directory.')
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
    Lg.logger.info('Image .png files have been moved to /Thumbs/Output/')
    Lg.logger.info('Image .jpg files have been moved to /Mandala Final Thumbs/')
# move_pics()    

# Due to their immense sizes, snapshots of running videos are created and stored at a dedicated location.
# Video files are compilations of Thumbs that are sorted and processed. They are converted and stored at '/media/sels/My_Media/Videos/no_audio'.
# Moves images to their respective locations from the code file and leaving .py files only, then to larger size drive(Container)
# Runs best with Master MandalaMaker. Using list comprehension syntax.

def move_all():
    origin = loc_thumb
    destination = con_vid
    endswith_ = '.avi'
    [shutil.move(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
    Lg.logger.info('Video .avi files have been moved to /Videos/')
    
    origin = loc_thumb
    destination = con_vid_no_audio
    endswith_ = '.mp4'
    [shutil.move(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
    Lg.logger.info('Video .mp4 files have been moved to /Videos/')
    
    origin = loc_thumb
    destination = con_vid
    endswith_ = '.webm'
    [shutil.move(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
    Lg.logger.info('Video .webm files have been moved to /Videos/')
    
    origin = loc_code
    destination = loc_thumb # + t.folder_name
    endswith_ = '.png'
    [shutil.move(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
    Lg.logger.info('Image .png files have been moved to /Thumbs/')
    
    origin = loc_thumb # + t.folder_name
    destination = loc_pic
    endswith_ = '.jpg'
    [shutil.move(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
    Lg.logger.info('Image .jpg files have been moved to /home/sels/Pictures/Mandala Final Thumbs/')
    Lg.logger.info('================================================================================')
# move_all()



# Empties the Pictures folder where final jpgs are stored. Default is to leave commented to avoid accidental purging.
# def clear_pics_mandalas():
#     file = pathlib.Path('/home/sels/Pictures/Mandalas/')
#     if file.exists ():
#         shutil.rmtree('/home/sels/Pictures/Mandalas/') #       os.makedirs('/home/sels/Pictures/Mandalas/')
#     else:
#         os.makedirs('/home/sels/Pictures/Mandalas/')
#     Lg.logger.info('Pictures/Mandalas/ folder has been emptied. All files therein were permanently deleted.')

   
# Function to get the current working directory   
def current_path():
    import os
    Lg.logger.info('Current working directory is:')
    Lg.logger.info(os.getcwd())
   

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
    Lg.logger.info('Pics have been moved to Pictures folder and Dropbox has been updated')

def clear_thumbs():
    Lg.logger.info('Preparing to empty the Thumbs folder.......')
    shutil.rmtree(loc_thumb)
    os.makedirs(loc_thumb)
    Lg.logger.info('Thumbs folder has been emptied')
# clear_thumbs()

# RUN THIS TO RESET THUMBS AND PICS FOLDERS. LEAVE COMMENTED TO AVOID ACCIDENTAL PURGING OF ALL FILES!
# def reset_images():
#     move_pics()
#     clear_Thumbs()
#     clear_pics_mandalas()
#     Lg.logger.info(str('Current time is    ' + str(tm.my_time)))

# Empties the folder where the .png files are stored for video processing

def make_file_folder():
    Lg.logger.info('Starting make_file_folder()...................')
#     t.folder_name = t.my_project
    delete_characters(t.splash,"'[]'")
    shutil.rmtree(loc_thumb + t.folder_name + '/')
    os.makedirs(loc_thumb + t.folder_name + '/')
    Lg.logger.info('New temp directory /Looped_Pics/Thumbs/' + t.folder_name + '   has been created')



'^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'
# Master MandalaMaker depends on the 'make_video' function to create videos from the hundreds of .png files.
# This works using moviepy on a single folder. Does not loop. Optional codecs are 'mpeg4', libx264(.mp4), 'rawvideo'(.avi),\
 # libvpx(webm)-HTML5 and browser videos.

def make_video():
    Lg.logger.info('Starting make_video() @ ' + Tm.my_time)
    import os
    import moviepy.video.io.ImageSequenceClip
    import moviepy.editor as mp
    fps = 240 # to speed up use 120
    # Make images directory current
    Lg.logger.info(f'Starting sort of screenshot files at {Tm.my_time}...')
    os.chdir(loc_thumb + t.folder_name)
    sorted_files = hs(os.listdir('.')) #Collect and sort .png files
    Lg.logger.info(f'Ending sort of screenshot files at {Tm.my_time}')
    my_clip =  moviepy.video.io.ImageSequenceClip.ImageSequenceClip(sorted_files, fps=fps)
#     my_clip.set_duration(550)
    Lg.logger.info(f'Creating video from png files @ {Tm.my_time}')
    # Write sequenced png files to a single .mp4 file normally less than 10 mb, quality as good as much larger .avi file
    my_clip.write_videofile(con_vid_no_audio + t.folder_name + '.mp4', fps = fps,  # This determines frame speed and movie length   Industry standard is 24; for shorter length and faster speed use 60
                            codec = 'libx264', bitrate = None, audio = False, audio_fps = 44100, preset='medium', audio_nbytes=4,
                            audio_codec= 'mp3', audio_bitrate= None, audio_bufsize=8000, temp_audiofile = my_work_dir + '/temp',
                            remove_temp= True, write_logfile= True, threads=None,
                            ffmpeg_params= None, logger='bar') #'bar'
    my_vidClip = f'{con_vid_no_audio}{t.folder_name}.mp4'
    clip = VideoFileClip(my_vidClip).subclip(0, 10)    
    # getting frame rate of the clip
    rate = clip.fps
    # printing the fps
    Lg.logger.info(f'FPS :{rate}')
    Lg.logger.info(f'mp4 no_audio duration: {my_clip.duration / 60:.2f} minutes')
    Tm.set_time()
    Lg.logger.info(f'Screenshot images conversion to audio-less mp4 video file completed @ {Tm.my_time}!')
'=================================================================================================='
# Copied from Geeks for Geeks ('https://www.geeksforgeeks.org/moviepy-fps-of-video-file-clip/?ref=rp')

def make_reversed_video():
    Tm.set_time()
    Lg.logger.info(f'Starting make_video() @ {Tm.my_time}')
    import os
    import moviepy.video.io.ImageSequenceClip
    import moviepy.editor as mp
    fps = 120 # to speed up use higher numbers
    # Make images directory current
    Tm.set_time()
    Lg.logger.info(f'Starting sort of screenshot files at {Tm.my_time}...')
    os.chdir(loc_thumb + t.folder_name)
    sorted_files = hs(os.listdir('.')) #Collect and sort .png files
    reverse_sorted_files = hs(os.listdir('.'), reverse = True)
    my_clip =  moviepy.video.io.ImageSequenceClip.ImageSequenceClip(sorted_files + reverse_sorted_files, fps=fps)
#     my_clip.set_duration(550)
    Tm.set_time()
    Lg.logger.info(f'Starting video generation from sorted screenshot files @ {Tm.my_time}')
    # Write sequenced png files to a single .mp4 file normally less than 10 mb, quality as good as much larger .avi file
    my_clip.write_videofile(f'{con_vid_no_audio}{t.folder_name}.mp4', fps = fps,  # This determines frame speed and movie length   Industry standard is 24; for shorter length and faster speed use 60-120
                            codec = 'libx264', bitrate = None, audio = False, audio_fps = 44100, preset='medium', audio_nbytes=4,
                            audio_codec= 'mp3', audio_bitrate= None, audio_bufsize=8000, temp_audiofile = my_work_dir + '/temp',
                            remove_temp= True, write_logfile= True, threads=None,
                            ffmpeg_params= None, logger='bar') #'bar'
    my_vidClip = f'{con_vid_no_audio}{t.folder_name}.mp4'
    clip = VideoFileClip(my_vidClip).subclip(0, 10)    
    # getting frame rate of the clip
    rate = clip.fps
    # printing the fps
    Lg.logger.info(f'FPS : {rate}')
    Lg.logger.info(f'mp4 no_audio duration: {my_clip.duration / 60:.2f} minutes')
    Tm.set_time()
    Lg.logger.info(f'Screenshot images conversion to audio-less mp4 video file completed @ {Tm.my_time}!')
    
      
    
    

  
# showing final clip
#clip.ipython_display()
'====================================================================================='
# make_video()
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
def get_duration():
    from moviepy.editor import VideoFileClip
    clip = VideoFileClip(my_clip)
    Lg.logger.info(f'Duration: {my_clip.duration}')
    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
# Used by Master Mandala maker Module to create videos from looped .png files
def set_vid_env():
    Lg.logger.info('Starting set_vid_env().............')
    current_path()
    os.chdir   (f'{loc_thumb}{t.folder_name}')  #(loc_thumb + t.folder_name)
    Lg.logger.info(f'The current folder is: {loc_thumb}{t.folder_name}')  #+ loc_thumb + t.folder_name)
    make_video()
    os.chdir(my_work_dir)

# Used by Master Mandala maker Module to create videos from looped .png files
def set_reverse_vid_env():
    Lg.logger.info('Starting set_vid_env().............')
    current_path()
    os.chdir(f'{loc_thumb}{t.folder_name}')
    Lg.logger.info(f'The current folder is: {loc_thumb}{t.folder_name}')
    make_reversed_video()
    os.chdir(my_work_dir)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
#  https://www.geeksforgeeks.org/moviepy-assigning-audio-clip-to-video-file/
# Used by Master Mandala maker to generate videos with sound by merging audio clips to video clips
def sync_av():
    Tm.set_time()
    Lg.logger.info(f'Starting sync_av() @ {Tm.my_time}')
    Lg.logger.info('Merging Video with Audio...')
    os.chdir(con_vid)
    new_video = '__temp__.mp4'
    Lg.logger.info(f'Folder name is {t.folder_name}')
    my_file = t.folder_name
    Lg.logger.info(f'File Name is {my_file}')
    videoclip = VideoFileClip(f'{my_video_path}/no_audio/{my_file}.mp4')
    audioclip = AudioFileClip(au.my_audio_clip)
    audioclip = audioclip.set_duration(videoclip.duration + 6)
    Lg.logger.info(f'The duration of this audio clip is {audioclip.duration / 60:.2f} minutes')
#     full_vid_path = my_work_dir + str('/Videos/Full_Vids/' + t.folder_name + '.mp4')
    new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip
    videoclip.duration
    videoclip.write_videofile(f'{my_full_vids_video_path}{t.folder_name}.mp4')
    Lg.logger.info(f'The duration of the new composite video is {videoclip.duration / 60:.2f} minutes')
    Lg.logger.info(f'The new composite video has been renamed to {t.folder_name}.mp4')
    os.chdir(loc_code)
    Lg.logger.info('====================================================================')
    
   # Use this to manually match a video clip to an audio clip to create a composite.
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

def make_my_movie():
    global my_video
    my_key = str(Tm.my_time)
    my_title = 'Colorful Mandala with 150 Degrees Angles and Earth Tones 194.1, 388.36, 1165.08 Hz.' # Enter Title
    my_str = my_title + 'v-' + my_key
    os.makedirs(f'/media/sels/My_Media/Videos/Special/{my_title}',  exist_ok=True)
    #Paste full video path (from no_audio library)
    my_video =  Y #C #A # B
    #Paste full audio path
    my_audio =  M #H #Y #Z # '/home/sels/Music/Solfeggio Tones/Solfeggio_528  Hz_bell_6sec_*120.mp3'
    Lg.logger.info('Starting make_my_movie()......................')
    os.chdir(con_vid)
    new_video = '__temp__.mp4'
    folder_name = f'/media/sels/My_Media/Videos/Special/{my_title}'
    Lg.logger.info('Folder name is:  ' + str(folder_name))
    Lg.logger.info('File Name is  ' + my_str)
    videoclip = VideoFileClip(my_video)
    audioclip = AudioFileClip(my_audio) 
    Lg.logger.info(f'The duration of this clip is {audioclip.duration / 60:.2f} minutes')
    new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip
    videoclip.write_videofile(folder_name + '/' + my_title +'.mp4')
    Lg.logger.info(f'The duration of the new video is {videoclip.duration / 60:.2f} minutes')
    Lg.logger.info(f'The new video has been renamed to {my_title}.mp4')
    os.chdir(loc_code)
    time.sleep(3)
    Lg.logger.info('====================================================================')
    
# make_my_movie()    
    
''' Future - set audio clip to match video and vice versa as needed
    audioclip = AudioFileClip("huru.wav").set_duration(clip_duration)
    new_audioclip = CompositeAudioClip([audioclip])
    clip = clip.set_audio(new_audioclip)
    video = CompositeVideoClip([clip, txt_clip]).set_duration(clip_duration)

'''    
    
# sync_av()






def append_to_text():
    import sys
    filename.txt = str(t.my_project + 'ran on' + str(Tm.datetime))
    Lg.logger.info('This message will be displayed on the screen.')
    Lg.logger.info( 'This, too!')
   

    with open('filename.txt', 'a') as f:
        sys.stdout = f # Change the standard output to the file we created.
        Lg.logger.info('This message will be written to a file.')
        Lg.logger.info('This, too! ')
        Lg.logger.info( 'And this too?')
        
    
# Change File Permissions to read/write
def change_file_mode():
    import subprocess
    my_directory = 'media/sels/Backup'
    subprocess.call[('chown', 'sels', 'my_directory')]
    subprocess.call(['chmod', '-R', '+w', my_directory]) #Change the directory path as needed
# change_file_mode()



# Make multiple copies of a file
def copy_pics():
    for num in range(300):
        src = my_work_dir + 'Images/An Awesome Polygram Mandala featuring 1512  Degree Angles_999_.jpg'  
        dest = my_work_dir + 'An Awesome Polygram Mandala featuring 1512  Degree Angles' + str(num) + '.jpg'
        destination  = shutil.copyfile(src, dest)
    Lg.logger.info('Files have been copied')   
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
    
    Lg.logger.info('Terminate? Type "y" to Quit')
    Lg.logger.info('Waiting 5 seconds. If no response, will continue')
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
             Lg.logger.info('Copying music from ripped/wav to truncated.....')
         except shutil.SameFileError as e:
             pass 
     else:
         pass
     Lg.logger.info('Copying Completed!')
     
#  def copy_script_to_win():
#      if my_os == 'Linux':
#          try:
#          origin = 
#          destination = r'/home/sels/Music/truncated//'
#          endswith_ = '.mp3'
#          [shutil.copy(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
#          Lg.logger.info('Copying music from ripped/wav to truncated.....')
#      except shutil.SameFileError as e:
#          pass 
#  else:
#      pass
# Lg.logger.info('Copying Completed!')   
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
#         Lg.logger.info('copied from   ' + source + '   to   ' + destination)        
#
# Needs a lot of work as of 8/14/2022 when first tried
def pause_option():
    answer = input('Stop? Enter y or n')
    if answer == 'y':
       exit
    elif answer == 'n':
       pass
    else:
        Lg.logger.info('Enter y or n')
        time.sleep(10)
        pass
# pause_option()    


#  Sync two folders from https://stackoverflow.com/questions/54688687/how-to-synchronize-two-folders-using-python-script
#sync(target_path, source_path, 'sync') #for syncing the opposite way
#sync(target_path_a, source_path_a, 'sync') #for syncing the opposite way
def sync_full_vids():
     #Sync Videos
    source_path_videos = '/home/sels/Videos/Full_Vids/'
    target_path = '/home/sels/MandalaBackup/Full_Vids/'
    target_path_shared_videos = my_shared_drive + 'MandalaMaker Full Vids/'
    target_path_media = '/media/sels/My_Media/Mandala Videos_Backup/'
    sync(source_path_videos, target_path, "sync")
    sync(source_path_videos, target_path_shared_videos, 'sync')
    sync(source_path_videos, target_path_media, 'sync')
    Lg.logger.info('Working on sync of MandalaMaker Full Vids folders....')
    Lg.logger.info(f'Sync of Mandala Video folders completed successfully @ {Tm.my_time}')
# sync_full_vids()    
    
def sync_module_folders():
     #Sync Modules
    source_path_a = my_home_dir + 'Modules/'
    target_path_a = '/home/sels/MandalaBackup/Modules/'
    target_path_b = '/media/sels/My_Media/Git/Modules/Mandala_Maker Project/'
    target_path_u = '/media/sels/Backup/'    
    target_path_shared_modules = my_shared_drive + 'MandalaMaker Modules/'   
    sync(source_path_a, target_path_a, 'sync')
    sync(source_path_a, target_path_shared_modules, 'sync')
    sync(source_path_a, target_path_b, 'sync')
    sync(source_path_a, target_path_u, 'sync')
    
    Lg.logger.info('Working on sync of MandalaMaker Module folders....')
    Lg.logger.info(f'Sync of MandalaMaker Module folders completed successfully @ {Tm.my_time}')
# sync_module_folders()

def sync_audio_clips():
    #Sync Audio Clips
    source_path_audio = my_audio_path
    target_path_shared_audio = my_shared_drive + 'MandalaMaker Audio Clips/'
    target_path_back_up_audio = '/media/sels/My_Media/Audio Clips/'
    target_path_u = '/media/sels/Backup/' 
    sync(source_path_audio, target_path_shared_audio, 'sync')
    sync(source_path_audio, target_path_back_up_audio, 'sync')
    sync(source_path_audio, target_path_u, 'sync')
    Lg.logger.info('Working on sync of MandalaMaker Audio folders....')
    Lg.logger.info(f'Sync of MandalaMaker Audio folders completed successfully @ {Tm.my_time}')
# sync_audio_clips()

def sync_images():
     #Sync Images
    source_path_images = loc_pic
    target_path_shared_images = my_shared_drive + 'MandalaMaker Final Images/'
    sync(source_path_images, target_path_shared_images, 'sync')
    Lg.logger.info('Working on sync of MandalaMaker Image folders....')
    Lg.logger.info(f'Sync of MandalaMaker Image  folders completed successfully @ {Tm.my_time}')
# sync_images()    


def sync_mandala_folders():
    #Sync All Folders
    sync_full_vids()
    sync_module_folders()
    sync_audio_clips()
    sync_images()
    
# sync_mandala_folders()


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
#     my_work_dir = my_no_audio_video_path
    my_work_dir = my_full_vids_video_path
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





  