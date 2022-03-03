#FileScripts.py contains file manipulation scripts associated with master_mandala_maker.py
             # by LeonRHatton



import os
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
from pathlib import Path
from glob import glob, iglob
import imageio
import my_angles as a
from moviepy.editor import *
import audio_clips as au
from moviepy.editor import AudioFileClip, ImageClip



global loc_code
loc_code = '/home/elemen/Make_Mandalas/'

global folder_name
folder_name = 'Images_TBD'

global loc_pic
loc_pic = '/media/elemen/Container/Images/' # Store Mandala jpg files here

global con_vid
con_vid = '/media/elemen/Container/Videos/'

global con_vid_no_audio
con_vid_no_audio = '/media/elemen/Container/Videos/no_audio/' # Store non audio Mandala videos here

global con_vid_av
con_vid_av = '/media/elemen/Container/Videos/AV Vids/Full_Vids/'

global loc_thumb
loc_thumb = '/media/elemen/Container/Thumbs/Output/' # Store Mandala Thumbs here


'**********************************************************************************************************'
# Audio Zone

#Path to songs
# Album: Jubilee, by Winston Rhodes
jub_00 = '/home/elemen/Music/Jubilee/Jubilee/\'Jubilee\'!.ogg'
jub_14 = '/home/elemen/Music/Jubilee/Jubilee/14 - Life\'s Storms.ogg'
jub_13 = '/home/elemen/Music/Jubilee/Jubilee/13 - Thank God I\'m Forgiven.ogg'
jub_12 = '/home/elemen/Music/Jubilee/Jubilee/12 - Trav\'lin On The Tracks of Life.ogg'
jub_11 = '/home/elemen/Music/Jubilee/Jubilee/11 - Music Still Blowing In The Wind.ogg'
jub_10 = '/home/elemen/Music/Jubilee/Jubilee/10 - On A Heavenly Journey.ogg' # Comment out if Duration too short, causing backend error. 
jub_09 = '/home/elemen/Music/Jubilee/Jubilee/09 - A Rasta Man\'s Prayer.ogg'
jub_08 = '/home/elemen/Music/Jubilee/Jubilee/08 - Drink From The Living Water.ogg'
jub_07 = '/home/elemen/Music/Jubilee/Jubilee/07 - On The Hallelujah Trail.ogg'
jub_06 = '/home/elemen/Music/Jubilee/Jubilee/06 - Spread Your Tender Mercy Over Me.ogg'
jub_05 = '/home/elemen/Music/Jubilee/Jubilee/05 - His Majesty, God!.ogg'
jub_04 = '/home/elemen/Music/Jubilee/Jubilee/04 - Heading To Zion.ogg'
jub_03 = '/home/elemen/Music/Jubilee/Jubilee/03 - I Never Knew.ogg'
jub_02 = '/home/elemen/Music/Jubilee/Jubilee/02 - Yes I\'m Still Here Lord.ogg'

# Mix
mix_01 = '/home/elemen/Music/Stored Jams/Music/The 60\'s Hits/Sam Cooke - Change Is Gonna Come.mp3'
my_mix = mix_01.lstrip('/home/elemen/Music/Stored Jams/Music/' + 'The 60\'s Hits/Sam Cooke - Change Is Gonna Come.mp3')

global jubilee_album
jubilee_album = [jub_00, jub_14, jub_02, jub_03, jub_04, jub_05, jub_06, jub_07, jub_08, jub_09, jub_11, jub_12, jub_13]

def pick_track():
    global random_track # global keyword is important here to make objects available outside of the module
    random_track =  random.choice(au.all_clips) # Can use(jubilee_album)
    global my_track
    my_track = random_track.lstrip('home/elemen/Music/Audio Clips for Python')  # or ('home/elemen/Music/Jubilee/') + ',  by Winston W. Rhodes'
    print('The track being used for this show is: ' + my_track)
    return my_track

'*******************************************************************************************************************'
      





# Backs up the code to current. Does not archive yet. 
def code_backup():
    shutil.rmtree('/home/elemen/CodeBackup/')
    shutil.rmtree('/home/elemen/MandalaMakerBackup/')
    src =  '/home/elemen/Python Code/'
    m_src = '/home/elemen/Make_Mandalas/'
    dest = '/home/elemen/CodeBackup/'
    m_dest = '/home/elemen/MandalaMakerBackup/'
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
    cv2.imwrite(t.my_str + '+' + str(t.iterable) +'.png', image)
    
    
# This creates  png and jpg files of the final image, to be saved out to the Pictures/Mandalas folder.
def save_final_thumb():
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite(t.my_str +'_' + '999' + '_' +'.jpg', image)
    cv2.imwrite(t.my_str +'_' + '998' + '_' + '.png', image)
   
    

 
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
    print('Image .png files have been moved to /media/elemen/Container/Thumbs/Output/')
    print('Image .jpg files have been moved to /media/elemen/Container/Images/')
# move_pics()    

# Video files originate in the /media/elemen/Thumbs/Output folder. This will move them to the /media/Container/Videos folder.
# Moves images to their respective locations from the code file and leaving .py files only, then to larger size drive(Container)
# Runs best with Master Mandala Maker. Using list comprehension syntax.
def move_all():
    origin = loc_thumb +'/'
    destination = con_vid
    endswith_ = '.avi'
    [shutil.move(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
    print('Video .avi files have been moved to /media/elemen/Container/Videos/')
    
    origin = loc_thumb +'/'
    destination = con_vid_no_audio
    endswith_ = '.mp4'
    [shutil.move(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
    print('Video .mp4 files have been moved to /media/elemen/Container/Videos/')
    
    origin = loc_thumb +'/'
    destination = con_vid
    endswith_ = '.webm'
    [shutil.move(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
    print('Video .webm files have been moved to /media/elemen/Container/Videos/')
    
    origin = loc_code +'/'
    destination = loc_thumb + folder_name +'/'
    endswith_ = '.png'
    [shutil.move(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
    print('Image .png files have been moved to /media/elemen/Container/Thumbs/Output/')
    
    origin = loc_thumb + folder_name +'/'
    destination = loc_pic
    endswith_ = '.jpg'
    [shutil.move(os.path.join(origin,i),os.path.join(destination,i)) for i in os.listdir(origin) if i.endswith(endswith_)]
    print('Image .jpg files have been moved to /media/elemen/Container/Images/')
    
# move_all()




# Empties the Pictures folder where final jpgs are stored. Default is to leave commented to avoid accidental purging.
# def clear_pics_mandalas():
#     file = pathlib.Path('/home/elemen/Pictures/Mandalas/')
#     if file.exists ():
#         shutil.rmtree('/home/elemen/Pictures/Mandalas/') #       os.makedirs('/home/elemen/Pictures/Mandalas/')
#     else:
#         os.makedirs('/home/elemen/Pictures/Mandalas/')
#     print('Pictures/Mandalas/ folder has been emptied. All files therein were permanently deleted.')



# Using Dropbox as file server to link the windows and phone
def update_dropbox():
    from shutil import copytree
    shutil.rmtree('/home/elemen/Dropbox/Code/')
    src =  '/home/elemen/Documents/Code/'
    dest = '/home/elemen/Dropbox/Code/'
    destination  = shutil.copytree(src, dest)
    print('Dropbox has been updated to current')
    
    
    
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
    os.chdir('/home/elemen/Python Code/')
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
    print('New temp directory /home/elemen/Looped_Pics/Thumbs/' + folder_name + '   has been created')



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
    os.chdir('/home/elemen/Make_Mandalas/')
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


    
def update_dropbox():
    from shutil import copytree
    shutil.rmtree('/home/elemen/Dropbox/Code/')
    src =  '/home/elemen/Documents/Code/'
    dest = '/home/elemen/Dropbox/Code/'
    destination  = shutil.copytree(src, dest)
    print('Dropbox has been updated to current')
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
# Used by Master Mandala maker Module to create videos from looped .png files
def set_vid_env():
#     time.sleep(3)
#     Tm.end_time()
#     move_pics()
    current_path()
    os.chdir(loc_thumb + folder_name + '/')
    print('The current folder is:  ' + str(loc_thumb + folder_name))
    try_video()
#     time.sleep(3)
#     move_all()
    os.chdir('/home/elemen/Make_Mandalas/')
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'

# This works to merge video clips into one.     
def merge_videos():
    my_directory = '/home/elemen/Videos/Mandalas/'
    os.chdir('/home/elemen/Videos/Mandalas/')
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
    fps = 1.75 # 1.75 value creates a video with audio file of 3 minutes, the max duration value of moviepy. Best with 300 loops.
    # Make images directory current
    os.chdir(loc_thumb + folder_name +'/')
    #Collect and sort .png files
    image_files = humansorted(os.listdir('.'))
    my_clip =  moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
#     my_clip_a = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
    #     os.chdir(loc_thumb + folder_name)
    # Write sequenced png files to a single .mp4 file normally less than 10 mb, quality as good as much larger .avi file
    # insert this after my_clip as needed to control duration: .set_duration(240).
    my_clip.write_videofile( con_vid_no_audio + folder_name +'.mp4', fps=30,\
                            codec='libx264', bitrate=None, audio=False, audio_fps=44100, preset='medium', audio_nbytes=4,\
                            audio_codec='mp3', audio_bitrate=None, audio_bufsize=4000, temp_audiofile='home/elemen/Music/temp',\
                            remove_temp=False, write_logfile=True, threads=None,\
                            ffmpeg_params=None, logger='bar')
    # Write sequenced .png files to a single .avi file normally exceeding 200 mb 
#     my_clip_a.set_duration(265).write_videofile( loc_thumb + folder_name +'.avi', fps=24,\
#                             codec='png', bitrate=None, audio=False, audio_fps=44100, preset='medium', audio_nbytes=4,\
#                             audio_codec=None, audio_bitrate=None, audio_bufsize=2000, temp_audiofile=None,\
#                             remove_temp=True, write_logfile=False, threads=None,\
#                             ffmpeg_params=None, logger='bar')

    print('Video is Ready')
    
    
    





    
# try_video()

def a_v_merge():
    os.chdir(con_vid +'/no_audio/')
    my_file = folder_name  # ['colorful_mandala_765', 'Blue and Red Hued Mandala_765','Mixed-Hued Mandala_765']
    
    videoclip = VideoFileClip('/media/elemen/Container/Videos/no_audio/' + my_file + '.mp4')
    audioclip = AudioFileClip(AudioFileClip(random_track))
    videoclip.duration = audioclip.duration
    new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip
    videoclip.write_videofile('/media/elemen/Container/AV Vids/' + my_file + '_with music' + '.mp4')
#     videoclip.set_duration(179).write_videofile(my_file + '_with Music' + '.mp4')
    
# a_v_merge()

#  https://www.geeksforgeeks.org/moviepy-assigning-audio-clip-to-video-file/
def sync_av():
    i_key = str(t.file_key)
    os.chdir(con_vid +'/')
    new_video = '__temp__.mp4'
#     audio_file = "/home/elemen/Music/Jubilee/Jubilee/12 - Trav'lin On The Tracks of Life.ogg"
    my_file = folder_name 
    # loading video gfg
    clip = VideoFileClip('/media/elemen/Container/Videos/no_audio/' + my_file + '.mp4')
  
    # select from 0 to x seconds, approx duration of the original video
    clip = clip.subclip(0, 179) # Limited by the maxduration variable to 179s duration
  
    # loading audio file
    audioclip = AudioFileClip(random_track) # .clip
  
    # adding audio to the video clip
    videoclip = clip.set_audio(audioclip)
  
                #     # showing video clip
    videoclip.ipython_display(loop = 5, maxduration = 999)
    shutil.move(os.path.join(new_video),os.path.join('/media/elemen/Container/AV Vids/Full_Vids/' + my_file + '_' + my_track + '_audio.mp4'))

    print('The new video has been renamed to    ' + str(my_file) + '_' + my_track + '_audio.mp4')
    my_clip = (VideoFileClip('/media/elemen/Container/AV Vids/Full_Vids/' + my_file + '_' + my_track + '_audio.mp4'))
    print('=========================================')    
    
# sync_av()    
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
def longer_video():
   
    my_video = '/media/elemen/Vids/Awesome Mandala713.avi'
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
import cv2
import numpy as np
import os
from natsort import humansorted
import natsort
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
    folder_name = '/media/elemen/Thumbs/Output/square_spiral_333/'
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
# output_to_file()

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



# Make multiple copies of a file

def copy_pics():
    for num in range(300):
        src = '/media/elemen/Container/Images/An Awesome Polygram Mandala featuring 1512  Degree Angles_999_.jpg'  
        dest = '/media/elemen/Container/300_pics/An Awesome Polygram Mandala featuring 1512/An Awesome Polygram Mandala featuring 1512  Degree Angles' + str(num) + '.jpg'
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
    my_dir = '/media/elemen/Container/300_pics/Mixed Hues 834/'
    os.chdir(my_dir)
    #Collect and sort .jpg files
    image_files = humansorted(os.listdir('.'))
    my_clip =  moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
#   # Write sequenced png files to a single .mp4 file normally less than 10 mb, quality as good as much larger .avi file
    # insert this after my_clip as needed to control duration: .set_duration(240).
    my_clip.write_videofile( my_dir +'MixedHues_834.mp4', fps=30,\
                            codec='libx264', bitrate=None, audio=False, audio_fps=44100, preset='medium', audio_nbytes=4,\
                            audio_codec='mp3', audio_bitrate=None, audio_bufsize=4000, temp_audiofile='home/elemen/Music/temp',\
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