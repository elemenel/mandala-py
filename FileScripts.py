#FileScripts.py contains file manipulation scripts associated with master_mandala_maker.py
             # by LeonRHatton

import os
import platform
import random
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
from glob import glob, iglob
import imageio
import my_angles as a
# import ipython
from moviepy.editor import *
import audio_clips as au
from moviepy.editor import AudioFileClip, ImageClip

my_os = platform.system()
print(my_os)
if my_os == 'Linux':
    my_path = '/media/elemen/Garage'
else:
    my_path = 'E:'

global loc_code
loc_code = my_path +'/Make_Mandalas/'

global folder_name
folder_name = '/Images_TBD'

global loc_pic
loc_pic = my_path + '/Images/' # Store Mandala jpg files here


global con_vid
con_vid = my_path +'/Videos/'

global con_vid_no_audio
con_vid_no_audio = my_path +'/Videos/no_audio/' # Store non audio Mandala videos here

global con_vid_av
con_vid_av = my_path +'/Videos/Full_Vids/'

global loc_thumb
loc_thumb = my_path +'/Output/' # Store Mandala Thumbs here

global clip_path
clip_path = my_path +'/Audio Clips for Python/'

# global random_track
# random_track = random.choice(au.all_clips)
# print (au.my_track)

'**********************************************************************************************************'
# Copies completed videos to /home/elemen/Videos/Full_Vids for Plex access om Linux
def copy_videos():
     if my_os == 'Linux':
         try:
             origin = '/media/elemen/Garage/Videos/Full_Vids/'
             destination = '/home/elemen/Videos/Full_Vids/'
             endswith_ = '.mp4'
             [shutil.copy(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
             print('Copying videos from Garage directory to Home directory.....')
         except shutil.SameFileError as e:
             pass 
     else:
         pass
     print('Completed videos have been copied to the Linux Home directory!')   
# copy_videos()

# Backs up the code to current. Does not archive yet. 
def code_backup():
    shutil.rmtree(my_path +'Code_Backup/')
    shutil.rmtree(my_path +'MandalaMakerBackup/')
    src =  my_path +'Python Code/'
    m_src = my_path +'Make_Mandalas/'
    dest = my_path +'Code_Backup/'
    m_dest = my_path +'MandalaMakerBackup/'
    destination = shutil.copytree(src, dest)
    destination = shutil.copytree(m_src, m_dest)
    print('Python Code files have been backed up to CodeBackup folder')
#Default is to leave commented. Uncomment to run from here.    
# code_backup()                                                           


# Empties the folder where the .png files are stored for video processing. Dependency: Master Mandala Maker    
def make_png_folder():
    png_folder = pathlib.Path(loc_thumb + folder_name +'/')
    Path(png_folder).mkdir(parents=True, exist_ok=True)
    os.chdir(png_folder)
    print('New folder:  ' + str(png_folder) + '  has been created')
    print(str(png_folder) +'  has been emptied. The folder is now ready for new content.')
# make_png_folder()
    
    
#  This creates a png of each loop.
def save_thumb():
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite(t.my_str + '_' + str(t.iterable) +'.png', image)
    
def save_undo():
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite(t.my_str + '+' + str(t.iterable) + '_undo_ ' + '.png', image)
    
    
# This creates  png and jpg files of the final image, to be saved out to the Pictures/Mandalas folder.
def save_final_thumb():
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite(t.my_str +'_' + '999' + '_' +'.jpg', image)
    cv2.imwrite(t.my_str +'_' + '998' + '_' + '.png', image)
   
def save_final_undo():
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite(t.my_str +'_' + '999' + '_undo_' +'.jpg', image)
    cv2.imwrite(t.my_str +'_' + '998' + '_undo_' + '.png', image)    

 
# Moves images to their respective locations from the code file and leaving .py files only
# Runs only with Master Mandala Maker. Using list comprehension syntax.

def move_pngs():
    origin = loc_code
    destination = loc_thumb + folder_name +'/'
    endswith_ = '.png'
    [shutil.move(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
    

def move_jpgs():
    origin = loc_code
    destination = loc_pic + folder_name
    endswith_ = '.jpg'
    [shutil.move(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]  

def move_pics():
    move_pngs()
    move_jpgs()
    print('Image .png files have been moved to /Thumbs/Output/')
    print('Image .jpg files have been moved to /Images/')
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
    print('Image .jpg files have been moved to /Images/')
    
# move_all()




# Empties the Pictures folder where final jpgs are stored. Default is to leave commented to avoid accidental purging.
# def clear_pics_mandalas():
#     file = pathlib.Path('/home/elemen/Pictures/Mandalas/')
#     if file.exists ():
#         shutil.rmtree('/home/elemen/Pictures/Mandalas/') #       os.makedirs('/home/elemen/Pictures/Mandalas/')
#     else:
#         os.makedirs('/home/elemen/Pictures/Mandalas/')
#     print('Pictures/Mandalas/ folder has been emptied. All files therein were permanently deleted.')



# # Using Dropbox as file server to link the windows and phone
# def update_dropbox():
#     from shutil import copytree
#     shutil.rmtree('/media/elemen/Container/Mint_Home/Dropbox/Code/')
#     src =  '/media/elemen/Container/Mint_Home/Documents/Code/'
#     dest = '/media/elemen/Container/Mint_Home/Dropbox/Code/'
#     destination  = shutil.copytree(src, dest)
#     print('Dropbox has been updated to current')
    
    
    
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
    os.chdir(my_path)
    current_path()
    print('Pics have been moved to Pictures folder and Dropbox has been updated')
    
# RUN THIS TO RESET THUMBS AND PICS FOLDERS. LEAVE COMMENTED TO AVOID ACCIDENTAL PURGING OF ALL FILES!
# def reset_images():
#     move_pics()
#     clear_Thumbs()
#     clear_pics_mandalas()
#     print(str('Current time is    ' + str(tm.my_time)))

# Empties the folder where the .png files are stored for video processing 
def make_file_folder():
    folder_name = t.my_str
    shutil.rmtree(loc_thumb + folder_name + '/')
    os.makedirs(loc_thumb + folder_name + '/')
    print('New temp directory /Looped_Pics/Thumbs/' + folder_name + '   has been created')



# Function to Get the current  working directory   
def current_path():
    print('Current Directory now:  ')
    print(os.getcwd())


def update_all():
    move_picture_file()
    update_dropbox()
    # Python program to change the
    # current working directory
    print(str(' Working directory changing from') + '    ' + str(current_path()))
    os.chdir(my_path + 'Python/Make_Mandalas/')
    print (str('Working directory changed to') +'   ' + str(current_path()))

def job():
    update_all()
    print(str('Files were updated as of'  +str(Tm.my_time) +'.'))
# Every day at 12am or 00:00 time bedtime() is called.
    schedule.every().day.at("03:00").do(job)

# job()
# # Loop so that the scheduling task
# # keeps on running all time.
# while True:
#     # Checks whether a scheduled task 
#     # is pending to run or not
#     schedule.run_pending()
#     time.sleep(1)


    
# def update_dropbox():
#     from shutil import copytree
#     shutil.rmtree('/home/elemen/Dropbox/Code/')
#     src =  '/home/elemen/Documents/Code/'
#     dest = '/home/elemen/Dropbox/Code/'
#     destination  = shutil.copytree(src, dest)
#     print('Dropbox has been updated to current')

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'

# This works to merge video clips into one.     
def merge_videos():
    my_directory = my_path +'Videos/Mandalas/'
    os.chdir(my_path + 'Videos/Mandalas/')
    # Select and input the files to merge
    clip1= VideoFileClip(my_directory + "Mixed-Hued Mandala_75.avi")
    clip2= VideoFileClip(my_directory + "Mixed-Hued Mandala_120.avi")
    clip3= VideoFileClip(my_directory + "Mixed-Hued Mandala_165.avi")
    clip4= VideoFileClip(my_directory + "Mixed-Hued Mandala_210.avi")
    clip5= VideoFileClip(my_directory + "Mixed-Hued Mandala_255.avi")
    clip6= VideoFileClip(my_directory + "Mixed-Hued Mandala_300.avi")
    clip7= VideoFileClip(my_directory + "Mixed-Hued Mandala_345.avi")
    clip8= VideoFileClip(my_directory + "Mixed-Hued Mandala_390.avi")
    clip9= VideoFileClip(my_directory + "Mixed-Hued Mandala_435.avi")
    clip10= VideoFileClip(my_directory + "Mixed-Hued Mandala_480.avi")         
             

    final_clip= concatenate_videoclips([clip1, clip2, clip3, clip4, clip5, clip6, clip7, clip8, clip9, clip10])
    #Change the name as appropriate
    final_clip.write_videofile(my_directory + "Mixed-Hued Mandalas_01.mp4")

#merge_videos()     
     
            


'^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'
# Used by Mandala Maker to create videos from the .png files.
# This works using moviepy on a single folder. Does not loop. Optional codecs are 'mpeg4', libx264(.mp4), 'rawvideo'(.avi),\
                                    # libvpx(webm)-HTML5 and browser videos.
def try_video():
    import os
    import moviepy.video.io.ImageSequenceClip
    import moviepy
#     from moviepy.editor import *
    import natsort
    from natsort import humansorted
    import my_angles as a
    fps = 1.75 
    # Make images directory current
    os.chdir(loc_thumb + folder_name +'/')
    #Collect and sort .png files
    image_files = humansorted(os.listdir('.'))
    my_clip =  moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
#     my_clip_a = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
    #     os.chdir(loc_thumb + folder_name)
    # Write sequenced png files to a single .mp4 file normally less than 10 mb, quality as good as much larger .avi file
    # insert this after my_clip as needed to control duration: .set_duration(240).
    my_clip.write_videofile( con_vid_no_audio + folder_name + '.mp4', fps=30,
                            codec='libx264', bitrate=None, audio=False, audio_fps=44100, preset='medium', audio_nbytes=4,
                            audio_codec='mp3', audio_bitrate=None, audio_bufsize=4000, temp_audiofile='E:/temp',
                            remove_temp=False, write_logfile=True, threads=None,
                            ffmpeg_params=None, logger='bar')
    # Write sequenced .png files to a single .avi file normally exceeding 200 mb 
#     my_clip_a.set_duration(265).write_videofile( loc_thumb + folder_name +'.avi', fps=24,\
#                             codec='png', bitrate=None, audio=False, audio_fps=44100, preset='medium', audio_nbytes=4,\
#                             audio_codec=None, audio_bitrate=None, audio_bufsize=2000, temp_audiofile=None,\
#                             remove_temp=True, write_logfile=False, threads=None,\
#                             ffmpeg_params=None, logger='bar')

    print('Video is Ready')
  
# try_video()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
# Used by Master Mandala maker Module to create videos from looped .png files
def set_vid_env():
    current_path()
    os.chdir(loc_thumb + folder_name + '/')
    print('The current folder is:  ' + str(loc_thumb + folder_name))
    try_video()
    os.chdir(my_path + '/Make_Mandalas/')
    
    
    

def a_v_merge():
    os.chdir(con_vid +'no_audio/')
    my_file = folder_name  # ['colorful_mandala_765', 'Blue and Red Hued Mandala_765','Mixed-Hued Mandala_765']
    
#     videoclip = VideoFileClip('E:/Videos/no_audio/' + my_file + '.mp4')
    videoclip = VideoFileClip(my_path + 'no_audio/' + my_file + '.mp4')
    audioclip = AudioFileClip(AudioFileClip(au.my_track))
#     videoclip.duration = audioclip.duration # set duration of video to duration of audio
    audioclip.duration = videoclip.duration # set duration of audio to duration of video
    new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip
    videoclip.write_videofile(my_path +'Videos/AV Vids/' + my_file + '_with music' + '.mp4')
    
#     videoclip.set_duration(179).write_videofile(my_file + '_with Music' + '.mp4')
    
# a_v_merge()

#  https://www.geeksforgeeks.org/moviepy-assigning-audio-clip-to-video-file/
# Used by Master Mandala maker to generate videos by merging audio clips to video clips
def sync_av():
    i_key = str(t.file_key)
    os.chdir(con_vid)
    new_video = '__temp__.mp4'
    audio_file = au.my_audio_clip
    my_file = folder_name
    print('Audio file::   ' + str(audio_file))
    print('my_file:   ' + str(my_file))
    # loading video gfg
    clip = VideoFileClip(my_path + '/Videos/no_audio/' + my_file +'.mp4')
    # select from 0 to x seconds, approx duration of the original video
    clip = clip.subclip(0, 999) # Limited by the maxduration variable to 179s duration
  
    # loading audio file
    audioclip = AudioFileClip(audio_file) # .clip
  
    # adding audio to the video clip
    videoclip = clip.set_audio(audioclip)
  
                #     # showing video clip
    videoclip.ipython_display(loop = 5, maxduration = 999)
#     shutil.move(os.path.join(new_video),os.path.join('E:/Videos/Full_Vids/' + my_file + '_' + au.my_track + '_audio.mp4'))
    shutil.move(os.path.join(new_video),os.path.join(my_path + '/Videos/Full_Vids/' +  my_file + '-' + au.my_track + '_.mp4'))
    
    print('The new video has been renamed to    ' + str(my_file) + '-' + au.my_track + '_.mp4')
   
#     my_clip= (VideoFileClip('E:/Videos/Full_Vids/' + my_file + '_' + au.my_track + '_audio.mp4'))
#     my_clip= (VideoFileClip(my_path + 'Videos/Full_Vids/' + my_file + au.my_track + '_.mp4'))
    os.chdir(loc_code)
    print('=========================================')    
    
# sync_av()    
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
def longer_video():
   
    my_video = my_path +'Awesome Mandala713.avi'
    new_video = '__temp__.mp4'
    # loading video dsa gfg intro video 
    clip = VideoFileClip(my_video) 
         
    # getting first 60 seconds
    clip = clip.subclip(0, 60)
      
    # new clip with new duration
    new_clip = clip.set_duration(130)
      
      
    # new clip with new duration
    new_clip.ipython_display(width = 1050)
    
    #rename the newly created .mp4 file
    shutil.move(os.path.join(new_video),os.path.join(my_video))
# longer_video()







'^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'
'*******************************************************************************************************************************'
# This absolutely works  using cv2 VideoWriter to create .avi videos on a single folder. Does not loop directories, but does loop the files.
# import cv2
# import numpy as np
# import os
# from natsort import humansorted
# import natsort
from os.path import isfile, join

def convert_frames_to_video(pathIn,pathOut,fps):
    frame_array = []
    files = humansorted([f for f in os.listdir(pathIn) if isfile(join(pathIn, f))])

    for i in range(len(files)):
        filename=pathIn + files[i]
        #reading each file
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        #Checks for the accuracy of sorted files to be converted
        print(i,filename)
        #inserting the frames into an image array
        frame_array.append(img)
       
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    out.release()
    print('Video is ready!')
    
def main():
    folder_name = my_path + 'Thumbs/Output/square_spiral_333/'
    pathIn=  folder_name
    pathOut = folder_name + '_mandala_show.avi'
    
    fps = 1.0
    convert_frames_to_video(pathIn, pathOut, fps)

# if __name__=="__main__":
#     main()

'************************************************************************************************************'




#  Output shell to a file
def begin_output_to_file():
    import sys
    original_stdout = sys.stdout
    filename.txt = str(t.my_str + 'ran on' + str(Tm.date_time))
    sys.stdout = open('filename.txt', w)
    print("test sys.stdout")
    sys.stdout = original_stdout
# begin_output_to_file()

def close_output_to_file():
    print('Closing output to file')
    filename.txt = str(t.my_str + 'ran on' + str(Tm.date_time))
    sys.stdout = close('filename.txt', w)
    sys.stdout = original_stdout


def output_to_text():
    import sys
    filename.txt = t.my_str + 'ran on' + str(Tm.date_time)
    print('filename.txt = str(t.my_str + ran on + str(Tm.date_time))')
    print(' By LeonRHatton')
    original_stdout = sys.stdout # Save a reference to the original standard output

    with open('filename.txt', 'w') as f:
        sys.stdout = f # Change the standard output to the file we created.
        print('This message will be written to a file.')
        print('This, too! ')
        print( 'And this too?')
        sys.stdout = original_stdout # Reset the standard output to its original value
        
    
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
        src = my_path + 'Images/An Awesome Polygram Mandala featuring 1512  Degree Angles_999_.jpg'  
        dest = my_path + 'An Awesome Polygram Mandala featuring 1512  Degree Angles' + str(num) + '.jpg'
        destination  = shutil.copyfile(src, dest)
    print('Files have been copied')   
        
# copy_pics()   

# Process 300 jpegs
def process_pics():
    import os
    import moviepy.video.io.ImageSequenceClip
    import moviepy
    import natsort
    from natsort import humansorted
    import my_angles as a
    fps = 1.75 # 1.75 value creates a video with audio file of 3 minutes, the max duration value of moviepy. Best with 300 loops.
    # Make images directory current
    my_dir = my_path +'300_pics/Mixed Hues 834/'
    os.chdir(my_dir)
    #Collect and sort .jpg files
    image_files = humansorted(os.listdir('.'))
    my_clip =  moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
#   # Write sequenced png files to a single .mp4 file normally less than 10 mb, quality as good as much larger .avi file
    # insert this after my_clip as needed to control duration: .set_duration(240).
    my_clip.write_videofile( my_dir +'MixedHues_834.mp4', fps=30,\
                            codec='libx264', bitrate=None, audio=False, audio_fps=44100, preset='medium', audio_nbytes=4,\
                            audio_codec='mp3', audio_bitrate=None, audio_bufsize=4000, temp_audiofile= my_path +'Music/temp',
                            remove_temp=False, write_logfile=True, threads=None,\
                            ffmpeg_params=None, logger='bar')
    # Write sequenced .png files to a single .avi file normally exceeding 200 mb 
#     my_clip_a.set_duration(265).write_videofile( loc_thumb + folder_name +'.avi', fps=24,\
#                             codec='png', bitrate=None, audio=False, audio_fps=44100, preset='medium', audio_nbytes=4,\
#                             audio_codec=None, audio_bitrate=None, audio_bufsize=2000, temp_audiofile=None,\
#                             remove_temp=True, write_logfile=False, threads=None,\
#                             ffmpeg_params=None, logger='bar')
    print('mp4 created!')
# process_pics()    
'**************************************************************************************************************************************'
this_file = my_path +'/Python/Make_Mandalas/my_angles.py'

def print_to_file():
    my_file = open(this_file)
    for line in my_file:
        print(line)
# print_to_file()        

